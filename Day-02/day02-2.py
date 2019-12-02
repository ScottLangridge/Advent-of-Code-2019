def main(raw_input):
    data = [int(x) for x in parse_input(raw_input)]

    for noun in range(100):
        for verb in range(100):
            if run_machine(data[:], noun, verb) == 19690720:
                return (100 * noun) + verb
    

def run_machine(data, noun, verb):
    data[1] = noun
    data[2] = verb

    # print('\n\n', data)

    pos = 0
    operand = data[0]

    while operand != 99:
        operand = data[pos]
        param1_addr = data[pos + 1]
        param2_addr = data[pos + 2]
        param1_val = data[param1_addr]
        param2_val = data[param2_addr]
        out_addr = data[pos + 3]

        # print('PC:', pos)
        # print('Operand:', data[pos])
        # print('Param Addrs:', data[pos + 1], data[pos + 2])
        # print('Param Vals:', data[data[pos + 1]], data[data[pos + 2]])
        # print('Dest:', data[pos + 3])
        # print()

        if operand == 1:
            data[out_addr] = param1_val + param2_val
        elif operand == 2:
            data[out_addr] = param1_val * param2_val
        else:
            pass

        pos += 4

    return data[0]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
