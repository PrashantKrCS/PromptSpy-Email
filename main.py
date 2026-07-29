import argparse

from pipeline import SimulationPipeline
from web.app import create_app

from config import HOST
from config import PORT
from config import DEBUG

from utils import divider


def console():

    results = SimulationPipeline().execute()

    divider("Simulation Complete")

    print(results["email"].render())

    print()

    print(results["assistant"]["summary"])

    print()

    print(results["trust"]["decision"])

    print()

    print(results["reply"])


def web():

    app = create_app()

    app.run(
        host=HOST,
        port=PORT,
        debug=DEBUG
    )


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--web",
        action="store_true"
    )

    args = parser.parse_args()

    if args.web:

        web()

    else:

        console()
