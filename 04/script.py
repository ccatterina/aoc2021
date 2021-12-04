import pathlib
import sys


def missing_sum(board, drawn):
    return sum([int(num) for row in board for num in row if num not in drawn])


def winning(board, drawn):
    return any([set(row).issubset(drawn) for row in board]) or any(
        [set(col).issubset(drawn) for col in zip(*board)]
    )


def winner_score(drawn_numbers, boards):
    for drawn_count in range(len(drawn_numbers)):
        drawn = drawn_numbers[: drawn_count + 1]
        winner = next((board for board in boards if winning(board, drawn)), None)
        if not winner:
            continue

        return int(drawn[-1]) * missing_sum(winner, drawn)


def last_winner_score(drawn_numbers, boards):
    for drawn_count in range(len(drawn_numbers)):
        drawn = drawn_numbers[: -(drawn_count + 1)]
        looser = next((board for board in boards if not winning(board, drawn)), None)
        if not looser:
            continue

        drawn = drawn_numbers[:-drawn_count]
        return int(drawn[-1]) * missing_sum(looser, drawn)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py path/to/input/file")
        exit(1)

    input = pathlib.Path(sys.argv[1]).read_text().splitlines()
    drawn_numbers = input[0].split(",")
    input = [line.split() for line in input[1:]]
    boards = [input[i : i + 5] for i in range(1, len(input), 6)]
    print(f"Winner score: {winner_score(drawn_numbers, boards)}")
    print(f"Last winner score: {last_winner_score(drawn_numbers, boards)}")
