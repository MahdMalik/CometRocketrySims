import ansys.fluent.core as pyfluent

# Connect to Fluent (can be local or remote)
session = pyfluent.launch_fluent(mode="solver", precision="double", processor_count=30, case_file_name="C:\\Users\\AIAA UT Dallas\\Desktop\\CFDTESTING-selected\\LeadingEdgeStudy\\LeadingEdgeStudy_files\\dp0\\FFF\\Fluent\\FFF.1-32.cas")

# Load initial case
#session.read_case(r"C:\Users\AIAA UT Dallas\Desktop\CFDTESTING-selected\LeadingEdgeStudy\LeadingEdgeStudy_files\dp0\FFF\Fluent\FFF.1-32.cas")

# Define list of velocities
velocities = [102.9, 205.8, 308.7]
inlet_name = "inlet"
wall_zone = "rocket"

drag_results = {}


# Set reference values function
def set_reference_values(vel):
    session.tui.report.reference_values.area = 0.01108
    session.tui.report.reference_values.density = 1.225
    session.tui.report.reference_values.length = 3
    session.tui.report.reference_values.pressure = 102539.85
    session.tui.report.reference_values.temperature = 302.594
    session.tui.report.reference_values.viscosity = 1.81e-05
    session.tui.report.reference_values.velocity = vel

# Main loop
for vel in velocities:
    print(f"Running simulation for velocity: {vel} m/s")

    # Set boundary condition
    session.tui.define.boundary_conditions.velocity_inlet(
        inlet_name, "no", "yes", "yes", "no", 0, "yes", "no", str(vel), "no", 0, "no", 0, "no", "no", "yes", "no", 1, 0.05, 10, "no", 0
    )

    set_reference_values(vel)

    # Initialize and run
    session.tui.solve.initialize.set_defaults("x-velocity", str(vel))
    session.tui.solve.initialize.initialize_flow()
    #session.tui.solution.initialization.hybrid_initialize()
    session.tui.solve.set.transient_controls.time_step_size(".5")
    session.tui.solve.set.transient_controls.max_iterations_per_time_step("1")
    session.tui.solve.set.transient_controls.number_of_time_steps("1")

    session.tui.solution.run_calculation.dual_time_iterate()

    # Get drag report
    drag = session.tui.report.forces.wall_forces(
        "no", wall_zone, ",", "1", "0", "0", "yes", "drag_report", "yes"
    )

    drag_results[vel] = drag

     #Save results
    session.tui.file.write_data(
        fr"C:\Users\Public\Documents\test\squared_{vel}.dat"
    )
    session.tui.file.write_case(
        fr"C:\Users\Public\Documents\test\squared_{vel}.cas"
    )



# Print summary
print("\n--- Simulation Drag Results ---")
for vel, drag in drag_results.items():
    print(f"Velocity: {vel} m/s → Drag Force: {drag} N")

# Exit Fluent
session.exit()