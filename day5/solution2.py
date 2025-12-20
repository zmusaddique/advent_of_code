def read_input(input_file):
    with open(input_file) as f:
        content = f.read()
    content = content.strip().split("\n\n")

    ranges = [
        tuple(map(int, seq_range.split("-"))) for seq_range in content[0].split("\n")
    ]
    return ranges


input_file = "day5/input.txt"


def main():
    ranges = read_input(input_file)
    ranges.sort()
    res_ranges = [ranges[0]]
    res = 0

    for i in range(1, len(ranges)):
        if ranges[i][0] <= res_ranges[-1][1]:
            merged_range = (res_ranges[-1][0], max(res_ranges[-1][1], ranges[i][1]))
            res_ranges[-1] = merged_range
        else:
            res_ranges.append(ranges[i])

    for start, end in res_ranges:
        res += end - start + 1
    print(res)


if __name__ == "__main__":
    main()
