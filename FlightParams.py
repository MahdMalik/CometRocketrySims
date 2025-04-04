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