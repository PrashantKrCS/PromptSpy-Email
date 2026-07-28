import time
from datetime import datetime

def banner(title):

    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)


def log(message):

    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")


def wait(seconds):

    time.sleep(seconds)


def separator():

    print("-" * 60)
