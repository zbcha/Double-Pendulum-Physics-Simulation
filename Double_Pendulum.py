import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

G = 9.81
FPS = 60

class Double_Pendulum:
    def __init__(self, L1, L2, m1, m2):
        self.m1 = m1 # Mass of pendulum 1
        self.m2 = m2 # Mass of pendulum 2
        self.L1 = L1 # Length of arm 1
        self.L2 = L2 # Length of arm 2

    def solve(self, t, ini_ar):
        # Pendulum initial degree of mass 1
        # Pendulum initial degree of mass 2
        # Pendulum initial velocity of mass 1
        # Pendulum initial velocity of mass 2
        theta1, theta2, omega1, omega2 = ini_ar

        # Define derivatives
        dydt = [
            omega1,
            omega2,
            (-G * (2 * self.m1 + self.m2) * np.sin(theta1) - self.m2 * G * np.sin(theta1 - 2 * theta2) -
             2 * np.sin(theta1 - theta2) * self.m2 * (omega2 ** 2 * self.L2 + omega1 ** 2 * self.L1 * np.cos(theta1 - theta2))) /
            (self.L1 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * theta1 - 2 * theta2))),
            (2 * np.sin(theta1 - theta2) * (omega1 ** 2 * self.L1 * (self.m1 + self.m2) + G * (self.m1 + self.m2) *
            np.cos(theta1) + omega2 ** 2 * self.L2 * self.m2 * np.cos(theta1 - theta2))) /
            (self.L2 * (2 * self.m1 + self.m2 - self.m2 * np.cos(2 * theta1 - 2 * theta2)))
        ]
        return dydt

    def update(self, y0, t_span):
        # Solve the ODE
        frame = (t_span[1] - t_span[0]) * FPS
        sol = solve_ivp(self.solve, t_span, y0, method='RK45', t_eval=np.linspace(t_span[0], t_span[1], frame))

        # Extract solutions
        theta1 = sol.y[0]
        theta2 = sol.y[1]

        # Calculate the positions of the pendulum masses
        x1 = self.L1 * np.sin(theta1)
        y1 = -self.L1 * np.cos(theta1)
        x2 = x1 + self.L2 * np.sin(theta2)
        y2 = y1 - self.L2 * np.cos(theta2)

        return x1, y1, x2, y2

    def temp_plot(self, x1, y1, x2, y2):
        plt.figure(figsize=(8, 6))
        plt.plot(x1, y1, label='Pendulum 1')
        plt.plot(x2, y2, label='Pendulum 2')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Motion of Double Pendulum')
        plt.legend()
        plt.grid(True)
        plt.axis('equal')
        plt.show()
