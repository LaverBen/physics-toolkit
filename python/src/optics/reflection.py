import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import argparse

from src.maths.standard import angles

PLOT_SCALE = 12
HORIZONTAL_INTERFACE_HEIGHT = 2

def reflect(angle_of_incidence, degrees=False, plot=False):
    # Check arguments
    if degrees:
        if angle_of_incidence >= 90:
            print(f'Invalid input angle of {angle_of_incidence} (must be less than 90)')
            return
    else:
        if angle_of_incidence >= np.pi/2:
            print(f'Invalid input angle of {angle_of_incidence} (must be less than \u03C0/2)')
            return

    angle_of_reflection = angle_of_incidence

    if plot:
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.axhline(y=HORIZONTAL_INTERFACE_HEIGHT, color='k') # Interface line
        ax.axvline(x=0, color='k') # Interface normal line
        if degrees:
            ax.arrow(-1*(PLOT_SCALE*np.sin(angles.degrees_to_radians(angle_of_incidence))), HORIZONTAL_INTERFACE_HEIGHT + PLOT_SCALE*np.cos(angles.degrees_to_radians(angle_of_incidence)), (PLOT_SCALE*np.sin(angles.degrees_to_radians(angle_of_incidence))), -PLOT_SCALE*np.cos(angles.degrees_to_radians(angle_of_incidence)), width=0, head_width=0.1, length_includes_head=True, fill=False, shape='full', color='b')
            ax.arrow(0, HORIZONTAL_INTERFACE_HEIGHT, PLOT_SCALE*np.sin(angles.degrees_to_radians(angle_of_incidence)), PLOT_SCALE*np.cos(angles.degrees_to_radians(angle_of_incidence)), width=0, head_width=0.1, length_includes_head=True, fill=False, shape='full', color='g')
        else:
            ax.arrow(-1*(PLOT_SCALE*np.sin(angle_of_incidence)), HORIZONTAL_INTERFACE_HEIGHT + PLOT_SCALE*np.cos(angle_of_incidence), (PLOT_SCALE*np.sin(angle_of_incidence)), -1*PLOT_SCALE*np.cos(angle_of_incidence), width=0, head_width=0.1, length_includes_head=True, fill=False, shape='full', color='b')
            ax.arrow(0, HORIZONTAL_INTERFACE_HEIGHT, PLOT_SCALE*np.sin(angle_of_incidence), PLOT_SCALE*np.cos(angle_of_incidence), width=0, head_width=0.1, length_includes_head=True, fill=False, shape='full', color='g')
        if degrees:
            ax.add_patch(patches.Arc((0,HORIZONTAL_INTERFACE_HEIGHT), PLOT_SCALE/4, PLOT_SCALE/4, angle=0, theta1=90, theta2=90 + angle_of_incidence, color='k'))
            ax.add_patch(patches.Arc((0,HORIZONTAL_INTERFACE_HEIGHT), PLOT_SCALE/4, PLOT_SCALE/4, angle=0, theta1=90 - angle_of_incidence, theta2=90, color='k'))
        else:
            ax.add_patch(patches.Arc((0,HORIZONTAL_INTERFACE_HEIGHT), PLOT_SCALE/4, PLOT_SCALE/4, angle=0, theta1=90, theta2=90 + angles.radians_to_degrees(angle_of_incidence), color='k'))
            ax.add_patch(patches.Arc((0,HORIZONTAL_INTERFACE_HEIGHT), PLOT_SCALE/4, PLOT_SCALE/4, angle=0, theta1=90 - angles.radians_to_degrees(angle_of_incidence), theta2=90, color='k'))
        ax.text(-1*(PLOT_SCALE/10), HORIZONTAL_INTERFACE_HEIGHT + (PLOT_SCALE/10), f'Incident \u03B8 = {angle_of_incidence:.3f}', ha='right', va='center')
        ax.text(PLOT_SCALE/10, HORIZONTAL_INTERFACE_HEIGHT + (PLOT_SCALE/10), f'Reflected \u03B8 = {angle_of_reflection:.3f}', ha='left', va='center')
        ax.set_xlim(-1*PLOT_SCALE, PLOT_SCALE)
        ax.set_ylim(HORIZONTAL_INTERFACE_HEIGHT - PLOT_SCALE*(1/4), HORIZONTAL_INTERFACE_HEIGHT + PLOT_SCALE)
        ax.fill_between(range(-1*PLOT_SCALE, PLOT_SCALE+1), 0, HORIZONTAL_INTERFACE_HEIGHT, alpha=0.5)
        plt.show()

if __name__=='__main__':
    parser = argparse.ArgumentParser(prog='Reflection', description='Calculates the law of reflection at an interface')
    parser.add_argument('angle', type=float)
    parser.add_argument('--degrees', action='store_true')
    parser.add_argument('--plot', action='store_true')
    args = parser.parse_args()

    reflect(args.angle, args.degrees, args.plot)