from datetime import datetime

from config import ENABLE_LOGGING
from config import LOG_TIME_FORMAT


def log(message: str):

    if ENABLE_LOGGING:
        print(
            f"[{datetime.now().strftime(LOG_TIME_FORMAT)}] {message}"
        )


def divider(title):

    print("\n" + "=" * 65)
    print(title.center(65))
    print("=" * 65)
