import argparse
from datetime import datetime


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Print a timestamped greeting.")
    parser.add_argument(
        "--name",
        default="Codex",
        help="Name to include in the greeting (default: Codex).",
    )
    parser.add_argument(
        "--format",
        choices=("12h", "24h"),
        default="24h",
        help="Time format to use: 12h or 24h (default: 24h).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    timestamp_format = "%Y-%m-%d %I:%M:%S %p" if args.format == "12h" else "%Y-%m-%d %H:%M:%S"
    print(f"Hello from {args.name} - {datetime.now().strftime(timestamp_format)}")


if __name__ == "__main__":
    main()
