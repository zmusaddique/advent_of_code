def get_data(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]


input_file = "day1/input.txt"
data = get_data(input_file)


def main():
    res = 0
    current_pos = 50

    for instruction in data:
        magnitude = int(instruction[1:])

        for _ in range(
            magnitude
        ):  # Cause we neeed to capture each passing. Couldn't think of a better way
            if instruction[0] == "L":
                current_pos = (current_pos - 1) % 100

            elif instruction[0] == "R":
                current_pos = (current_pos + 1) % 100

            if current_pos == 0:
                res += 1

    print(res)
    return res


if __name__ == "__main__":
    main()
