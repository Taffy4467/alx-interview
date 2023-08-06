#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics.
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
Return status codes in ascending order
"""

import sys
from collections import defaultdict
from typing import Dict, Tuple

def print_stats(total_size: int, status_counts: Dict[int, int]) -> None:
    """
    Print the computed statistics.
    """
    print("File size:", total_size)
    for status_code, count in sorted(status_counts.items()):
        print(f"{status_code}: {count}")

def parse_line(line: str) -> Tuple[int, int]:
    """
    Parse the line and extract file size and status code.
    """
    parts = line.strip().split()
    if len(parts) < 8 or parts[-4] != "GET" or not parts[-2].isdigit():
        return None, None

    status_code = int(parts[-2])
    file_size = int(parts[-1])
    return status_code, file_size

def main() -> None:
    """
    Main function to compute metrics.
    """
    total_size = 0
    status_counts = defaultdict(int)

    try:
        for line_counter, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is not None and file_size is not None:
                total_size += file_size
                status_counts[status_code] += 1

            if line_counter % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        # Print final statistics before terminating on KeyboardInterrupt
        print_stats(total_size, status_counts)
        sys.exit(0)

    # Print final statistics if the loop ends without KeyboardInterrupt
    print_stats(total_size, status_counts)

if __name__ == "__main__":
    main()
