import matplotlib.pyplot as plt
import os
from abm import PandemicABM

def compare_distancing(steps=200):
    # No distancing (move_prob=1)
    model1 = PandemicABM(move_prob=1.0)
    S1, I1, R1 = model1.run(steps)

    # With social distancing (move_prob=0.3 → 70% reduced movement)
    model2 = PandemicABM(move_prob=0.3)
    S2, I2, R2 = model2.run(steps)

    plt.figure(figsize=(8,5))
    plt.plot(I1, label="No Distancing (move_prob=1.0)")
    plt.plot(I2, label="Social Distancing (move_prob=0.3)")
    plt.xlabel("Time Steps")
    plt.ylabel("Infected Population")
    plt.title("Effect of Social Distancing on Infection Spread")
    plt.legend()
    plt.grid(True)

    output_path = os.path.join(os.path.dirname(__file__), "..", "figures", "social_distancing.png")
    plt.savefig(output_path, dpi=300)
    print(f"Saved to {output_path}")
    plt.show()

if __name__ == "__main__":
    compare_distancing()
