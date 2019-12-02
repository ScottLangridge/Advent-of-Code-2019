from riscy import RISCy


def main(raw_input):
    riscy = RISCy()
    data = [int(x) for x in parse_input(raw_input)]

    for noun in range(100):
        for verb in range(100):
            riscy.set_memory(data[:])
            riscy.set_noun_verb(noun, verb)
            if riscy.run() == 19690720:
                return (100 * noun) + verb


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('../input.txt')
    print(main(puzzle_input))
