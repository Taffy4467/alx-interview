#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''
import sys

def print_stats(total_file_size, status_code_count):
    print("File size: {}".format(total_file_size))
    for status_code in sorted(status_code_count.keys()):
        count = status_code_count[status_code]
        print("{}: {}".format(status_code, count))

def parse_log_line(line):
    parts = line.strip().split(" ")
    if len(parts) != 9:
        return None

    ip, _, _, timestamp, _, request, status_code, file_size, _ = parts
    if request != '"GET /projects/260 HTTP/1.1"':
        return None

    try:
        status_code = int(status_code)
        file_size = int(file_size)
        return status_code, file_size
    except ValueError:
        return None

def main():
    total_file_size = 0
    status_code_count = {}

    try:
        line_count = 0
        for line in sys.stdin:
            log_entry = parse_log_line(line)
            if log_entry:
                status_code, file_size = log_entry
                total_file_size += file_size
                status_code_count[status_code] = status_code_count.get(status_code, 0) + 1

            line_count += 1
            if line_count == 10:
                print_stats(total_file_size, status_code_count)
                line_count = 0

    except KeyboardInterrupt:
        print_stats(total_file_size, status_code_count)

if __name__ == "__main__":
    main()

