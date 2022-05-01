import math
import matplotlib.pyplot as plt
import numpy as np
print('SAVITRIBAI PHULE PUNE UNIVERSITY')
print('\n SUBJECT: KINEMATICS OF MACHINERY')
print('\n KINEMATIC ANALYSIS OF SLIDER CRANK MECHANISM')
print('\n STUDENTDETAILS')
n1 = input('ENTER YOURNAME::')
r1 = int(input('ENTER YOUR ROLL NUMBER::'))
print('\n INPUTPARAMETER')
r = float(input('Enter crank radius::'))
n = float(input('Enter Obliquityratio::'))
w = float(input('Angular Velocity(Rad/Sec)::'))
print('\n ----------------------------------------------VELOCITY AND ACCELERATION PLOT--------')
ang = []  # Value of angles store in this list
disp = []  # Value of displacement store in this list
vel = []  # Value of Velocity store in this list
acc = []  # Value of Acceleration store in thislist

for i in range(0, 360):
    ang.append(i)  # Store value of i in "ang"List
    a = math.radians(i)
    d1 = r * (1 - math.cos(a) + math.sin(a) * math.sin(a) / (2 * n))
    displacement = round(d1, 4)
    v1 = w * r * (math.sin(a) + math.sin(2 * a) / (2 * n))
    velocity = round(v1, 4)
    a1 = w ** 2 * r * (math.cos(a) + math.cos(2 * a) / n)
    acclr = round(a1, 4)
    disp.append(displacement)
    vel.append(velocity)
    acc.append(acclr)


ang = np.array(ang)
disp = np.array(disp)
vel = np.array(vel)
acc = np.array(acc)

# Displacement Graph
plt.subplot(3, 1, 1)
plt.plot(ang, disp)
plt.title('Displacement')

# VelocityGraph

print(' ---------')
plt.subplot(3, 1, 2)
plt.plot(ang, vel)
plt.title('Velocity')

# Acceleration Graph
plt.subplot(3, 1, 3)
plt.plot(ang, acc)
plt.title('Acceleration')

plt.show()

print('\n RESULT')
for h in range(0, 360, 45):
    print(
        'for angle ',
        ang[h],
        '= ',
        'dispalcement ',
        disp[h],
        ' velocity',
        vel[h],
        ' Acceleration ',
        acc[h],
    )
