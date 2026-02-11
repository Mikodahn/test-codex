import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Greet someone with timestamp')
parser.add_argument('name', nargs='?', default='World', help='Name to greet')
args = parser.parse_args()

print(f"Hello, {args.name}! - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
