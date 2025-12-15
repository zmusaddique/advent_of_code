def read_input(input_file):
    with open(input_file) as f:
        data = f.readline()
        ranges = data.split(",")
        return ranges


input_file = "day2/input1.txt"


def is_invalid(num: str):
    n = len(num)
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            seq = num[:i]
            if seq * (n // i) == num:
                return True

    return False


def main():
    res = 0

    ranges = read_input(input_file)
    for seq_range in ranges:
        start, end = [int(x) for x in seq_range.split("-")]
        for i in range(start, end + 1):
            i_str = str(i)

            if is_invalid(i_str):
                res += int(i_str)
    print(res)
    return res


if __name__ == "__main__":
    main()
