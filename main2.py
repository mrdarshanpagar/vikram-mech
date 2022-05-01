
# Program : KINEMATIC ANALYSIS OF HOOKE'S JOINT

import matplotlib.pyplot as plt  # import Library to plot PolarDiagram
import math  # import MathLibrary
print('SAVITRIBAI PHULE PUNE UNIVERSITY')
print('\n SUBJECT: KINEMATICS OF MACHINERY')
print("\n KINEMATIC ANALYSIS OF HOOKE'S JOINT")
print('\n----------------------------------------------STUDENTDETAILS ---------------------------------')
n1 = input('ENTER YOUR NAME::')
r1 = int(input('ENTER YOUR ROLL NUMBER::'))
print('\n INPUTPARAMETERS ')
w1 = float(input('Velocity of input shaft(RPM)::'))
alpha = float(input('shaft angle IN DEGREE::'))
alpha = math.radians(alpha)  # Convert angle into radian
ang = []  # Empty Cell to store angle values
velocity = []  # Empty Cell to store velocityValues
print('\n POLARDIGRAM ')
for i in range(0, 361):  # plot the velocity of output shaft for angle ranging 0 to 360 with 1 degreeinteval
    ang.append(i)  # Value of i will be stored in Empty ang=[] cell
    ang_r = math.radians(i)  # value oftheta
    w2 = w1 * math.cos(alpha) / (1 - math.cos(ang_r) ** 2
                                 * math.sin(alpha) ** 2)  # formula of velocity ratio for hooks joint
    w2 = round(w2, 4)  # Round of velocity value upto precision points.
    # Value of velocity will be stored in empty Ang_velocity=[]cell
    velocity.append(w2)
plt.axes(projection='polar')  # draw polar plot
for i in range(0, 361):  # plot the velocity of output shaft for angle ranging 0 to 360 with 1 degree inteval
    # plot polar diagram of input shaft
    plt.polar(math.radians(ang[i]), w1, 'r.')
    # plot polar diagram of output shaft
    plt.polar(math.radians(ang[i]), velocity[i], 'g.')
plt.title('POLARDIAGRAM')  # Title of Diagram
plt.legend(labels=('Input speed', 'Output speed'), loc=1)  # Addlegend
plt.show()  # plotdiagram
print('\n ')
print('MAXIMUM VELOCITY: ', velocity[0])  # print Maximum velocity
print('MINIMUM VELOCITY: ', velocity[90])  # print Minimumvelocity
for h in range(0, 361, 60):  # print vslus of output speed at an interval of 60 degree
    print(
        'for angle ',
        ang[h],
        '= ',
        'Angular velocity of output shaft',
        velocity[h],
        'RPM',
    )
