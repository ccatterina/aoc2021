import pathlib
import sys

import numpy as np


def get_consumption(report):
    transposed_report = np.array([list(line) for line in report]).astype(int).T

    most_common_bits = ["1" if np.count_nonzero(r) > len(r) / 2 else "0" for r in transposed_report]
    gamma = int("".join(most_common_bits), 2)

    least_common_bits = ["1" if b == "0" else "0" for b in most_common_bits]
    epsilon = int("".join(least_common_bits), 2)

    return gamma * epsilon


if __name__ == "__main__":
    for path in sys.argv[1:]:
        report = pathlib.Path(path).read_text().strip().split()
        print(f"Consumption: {get_consumption(report)}")
