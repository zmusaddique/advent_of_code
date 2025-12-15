def read_input(input_file):
    with open(input_file) as f:
        banks = [line.strip() for line in f]
        return banks


input_file = "day3/input.txt"


def main():
    banks = read_input(input_file)
    res: int = 0

    for bank in banks:
        window_size = 12
        to_remove = len(bank) - window_size

        bank_jolt = []

        for jolt in bank:
            while bank_jolt and to_remove > 0 and bank_jolt[-1] < jolt:
                bank_jolt.pop()
                to_remove -= 1
            bank_jolt.append(jolt)

        bank_jolt = "".join(bank_jolt[:window_size])
        res += int(bank_jolt)

    print(res)
    return res


if __name__ == "__main__":
    main()
