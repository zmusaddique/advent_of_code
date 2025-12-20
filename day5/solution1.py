def read_input(input_file: str):
    with open(input_file) as f:
        content = f.read()
    sections = content.strip().split("\n\n")

    ranges = [
        tuple(map(int, seq_range.split("-"))) for seq_range in sections[0].split("\n")
    ]
    id_s = [int(id) for id in sections[1].split("\n")]

    return ranges, id_s


input_file = "day5/input.txt"


def main():
    ranges, id_s = read_input(input_file)
    fresh_items = 0

    for id in id_s:
        for start, end in ranges:
            if start <= id <= end:
                fresh_items += 1
                break
    print(fresh_items)


if __name__ == "__main__":
    main()
