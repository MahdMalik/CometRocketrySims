from rocketpy.mathutils.function import Function
from rocketpy.motors import motor

# HERE ARE THE VARIABLES YOU WILL HAVE TO CHANGE

#motor
propellant_mass = 4.122
totalMotorMass = 6.032
grainInnerRadius = 0.022225/2
grainOuterRadius = 0.0654558/2
grainHeight = 0.1317752
motorRadius = 75 / 2 * 10**(-3)
motorLength = .923
the_nozzle_radius = .047625/2
the_throat_radius= .017399/2
the_nozzle_position = .1317752 * 3 + 0.08
grain_center_of_mass_position = 0
center_of_dry_mass_within_motor = 0
motor_thrust_file = "AeroTech_M1850WSledge.csv"
motor_volume = grainHeight * 0.0114332036534 + (grainHeight * .011908241951)*5
burn_time = 2.505
numGrains = 6
grainSeparation = 0

#rocket general
spMass = 16.4
spRadius = 0.155/2
spLength = .152 + .305 + .559 + .508 + .356 + .152
the_center_of_mass_without_motor = 1.87
spLength = .864 + 1.02
power_off_file = "SPCDOFFSledge.csv"
power_on_file = "SPCDONSledge.csv"

#nose cone
nose_cone_length = .813

#fins
the_fin_position = 2.62
finSpan = 0.146
root_chord=0.364
tip_chord=0.164
fin_cant_angle = 0
fin_sweep_length = 0.15
numFins = 4

#bottail
boattailPos = 0.813+0.152+0.305+0.559+0.508+0.356+0.152
boattailPos = 2.64-.152
boattail_bottom_radius = 0.05
bottail_length = 0.152

#parachutes
drogueRadius = 0.61/2
drogueCdS = 0.97*3.1415*(drogueRadius)**2
lightRadius = 3.05/2
lightCdS = 2.2*3.1415*(lightRadius)**2
lag_rec = 0
lag_se = 0
drogueTrigger = "apogee"
lightTrigger = 110

#rail buttons
upper_railbutton_position = 1.57 + .44
lower_railbutton_position = 1.57 + .44 + .44
railbutton_angular_position = 180


#environment
fahrenheit_temp = 80
envParams = {
    "latitude": 32.9823279,
    "longitude": -106.9490122,
    "elevation": 1400.556,
    "type": "custom_atmosphere",
}

#final rocket stuff
inclination = 88
heading = 90
rail_length = 4.572

#airbrakes
air_brake_drag_file = [
        # Mach 0.1
        [0, 0.1, 0.7692],
        [10 / 100, 0.1, 0.7663],
        [20 / 100, 0.1, 0.7762],
        [30 / 100, 0.1, 0.7847],
        [40 / 100, 0.1, 0.7999],
        [50 / 100, 0.1, 0.8246],
        [60 / 100, 0.1, 0.8310],
        [70 / 100, 0.1, 0.8499],
        [80 / 100, 0.1, 0.8738],
        [90 / 100, 0.1, 0.8945],
        [100 / 100, 0.1, 1.1018],
        # Mach 0.2
        [0, 0.2, 0.7508],
        [10 / 100, 0.2, 0.7513],
        [20 / 100, 0.2, 0.7670],
        [30 / 100, 0.2, 0.7782],
        [40 / 100, 0.2, 0.7943],
        [50 / 100, 0.2, 0.8063],
        [60 / 100, 0.2, 0.8243],
        [70 / 100, 0.2, 0.8493],
        [80 / 100, 0.2, 0.8781],
        [90 / 100, 0.2, 0.8925],
        [100 / 100, 0.2, 0.9851],
        # Mach 0.3
        [0, 0.3, 0.7445],
        [10 / 100, 0.3, 0.7571],
        [20 / 100, 0.3, 0.7699],
        [30 / 100, 0.3, 0.7828],
        [40 / 100, 0.3, 0.7985],
        [50 / 100, 0.3, 0.8114],
        [60 / 100, 0.3, 0.8379],
        [70 / 100, 0.3, 0.8634],
        [80 / 100, 0.3, 0.8834],
        [90 / 100, 0.3, 0.8947],
        [100 / 100, 0.3, 0.9782],
        # Mach 0.4
        [0, 0.4, 0.7492],
        [10 / 100, 0.4, 0.7566],
        [20 / 100, 0.4, 0.7698],
        [30 / 100, 0.4, 0.7840],
        [40 / 100, 0.4, 0.7994],
        [50 / 100, 0.4, 0.8136],
        [60 / 100, 0.4, 0.8399],
        [70 / 100, 0.4, 0.8665],
        [80 / 100, 0.4, 0.8834],
        [90 / 100, 0.4, 0.8969],
        [100 / 100, 0.4, 0.9659],
        # Mach 0.5
        [0, 0.5, 0.7454],
        [10 / 100, 0.5, 0.7537],
        [20 / 100, 0.5, 0.7651],
        [30 / 100, 0.5, 0.7811],
        [40 / 100, 0.5, 0.7987],
        [50 / 100, 0.5, 0.8163],
        [60 / 100, 0.5, 0.8404],
        [70 / 100, 0.5, 0.8631],
        [80 / 100, 0.5, 0.8788],
        [90 / 100, 0.5, 0.8951],
        [100 / 100, 0.5, 0.9416],
        # Mach 0.6
        [0, 0.6, 0.7036],
        [10 / 100, 0.6, 0.7237],
        [20 / 100, 0.6, 0.7359],
        [30 / 100, 0.6, 0.7496],
        [40 / 100, 0.6, 0.7684],
        [50 / 100, 0.6, 0.7899],
        [60 / 100, 0.6, 0.8153],
        [70 / 100, 0.6, 0.8406],
        [80 / 100, 0.6, 0.8539],
        [90 / 100, 0.6, 0.8712],
        [100 / 100, 0.6, 0.9286],
        # Mach 0.7
        [0, 0.7, 0.6810],
        [10 / 100, 0.7, 0.6948],
        [20 / 100, 0.7, 0.7076],
        [30 / 100, 0.7, 0.7233],
        [40 / 100, 0.7, 0.7427],
        [50 / 100, 0.7, 0.7629],
        [60 / 100, 0.7, 0.7876],
        [70 / 100, 0.7, 0.8073],
        [80 / 100, 0.7, 0.8272],
        [90 / 100, 0.7, 0.8453],
        [100 / 100, 0.7, 0.8960],
        # Mach 0.8
        [0, 0.8, 0.6578],
        [10 / 100, 0.8, 0.6739],
        [20 / 100, 0.8, 0.6870],
        [30 / 100, 0.8, 0.7036],
        [40 / 100, 0.8, 0.7240],
        [50 / 100, 0.8, 0.7457],
        [60 / 100, 0.8, 0.7676],
        [70 / 100, 0.8, 0.7880],
        [80 / 100, 0.8, 0.8098],
        [90 / 100, 0.8, 0.8278],
        [100 / 100, 0.8, 0.8799],
        # Mach 0.9
        [0, 0.9, 0.6574],
        [10 / 100, 0.9, 0.6634],
        [20 / 100, 0.9, 0.6794],
        [30 / 100, 0.9, 0.6958],
        [40 / 100, 0.9, 0.7201],
        [50 / 100, 0.9, 0.7395],
        [60 / 100, 0.9, 0.7618],
        [70 / 100, 0.9, 0.7844],
        [80 / 100, 0.9, 0.8057],
        [90 / 100, 0.9, 0.8278],
        [100 / 100, 0.9, 0.8628],
        # Mach 1.0
        [0, 1.0, 0.8350],
        [10 / 100, 1.0, 0.8241],
        [20 / 100, 1.0, 0.8403],
        [30 / 100, 1.0, 0.8593],
        [40 / 100, 1.0, 0.8832],
        [50 / 100, 1.0, 0.9070],
        [60 / 100, 1.0, 0.9358],
        [70 / 100, 1.0, 0.9639],
        [80 / 100, 1.0, 0.9881],
        [90 / 100, 1.0, 1.0093],
        [100 / 100, 1.0, 1.0347],
        # Mach 1.1
        [0, 1.1, 0.8610],
        [10 / 100, 1.1, 0.8447],
        [20 / 100, 1.1, 0.8617],
        [30 / 100, 1.1, 0.8800],
        [40 / 100, 1.1, 0.9027],
        [50 / 100, 1.1, 0.9244],
        [60 / 100, 1.1, 0.9515],
        [70 / 100, 1.1, 0.9810],
        [80 / 100, 1.1, 1.0069],
        [90 / 100, 1.1, 1.0253],
        [100 / 100, 1.1, 1.0560],
    ]
airbrake_sample_rate = 10 # 10 herz, so every .1 seconds
airbrake_clamp = True
override_rocketdrag_with_airbrakedrag = False
airbrake_area = 2 # in meters
airbrake_deploy_altitude = 1000
def airbrake_controller_function(time, sampling_rate, state, state_history, observed_variables, air_brakes, env):
    # state = [x, y, z, vx, vy, vz, e0, e1, e2, e3, wx, wy, wz]
    altitude_ASL = state[2]
    altitude_AGL = altitude_ASL - env.elevation
    vx, vy, vz = state[3], state[4], state[5]

    # Get winds in x and y directions
    wind_x, wind_y = env.wind_velocity_x(altitude_ASL), env.wind_velocity_y(altitude_ASL)

    # Calculate Mach number
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
    if time < burn_time:
        return None

    # If below 1500 meters above ground level, air_brakes are not deployed
    if altitude_AGL < airbrake_deploy_altitude:
        air_brakes.deployment_level = 0

    # Else calculate the deployment level
    else:
        # Controller logic
        new_deployment_level = (
            air_brakes.deployment_level + 0.1 * vz + 0.01 * previous_vz**2
        )

        # Limiting the speed of the air_brakes to 0.2 per second
        # Since this function is called every 1/sampling_rate seconds
        # the max change in deployment level per call is 0.2/sampling_rate
        max_change = 0.2 / sampling_rate
        lower_bound = air_brakes.deployment_level - max_change
        upper_bound = air_brakes.deployment_level + max_change
        new_deployment_level = min(max(new_deployment_level, lower_bound), upper_bound)

        air_brakes.deployment_level = new_deployment_level

    # Return variables of interest to be saved in the observed_variables list
    return (
        time,
        air_brakes.deployment_level,
        air_brakes.drag_coefficient(air_brakes.deployment_level, mach_number),
    )



# HERE ARE THE VARIABLES YOU DON'T HAVE TO CHANGE
dryMotorMass = totalMotorMass - propellant_mass
totalHeight = grainHeight * numGrains
motor_11_inertia = (0.08333)*dryMotorMass*(motorRadius)**2
motor_density = propellant_mass/motor_volume
motor_33_inertia = ((1/4)*dryMotorMass*(motorRadius)**2) + (1/12)*dryMotorMass*(motorLength)**2
the_motor_position = spLength + nose_cone_length + grainHeight/2 - (totalHeight)/2
the_motor_center_of_dry_mass_position = the_motor_position

_, _, points = motor.Motor.import_eng("ReferencedFiles/" + motor_thrust_file)
thrust_source = points
interpolation_method = "linear"
thrust = Function(thrust_source, "Time (s)", "Thrust (N)", interpolation_method, "zero")
impulse = thrust.integral(0, burn_time)

spCentralAxis = (spRadius**2)*spMass*2/12
spCentralDiameter = ((1/4)*spMass*(spRadius)**2) + (1/12)*spMass*(totalHeight)**2
rocket_center_of_dry_mass_position = (the_center_of_mass_without_motor * spMass + the_motor_center_of_dry_mass_position * dryMotorMass) / (dryMotorMass + spMass)

power_off = 1
power_on = 1
kelvin_temp = (fahrenheit_temp - 32) * 5/9 + 273.15
nose_position = 0