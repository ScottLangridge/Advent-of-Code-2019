from itertools import permutations

from riscy_mk3 import RISCy


def main(raw_input):
    data = [int(x) for x in parse_input(raw_input)]
    possible_phase_settings = permutations([5, 6, 7, 8, 9])

    outputs = {}
    for config in possible_phase_settings:
        # Configure amps
        amps = []
        for i in range(5):
            new_amp = RISCy(pause_on_output=True)
            new_amp.set_memory(data)
            new_amp.queue_input(config[i])
            amps.append(new_amp)

        # Run
        current_amp = 0
        next_input = 0
        while not all_halted(amps):
            amps[current_amp].queue_input(next_input)
            amps[current_amp].run()
            amps[current_amp].reset_pause_flag()
            next_input = amps[current_amp].get_io_log()[-1]
            current_amp = (current_amp + 1) % 5

        outputs[config] = int(next_input)

    return max(outputs.values())


def all_halted(amps):
    for amp in amps:
        if not amp.halted():
            return False
    return True


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    return raw_input.split(',')


if __name__ == '__main__':
    puzzle_input = get_input('input.txt')
    print(main(puzzle_input))
