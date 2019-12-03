def main(raw_input):
    data = parse_input(raw_input)
    for wire in data:
        gen_wiremap(wire)

    # Return solution
    return None


def get_input(filename):
    with open(filename) as f:
        raw_input = f.read()
    return raw_input


def parse_input(raw_input):
    wires = raw_input.split('\n')
    return [wires[0].split(','), wires[1].split(',')]


def gen_wiremap(wire):
    x = 0
    y = 0
    wiremap = []
    for input_line in wire:
        line = {}
        if input_line[0] == 'R':
            line['direction'] = 'x'
            line['constant'] = y
            line['start'] = x + 1
            line['end']= x + int(input_line[1:])
            x = line['end']
            
        elif input_line[0] == 'L':
            line['direction'] = 'x'
            line['constant'] = y
            line['start'] = x - 1
            line['end']= x - int(input_line[1:])
            x = line['end']
        elif input_line[0] == 'U':
            line['direction'] = 'y'
            line['constant'] = x
            line['start'] = y + 1
            line['end']= y + int(input_line[1:])
            y = line['end']
        else:
            line['direction'] = 'y'
            line['constant'] = x
            line['start'] = y - 1
            line['end']= y - int(input_line[1:])
            y = line['end']
        wiremap.append(line)
            

    for i in wiremap:
        print(i)


if __name__ == '__main__':
    puzzle_input = get_input('test.txt')
    print(main(puzzle_input))
