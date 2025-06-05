from rocketpy.mathutils.function import Function
from rocketpy.motors import motor
import numpy as np

# HERE ARE THE VARIABLES YOU WILL HAVE TO CHANGE

#other stuff
varyingPossibilities = ["airbrake", "finposition", "weatherHour"]
varyingVariable = varyingPossibilities[2]

numberSims = 5
processes = 5

latitude = 31.0437
longitude = -103.532806

generatedFilesLocation ="IrecSims/"

#motor
propellant_mass = 4.898
dryMotorMass = 4.896
grainInnerRadius = (43.942 * 10 ** -3) /2
grainOuterRadius = (82.27 * 10 ** -3) / 2
grainHeight = 0.127
the_nozzle_radius = (79.32 * 10 ** -3) / 2
the_throat_radius= (29.21 * 10 ** -3) / 2
the_nozzle_position = grainHeight * 3.9
grain_center_of_mass_position = 0
center_of_dry_mass_within_motor = 0
motor_thrust_file = "testthrustcurve.csv"
burn_time = 4.13
numGrains = 6
motorLength = grainHeight * numGrains
grainSeparation = 0

#rocket general
spMass = 16.656
spRadius = 0.155/2
spLength = .152 + .305 + .559 + .508 + .356 + .152
the_center_of_mass_without_motor = 1.89
power_off_file = "Sp25CDOFF4.24.csv"
power_on_file = "Sp25CDON4.24.csv"

#nose cone
nose_cone_length = .813
nose_cone_type = "von karman"

#fins
the_fin_position = 2.62
finSpan = 0.216
root_chord=0.279
tip_chord=0.091
fin_cant_angle = 0
fin_sweep_length = 0.173
numFins = 4

#bottail
boattailPos = 0.813+0.152+0.305+0.559+0.508+0.356+0.152
boattail_bottom_radius = 0.129/2
bottail_length = 0.203

#parachutes
drogueRadius = 0.61/2
drogueCdS = 0.97*3.1415*(drogueRadius)**2
lightRadius = 3.05/2
lightCdS = 2.2*3.1415*(lightRadius)**2
lag_rec = 0
lag_se = 0
drogueTrigger = "apogee"
lightTrigger = 450

#rail buttons
lower_railbutton_position = 2.79
upper_railbutton_position = lower_railbutton_position - 0.274
railbutton_angular_position = 135


#environment
fahrenheit_temp = 80
envParams = {
    "latitude": 32.9823279,
    "longitude": -106.9490122,
    "elevation": 1400.556,
    "type": "custom_atmosphere",
}

#final rocket stuff
inclination = 84
heading = 90
rail_length = 5.2

#airbrakes
air_brake_drag_file = "ReferencedFiles/AirbrakeDrag.csv"
airbrake_sample_rate = 1 # 1 herz, so every .1 seconds
airbrake_clamp = True
override_rocketdrag_with_airbrakedrag = True
airbrake_area = 2 # in meters

halfway_to_target = 1524

# airbrake_deploy_altitude = 2000
def airbrake_controller_function(time, sampling_rate, state, state_history, observed_variables, air_brakes, env):
    canDeployAirbrake = False

    deployment_time = air_brakes.airbrake_deploy_time

    # state = [x, y, z, vx, vy, vz, e0, e1, e2, e3, wx, wy, wz]
    altitude_ASL = state[2]
    altitude_AGL = altitude_ASL - env.elevation
    vx, vy, vz = state[3], state[4], state[5]

    # Get winds in x and y directions
    wind_x, wind_y = env.wind_velocity_x(altitude_ASL), env.wind_velocity_y(altitude_ASL)

    # Calculate Mach number, by first getting entire speed
    free_stream_speed = (
        (wind_x - vx) ** 2 + (wind_y - vy) ** 2 + (vz) ** 2
    ) ** 0.5
    mach_number = free_stream_speed / env.speed_of_sound(altitude_ASL)

    # Get previous state from state_history
    previous_state = state_history[-1]
    previous_vz = previous_state[5]

    # If we wanted to we could get the returned values from observed_variables:
    # returned_time, deployment_level, drag_coefficient = observed_variables[-1]

    # Check if the rocket has reached burnout
    if (time > burn_time and deployment_time <= time and altitude_AGL > halfway_to_target):
        canDeployAirbrake = True
    # Else calculate the deployment level
   
    # else:
    #     # Controller logic
    #     new_deployment_level = (
    #         air_brakes.deployment_level + 0.1 * vz + 0.01 * previous_vz**2
    #     )

    #     # Limiting the speed of the air_brakes to 0.2 per second
    #     # Since this function is called every 1/sampling_rate seconds
    #     # the max change in deployment level per call is 0.2/sampling_rate
    #     max_change = 0.2 / sampling_rate
    #     lower_bound = air_brakes.deployment_level - max_change
    #     upper_bound = air_brakes.deployment_level + max_change
    #     new_deployment_level = min(max(new_deployment_level, lower_bound), upper_bound)

    #     air_brakes.deployment_level = new_deployment_level

    # Return variables of interest to be saved in the observed_variables list
    
    return (
        "airbrake" + str(canDeployAirbrake),
        time,
        air_brakes.deployment_level,
        air_brakes.drag_coefficient(air_brakes.deployment_level, mach_number),
    )





# HERE ARE THE VARIABLES YOU DON'T HAVE TO CHANGE
totalMotorMass = dryMotorMass + propellant_mass
totalHeight = grainHeight * numGrains
# area = pi * r^2 * height
motor_volume = (((np.pi * grainOuterRadius ** 2) - (np.pi * grainInnerRadius ** 2)) * totalHeight)
motor_11_inertia = (1/12)*dryMotorMass*(grainOuterRadius)**2
motor_density = propellant_mass/motor_volume
motor_33_inertia = ((1/4)*dryMotorMass*(grainOuterRadius)**2) + (1/12)*dryMotorMass*(motorLength)**2
the_motor_position = spLength + nose_cone_length + grainHeight/2 - (totalHeight)/2
the_motor_center_of_dry_mass_position = the_motor_position

_, _, points = motor.Motor.import_eng("ReferencedFiles/" + motor_thrust_file)
thrust_source = points
interpolation_method = "linear"
thrust = Function(thrust_source, "Time (s)", "Thrust (N)", interpolation_method, "zero")
impulse = thrust.integral(0, burn_time)

spCentralAxis = (spRadius**2)*spMass*1/2
spCentralDiameter = ((1/4)*spMass*(spRadius)**2) + (1/12)*spMass*(spLength)**2
rocket_center_of_dry_mass_position = (the_center_of_mass_without_motor * spMass + the_motor_center_of_dry_mass_position * dryMotorMass) / (dryMotorMass + spMass)

power_off = 1
power_on = 1
kelvin_temp = (fahrenheit_temp - 32) * 5/9 + 273.15
nose_position = 0