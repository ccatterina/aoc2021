import pathlib
import sys

import numpy as np


def consumption(report):
    transposed_report = np.array([list(line) for line in report]).astype(int).T

    most_common_bits = ["1" if np.count_nonzero(r) > len(r) / 2 else "0" for r in transposed_report]
    gamma = int("".join(most_common_bits), 2)

    least_common_bits = ["1" if b == "0" else "0" for b in most_common_bits]
    epsilon = int("".join(least_common_bits), 2)

    return gamma * epsilon


def calculate_rating(report, bit_criteria):
    report = np.array([list(line) for line in report])
    for i in range(len(report.T)):
        report = np.array([row for row in report if row[i] == bit_criteria(report.T[i])])
        if len(report) != 1:
            continue

        return int("".join(report[0]), 2)


def oxygen_generator_rating(report):
    bit_criteria = lambda c: "1" if np.count_nonzero(c == "1") >= len(c) / 2 else "0"
    return calculate_rating(report, bit_criteria)


def co2_scrubber_rating(report):
    bit_criteria = lambda c: "1" if np.count_nonzero(c == "1") < len(c) / 2 else "0"
    return calculate_rating(report, bit_criteria)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py path/to/input/file")
        exit(1)

    path = sys.argv[1]
    report = pathlib.Path(path).read_text().strip().split()
    print(f"Consumption: {consumption(report)}")
    print(f"Life support rating: {oxygen_generator_rating(report) * co2_scrubber_rating(report)}")
