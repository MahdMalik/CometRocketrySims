from rocketpy import Environment, SolidMotor, Rocket, Flight
from numpy.random import normal, choice
from time import process_time
import numpy as np

import logging

# Configure logging
def runFlightWithMonteCarlo(numOfSims, envParams, analysis_parameters, initial_cpu_time):
    logging.basicConfig(
    filename='app.log',  # Change this to your desired log file
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='a',  # 'w' for overwrite, 'a' for append
    )
    
    env = Environment(latitude=envParams["latitude"], longitude=envParams["longitude"], elevation=envParams["elevation"])
    env.set_atmospheric_model(type=envParams["type"], file = envParams["file"])
    flightData = ["", "", ""]
    i=0
    for setting in flight_settings(analysis_parameters, numOfSims):
        start_time = process_time()
        
        numGrain = 5
        
        MotorOne = SolidMotor(
            thrust_source="thrustcurve.csv", #Thrustcurve.org Mike Haberer - Rock Sim, Also uploaded to Google
            burn_time = 2.14,#Straight from thrustcurve.org
            reshape_thrust_curve=(setting["burn_time"], setting["impulse"]),
            nozzle_radius= setting["nozzle_radius"], # Part List
            throat_radius= setting["throat_radius"], # Part List
            grain_number=numGrain, #Based on cross-section
            grain_separation= setting["grain_separation"], # Good
            grain_density= setting["grain_density"], #Calculated mass of grain / volume of grain , for this i did - the core since it should be empty? not sure
            grain_outer_radius= setting["grain_outer_radius"], # Good
            grain_initial_inner_radius= setting["grain_initial_inner_radius"], # Good
            grain_initial_height= setting["grain_initial_height"] , # Good
            interpolation_method = "linear",
            coordinate_system_orientation="combustion_chamber_to_nozzle",
            nozzle_position = setting["nozzle_position"],#eyeballed
            grains_center_of_mass_position= 0,
            dry_mass=setting["motor_dry_mass"], #kg thrustcurve
            dry_inertia=(setting["motor_inertia_11"], setting["motor_inertia_11"], setting["motor_inertia_33"]), #based off drawing
            center_of_dry_mass_position= 0,
        )

        #Pretty Much done except grain density and maybe nozz)le position

        Sp25 = Rocket(
            mass = setting["rocket_mass"], #OpenRocket
            radius = setting["radius"], #OpenRocket
            inertia = (setting["rocket_inertia_11"], setting["rocket_inertia_11"],setting["rocket_inertia_33"]), # Calculated via Open Rocket
            coordinate_system_orientation = "nose_to_tail",
            center_of_mass_without_motor = 1.93, # OpenRocket
            power_off_drag ="Sp25CDOFF10.7.csv", #Uploaded to drive
            power_on_drag = "Sp25CDON10.7.csv", #Uploaded to drive
        )

        # CHANGE ONCE YOU FIND A GOOD WAY TO DO SO
        # Sp25.power_off_drag *= setting["power_off_drag"]
        # Sp25.power_on_drag *= setting["power_on_drag"]

        spLength = .152 + .305 + .559 + .508 + .356 + .152

        nose_cone = Sp25.add_nose(
            length = setting["nose_length"], kind = "lvhaack", position = 0)

        fin_set = Sp25.add_trapezoidal_fins(n=4, root_chord= setting["fin_root_chord"], tip_chord=setting["fin_tip_chord"], span=setting["fin_span"],
            fin_Position=setting["fin_distance_to_CM"] + Sp25.center_of_dry_mass_position,cant_angle=0, sweep_length=0.173)

        boattail = Sp25.add_tail(top_radius = setting["radius"], bottom_radius = 0.127/2,length = 0.203,position = spLength)

        Sp25.add_motor(MotorOne, spLength + nose_cone.length + setting["grain_initial_height"]/2 - (setting["grain_initial_height"] * numGrain)/2)
        
        topRB = 2.77-0.26-0.26
        rail_buttons = Sp25.set_rail_buttons(
            upper_button_position= topRB,
            lower_button_position= 2.77,
            angular_position=135
        )

        Drogue = Sp25.add_parachute(
            "Drogue",
            cd_s = setting["cd_s_drogue"],
            trigger = "apogee"
        )
        lightRadius = 3.05/2
        Light = Sp25.add_parachute(
            "Light",
            cd_s = 2.2*3.1415*(lightRadius)**2,
            trigger = 450
        )

        # Run trajectory simulation
        try:
            testFlight = Flight(
                rocket=Sp25, environment=env,rail_length = setting["rail_length"],inclination = setting["inclination"],heading=setting["heading"],
            )
            inputOutput = export_flight_data(setting, testFlight, process_time() - start_time, env)
            flightData[0] += "\n" + str(inputOutput[0])
            flightData[1] += "\n" + str(inputOutput[1])
        except Exception as E:
            print(E)
            flightData[2] += "\n" + str(export_flight_error(setting))
        # Register time
        i+=1
        if(i % 10 == 0):
            logging.getLogger().info(f"Curent iteration: {i:06d} | Average Time per Iteration: {(process_time() - initial_cpu_time)/i:2.6f} s")
    return flightData

def flight_settings(analysis_parameters, total_number):
    i = 0
    while i < total_number:
        # Generate a flight setting
        flight_setting = {}
        for parameter_key, parameter_value in analysis_parameters.items():
            if type(parameter_value) is tuple:
                flight_setting[parameter_key] = normal(*parameter_value)
            else:
                flight_setting[parameter_key] = choice(parameter_value)

        # Skip if certain values are negative, which happens due to the normal curve but isnt realistic
        if flight_setting["lag_rec"] < 0 or flight_setting["lag_se"] < 0:
            continue

        # Update counter
        i += 1
        # Yield a flight setting
        yield flight_setting

def export_flight_data(flight_setting, flight_data, exec_time, env):
    # Generate flight results
    flight_result = {
        "out_of_rail_time": flight_data.out_of_rail_time,
        "out_of_rail_velocity": flight_data.out_of_rail_velocity,
        "max_velocity": flight_data.speed.max,
        "apogee_time": flight_data.apogee_time,
        "apogee_altitude": flight_data.apogee - env.elevation,
        "apogee_x": flight_data.apogee_x,
        "apogee_y": flight_data.apogee_y,
        "impact_time": flight_data.t_final,
        "impact_x": flight_data.x_impact,
        "impact_y": flight_data.y_impact,
        "impact_velocity": flight_data.impact_velocity,
        "initial_static_margin": flight_data.rocket.static_margin(0),
        "out_of_rail_static_margin": flight_data.rocket.static_margin(
            flight_data.out_of_rail_time
        ),
        "final_static_margin": flight_data.rocket.static_margin(
            flight_data.rocket.motor.burn_out_time
        ),
        "number_of_events": len(flight_data.parachute_events),
        "execution_time": exec_time,
    }

    # Take care of parachute results
    if len(flight_data.parachute_events) > 0:
        flight_result["drogue_triggerTime"] = flight_data.parachute_events[0][0]
        flight_result["drogue_inflated_time"] = (
            flight_data.parachute_events[0][0] + flight_data.parachute_events[0][1].lag
        )
        flight_result["drogue_inflated_velocity"] = flight_data.speed(
            flight_data.parachute_events[0][0] + flight_data.parachute_events[0][1].lag
        )
    else:
        flight_result["drogue_triggerTime"] = 0
        flight_result["drogue_inflated_time"] = 0
        flight_result["drogue_inflated_velocity"] = 0
    # Write flight setting and results to file
    return [flight_setting, flight_result]

def export_flight_error(flight_setting):
    print()
    return flight_setting