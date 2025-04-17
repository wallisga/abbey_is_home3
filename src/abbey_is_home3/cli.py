"""Command line interface for abbey_is_home3."""

import argparse
import sys

from abbey_is_home3 import __version__


def parse_args(args=None):
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="AG")
    parser.add_argument(
        "--version", action="store_true", help="Show version and exit"
    )
    
    return parser.parse_args(args)


def main(args=None):
    """Run the main program."""
    args = parse_args(args)
    
    if args.version:
        print(f"abbey_is_home3 v{__version__}")
        return 0
    
    # Add your code here
    print("Hello from abbey_is_home3!")
    print(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
