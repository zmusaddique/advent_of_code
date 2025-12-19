def read_input(input_file: str):
    with open(input_file) as f:
        data = [list(line.strip()) for line in f.readlines()]
        return data


input_file = "day4/input.txt"


def find_rolls(grid: list[list]):
    optimal_rolls = 0
    optimal_rolls_pos = []

    relative_pos = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
    ]
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@":
                adj_rolls = 0

                for dr, dc in relative_pos:
                    rr = row + dr
                    cc = col + dc

                    if 0 <= rr < rows and 0 <= cc < cols:
                        if grid[rr][cc] == "@":
                            adj_rolls += 1
                            if adj_rolls > 3:
                                break
                if adj_rolls < 4:
                    optimal_rolls += 1
                    optimal_rolls_pos.append((row, col))

    return optimal_rolls, optimal_rolls_pos


def main():
    grid: list = read_input(input_file)
    res = 0
    possible_rolls = 0
    eliminating_rolls = []

    while True:
        possible_rolls, eliminating_rolls = find_rolls(grid)
        if possible_rolls == 0:
            break
        res += possible_rolls

        for r, c in eliminating_rolls:
            grid[r][c] = "."

    print("Possible rolls: ", res)
    return res


if __name__ == "__main__":
    main()
