from riscy_mk2 import RISCy


def main(raw_input):
    riscy = RISCy()
    data = [int(x) for x in parse_input(raw_input)]
    riscy.set_memory(data)
    riscy.set_input_queue([1])

    riscy.run()
    return riscy.get_io_log()[-1]


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
