import matplotlib.pyplot as plt
import os
from abm import PandemicABM

def compare_avoidance(steps=200):
    # No avoidance
    model1 = PandemicABM(move_prob=1.0, avoid_strength=0.0)
    _, I1, _ = model1.run(steps)

    # Strong avoidance
    model2 = PandemicABM(move_prob=1.0, avoid_strength=0.8)
    _, I2, _ = model2.run(steps)

    plt.figure(figsize=(8,5))
    plt.plot(I1, label="No Avoidance")
    plt.plot(I2, label="Avoidance (avoid_strength=0.8)")
    plt.xlabel("Time Steps")
    plt.ylabel("Infected Population")
    plt.title("Effect of Avoidance Behavior on Infection Spread")
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(os.path.dirname(__file__), "..", "figures", "avoidance.png")
    plt.savefig(output_path, dpi=300)
    print(f"Saved to {output_path}")
    plt.show()

if __name__ == "__main__":
    compare_avoidance()
