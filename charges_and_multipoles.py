import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Q1_magn = 1
Q2_magn = -1

q1 = np.array([0, 0, 0.01])
q2 = np.array([0, 0, -0.01])
x = np.arange(-5, 5.2, 1.5)
y = np.arange(-5, 5.2, 1.5)
z = np.arange(-5, 5.2, 1.5)

X, Y, Z = np.meshgrid(x, y, z)

def electric_field_charge(Q, charge_pos, X, Y, Z):
    Rx = X - charge_pos[0]
    Ry = Y - charge_pos[1]
    Rz = Z - charge_pos[2]

    r = np.sqrt(Rx**2 + Ry**2 + Rz**2)
    r[r == 0] = 1e-9

    Ex = Q * Rx / r**3
    Ey = Q * Ry / r**3
    Ez = Q * Rz / r**3
    
    return Ex, Ey, Ez

def potential_charge(Q, charge_pos, X, Y, Z):
    Rx = X - charge_pos[0]
    Ry = Y - charge_pos[1]
    Rz = Z - charge_pos[2]

    r = np.sqrt(Rx**2 + Ry**2 + Rz**2)
    r[r == 0] = 1e-9

    U = Q / r
    return U

Ex_mq, Ey_mq, Ez_mq = electric_field_charge(Q1_magn, q1, X, Y, Z)
Ex_pq, Ey_pq, Ez_pq = electric_field_charge(Q2_magn, q2, X, Y, Z)

Ex = Ex_mq + Ex_pq
Ey = Ey_mq + Ey_pq
Ez = Ez_mq + Ez_pq

E_magnitude = np.sqrt(Ex**2 + Ey**2 + Ez**2)
Ex = Ex / E_magnitude
Ey = Ey / E_magnitude
Ez = Ez / E_magnitude

figE = plt.figure(figsize=(10, 7))
ax = figE.add_subplot(111, projection='3d')

ax.quiver(X, Y, Z, Ex, Ey, Ez, length=1, normalize=True, color='000000')

ax.scatter(*q1, color='#00FF00', s=10, label='Q = 1')
ax.scatter(*q2, color='#0000FF', s=10, label='Q = -1')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()

x = np.linspace(-5, 5, 100)
z = np.linspace(-5, 5, 100)
X, Z = np.meshgrid(x, z)

def potential_charge(Q, charge_pos, X, Z):
    Rx = X - charge_pos[0]
    Rz = Z - charge_pos[2]
    r = np.sqrt(Rx**2 + Rz**2)
    r[r == 0] = 1e-9
    return Q / r

U1 = potential_charge(Q1_magn, q1, X, Z)
U2 = potential_charge(Q2_magn, q2, X, Z)
U_total = U1 + U2

plt.figure(figsize=(8, 6))
contour = plt.contour(X, Z, U_total, levels=100)  

plt.scatter(q1[0], q1[2], color='green', s=100, label="Q = +1")
plt.scatter(q2[0], q2[2], color='blue', s=100, label="Q = -1")

plt.xlabel("X-axis")
plt.ylabel("Z-axis")
plt.title("Equipotential Lines of Dipole (XZ Plane)")
plt.legend()
plt.grid()
plt.show()
