import logging
import sys
from datetime import datetime


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> int:
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        logger.info("Generated current timestamp")
        print(f"Hello from Codex - {now}")
        return 0
    except Exception:
        logger.exception("Unexpected error while generating greeting")
        return 1


if __name__ == "__main__":
    sys.exit(main())
