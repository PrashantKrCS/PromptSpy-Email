from pipeline import SimulationPipeline

from utils import divider


def start_console():

    results = SimulationPipeline(
        secure_mode=True
    ).execute()

    divider("Simulation Complete")

    print(results["email"].render())

    print()

    print("Summary:")
    print(results["assistant"]["summary"])

    print()

    print("Trust Boundary:")
    print(results["trust"]["decision"])

    print()

    print("Reply:")

    print(results["reply"])


if __name__ == "__main__":

    start_console()
