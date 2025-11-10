# p: infection rate
# q: recovery rate
import matplotlib.pyplot as plt
import os
from abm import PandemicABM

def run_sir(p, q, steps=200):
    model = PandemicABM(p_infection=p, p_recovery=q)
    S, I, R = model.run(steps)
    return S, I, R

def sensitivity_run():
    scenarios = [
        (0.05, 0.02),
        (0.05, 0.05),
        (0.10, 0.02),
        (0.10, 0.05),  # baseline
    ]

    plt.figure(figsize=(10, 6))

    for p, q in scenarios:
        S, I, R = run_sir(p, q)
        plt.plot(I, label=f"I (p={p}, q={q})")

    plt.title("Sensitivity Analysis: Infection Curves for Different p and q")
    plt.xlabel("Time Steps")
    plt.ylabel("Number of Infected Agents")
    plt.legend()
    plt.grid(True)

    # Save file safely
    output_path = os.path.join(os.path.dirname(__file__), "..", "figures", "sensitivity_pq.png")
    plt.savefig(output_path, dpi=300)
    print(f"Saved plot to {output_path}")
    plt.show()

if __name__ == "__main__":
    sensitivity_run()
