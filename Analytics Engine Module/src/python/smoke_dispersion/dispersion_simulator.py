import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class SmokeDispersionSimulator:
    def __init__(self, initial_concentration, wind_speed, diffusion_coefficient):
        """
        Initializes the SmokeDispersionSimulator with initial parameters.

        :param initial_concentration: Initial smoke concentration (e.g., at the fire source)
        :param wind_speed: Wind speed affecting smoke dispersion
        :param diffusion_coefficient: Coefficient for smoke diffusion
        """
        self.initial_concentration = initial_concentration
        self.wind_speed = wind_speed
        self.diffusion_coefficient = diffusion_coefficient

    def _dispersion_model(self, concentration, t):
        """
        Defines the differential equation for the dispersion model.

        :param concentration: Current concentration of smoke
        :param t: Time
        :return: Derivative of concentration with respect to time
        """
        dCdt = -self.wind_speed * concentration + self.diffusion_coefficient * concentration
        return dCdt

    def simulate_dispersion(self, time_points):
        """
        Simulates the dispersion of smoke over time.

        :param time_points: Array of time points for simulation
        :return: Array of smoke concentrations over time
        """
        concentrations = odeint(self._dispersion_model, self.initial_concentration, time_points)
        return concentrations

    def plot_dispersion(self, time_points, concentrations):
        """
        Plots the smoke dispersion over time.

        :param time_points: Array of time points
        :param concentrations: Array of smoke concentrations over time
        """
        plt.figure(figsize=(10, 6))
        plt.plot(time_points, concentrations, label='Smoke Concentration')
        plt.xlabel('Time')
        plt.ylabel('Concentration')
        plt.title('Smoke Dispersion Over Time')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Initialize simulator with example parameters
    initial_concentration = 100  # Initial concentration at the fire source
    wind_speed = 0.1  # Wind speed affecting dispersion
    diffusion_coefficient = 0.01  # Diffusion coefficient

    simulator = SmokeDispersionSimulator(initial_concentration, wind_speed, diffusion_coefficient)
    
    # Define time points for the simulation
    time_points = np.linspace(0, 50, 100)  # Simulate for 50 time units

    # Simulate smoke dispersion
    concentrations = simulator.simulate_dispersion(time_points)
    
    # Plot results
    simulator.plot_dispersion(time_points, concentrations)
