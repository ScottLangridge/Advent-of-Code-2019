from itertools import permutations

from riscy_mk2 import RISCy


def main(raw_input):
    data = [int(x) for x in parse_input(raw_input)]

    possible_phase_settings = permutations([0, 1, 2, 3, 4])

    outputs = {}
    for config in possible_phase_settings:
        amp_input = 0
        for phase in config:
            amp = RISCy()
            amp.set_memory(data)
            amp.set_input_queue([phase, amp_input])
            amp.run()
            amp_input = amp.get_io_log()[-1]
        outputs[config] = int(amp_input)

    return max(outputs.values())


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
