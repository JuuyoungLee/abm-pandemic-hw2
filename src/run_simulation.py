import matplotlib.pyplot as plt
from abm import PandemicABM
import os

def run_and_plot(steps=200):
    # Create model instance
    model = PandemicABM()

    # Run the model
    S, I, R = model.run(steps)

    # Plot the results
    plt.figure(figsize=(8, 5))
    plt.plot(S, label="Susceptible (S)")
    plt.plot(I, label="Infected (I)")
    plt.plot(R, label="Recovered (R)")
    plt.title("Pandemic Spread Simulation (SIR Model)")
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Agents")
    plt.legend()
    plt.grid(True)

    # Save into figures folder
    output_path = os.path.join(os.path.dirname(__file__), "..", "figures", "base_simulation.png")
    plt.savefig(output_path, dpi=300)
    plt.show()

if __name__ == "__main__":
    run_and_plot()
