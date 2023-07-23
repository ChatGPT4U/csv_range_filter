# CSV Range Filter

This Python script allows you to filter a CSV file based on specified line ranges. It is particularly useful when you want to keep only certain parts of a large CSV file.

## Requirements

- Python 3.6 or higher

## Usage

The script is run from the command line with three arguments:

1. `input_file_path`: The path to the input CSV file.
2. `output_file_path`: The path to the output CSV file.
3. `n`: A number used to calculate the line ranges to keep.

The script will keep the header and the first `n` records of each model in the output CSV file. The models are assumed to be located at lines 2 to `n+1`, 502 to `501+n`, 1002 to `1001+n`, and 1502 to `1501+n` in the input CSV file.

Here is an example of how to run the script:

```bash
python app.py .\in\PRIME_EVAL.csv .\out\PRIME_EVAL_10.csv 10
```

In this example, the script will read `PRIME_EVAL.csv`, keep the specified line ranges, and write the result to `PRIME_EVAL_10.csv`.

## Code Overview

The script mainly consists of four functions:

- `calculate_keep_ranges(n)`: Calculates the line ranges to keep based on the given number `n`.
- `should_keep_line(line_number, keep_ranges)`: Checks if a line number is in any of the keep ranges.
- `process_csv(input_file_path, output_file_path, n)`: Reads the input CSV file, keeps the lines in the keep ranges, and writes the result to the output CSV file.
- `main()`: Parses the command line arguments and runs the `process_csv` function.

## Acknowledgements

- GPT-4 (Poe)
