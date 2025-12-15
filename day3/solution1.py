def read_input(input_file):
    with open(input_file) as f:
        banks = [line.strip() for line in f]
        return banks


input_file = "day3/input.txt"


def main():
    res = 0
    banks = read_input(input_file)

    for bank in banks:
        first_digit = -1
        first_digit_pos = -1

        for i, c in enumerate(bank[:-1]):
            cur_num = int(c)

            if cur_num > first_digit:
                first_digit = cur_num
                first_digit_pos = i

        second_digit = -1

        for c in bank[first_digit_pos + 1 :]:
            cur_num = int(c)

            if cur_num > second_digit:
                second_digit = cur_num

        bank_output = int(str(first_digit) + str(second_digit))

        res += bank_output
    print(res)
    return res


if __name__ == "__main__":
    main()
