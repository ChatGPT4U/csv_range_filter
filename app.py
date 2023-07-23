import csv
import argparse


def calculate_keep_ranges(n):
    """Calculate line ranges to keep based on a given number."""
    keep_ranges = [(1, 2), (2, n+2), (502, 502+n),
                   (1002, 1002+n), (1502, 1502+n)]
    return keep_ranges


def should_keep_line(line_number, keep_ranges):
    """Check if line number is in any of the keep ranges."""
    for start, end in keep_ranges:
        if start <= line_number < end:
            return True
    return False


def process_csv(input_file_path, output_file_path, n):
    keep_ranges = calculate_keep_ranges(n)

    with open(input_file_path, 'r') as input_file, open(output_file_path, 'w', newline='') as output_file:
        reader = csv.reader(input_file)
        writer = csv.writer(output_file)

        # start=1 to make line numbers 1-indexed
        for i, row in enumerate(reader, start=1):
            if should_keep_line(i, keep_ranges):
                writer.writerow(row)


def main():
    # Define argument parser
    parser = argparse.ArgumentParser(
        description='Keep specified line ranges from a CSV file.')
    parser.add_argument('input_file_path', help='Path to the input CSV file.')
    parser.add_argument('output_file_path',
                        help='Path to the output CSV file.')
    parser.add_argument(
        'n', type=int, help='Number to calculate line ranges to keep.')

    # Parse arguments
    args = parser.parse_args()

    # Run main function
    process_csv(args.input_file_path, args.output_file_path, args.n)


if __name__ == '__main__':
    main()
