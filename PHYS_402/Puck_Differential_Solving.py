#! /usr/bin/env python

# Patrick McMillin, Fernando Ramirez, Jeffrey Valdez
# Extra-Credit Puck on Merry-Go-Round Project
# Physics 402, Dr. Lim, 8 May 2017

# Import libraries to use
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def main():
    '''
    This is the main function, which will run all of the code required to plot the puck's trajectory.
    1) Asks the user for the initial conditions.
    2) Solves the system of coupled, second order ordinary differential equations with the inital conditions from the user. 
    3) Finds the time it takes for the puck to reach the edge of the merry-go-round.
    4) Plots the trajectory of the puck.
    '''
    # Defines the radius of the merry-go-round
    Radius = 1
    # Defines the angular speed of the puck. (radians per second)
    # Note: The angular velocity is ONLY in the z direction, out of the plane of the merry-go-round.
    omega_z = 1 
    # Asks for the initial conditions of the system at time = 0. These are the initial conditions to be used when solving the ODE's.
    velocity_magnitude_initial = input('Please input the initial magnitude of velocity: ')
    velocity_angle_initial = input('Please input the angle that the velocity vector makes with the right horizontal: ')
    x_position_initial = input('Please input the initial x position of the puck relativce to the center of the merry-go-round: ')
    y_position_initial = 0
    # Here we define some values which are needed in solving the differential equation. 
    abserr = 1.0e-8 # Absolute error
    relerr = 1.0e-6 # Relative error
    final_time = 100 # Last value of time to consider
    npoints = 50000 # Number of points (Larger for better results)
    # Time vector
    t = [final_time * float(i) / (npoints - 1) for i in range(npoints)]
    # Collecting initial conditions
    initial_conditions = [x_position_initial, velocity_magnitude_initial * np.cos(np.deg2rad(velocity_angle_initial)), 
                          y_position_initial, velocity_magnitude_initial * np.sin(np.deg2rad(velocity_angle_initial))]
    # Call the differential equation solver.
    solution_list = odeint(equations_of_motion, initial_conditions, t, args=(omega_z,), atol = abserr, rtol = relerr)
    # Gets the time which the puck reaches the edge of the merry-go-round
    index, time = get_time_puck_falls_off(solution_list, Radius, t)
    # Plots the trajectory of the puck
    plotting(solution_list, index, time, velocity_magnitude_initial)

def equations_of_motion(initial_conditions, t, omega_z):
    '''
    Defines the differential equations which we need to solve for the puck on the merry go round.
    '''
    x1, y1, x2, y2 = initial_conditions
    system_of_equations = [y1, ((omega_z) * (omega_z * x1 + 2 * y2)), 
                           y2, ((omega_z) * (omega_z * x2 - 2 * y1))]
    return system_of_equations

def get_time_puck_falls_off(solution_list, Radius, t):
    '''
    This function is designed to get the time at which the puck leaves the merry-go-round.
    We loop through all of the elements of the solution and get the magnitude of the position vector.
    If the magnitude is greater than the radius of the merry-go-round, then the time is found from the index. 
    The index and the time is returned. 
    '''
    i = 0
    while i < 50000:
        if np.sqrt(solution_list[i][0] ** 2 + solution_list[i][2] ** 2) > Radius:
            break
        i += 1
    return i-1, t[i-1]

def plotting(solution_list, index, time, velocity_magnitude_initial):
    '''
    Plots the puck's trajectory on the merry go round.
    Sets the limits of the plot to just greater than the merry-go-round's radius.
    Plots the trajectory, and a circle which represents the merry-go-round.
    Adds text to the plot to display the initial velocity magnitude and the time it took the puck to fall off the merry-go-round.
    '''
    # Resize the list to plot only the positions before the puck falls off the merry-go-round.
    solution_list = solution_list[:index]
    # Clear the plot.
    plt.cla()
    # Set the axis size.
    ax = plt.axes(aspect = 1)
    # Set limits to view to x and y axes.
    ax.set_xlim((-1.1, 1.1))
    ax.set_ylim((-1.1, 1.1))
    # Plot y vs x
    ax.plot(solution_list[:,0], solution_list[:,2])
    ax.add_artist(plt.Circle((0, 0), 1, fill = False))
    # Add the time it took for the puck to fall off the merry-go-round.
    ax.text(0.55, 0.9,"$T$ = " + '{:.4f}'.format(time) + " s" )
    # Add the initial velocity magnitude
    ax.text(0.55, 1.0, "$v_o$ = "  + '{:.2f}'.format(velocity_magnitude_initial) + " m/s")
    plt.show()

main()
