def get_data(input_file):
    with open(input_file) as file:
        content = file.readline()
        ranges = content.split(",")
        return ranges


input_file = "day2/input1.txt"


def main():
    res = 0
    ranges = get_data(input_file)
    for seq_range in ranges:
        start, end = [int(x) for x in seq_range.split("-")]

        for i in range(start, end):
            i_str = str(i)
            i_len_half = len(i_str) // 2

            if i_str[:i_len_half] == i_str[i_len_half:]:
                res += int(i_str)
    print(res)
    return res


if __name__ == "__main__":
    main()
