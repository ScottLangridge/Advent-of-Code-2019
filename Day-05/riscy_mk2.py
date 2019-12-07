class RISCy:
    def __init__(self):
        # Registers
        self._pc = None
        self._memory = []
        self._input_queue = []
        self._io_log = []

        # Flags
        self._halt_flag = None

        # Instructions
        self._instruction_set = {
            99: {'len': 1, 'function': self._halt},
            1: {'len': 4, 'function': self._add},
            2: {'len': 4, 'function': self._mult},
            3: {'len': 2, 'function': self._input},
            4: {'len': 2, 'function': self._output}
        }

    def set_memory(self, data):
        self._memory = data

    def set_noun_verb(self, noun, verb):
        self._memory[1] = noun
        self._memory[2] = verb

    def set_input_queue(self, inputs):
        self._input_queue = inputs

    def get_io_log(self):
        return self._io_log

    def run(self):
        self._pc = 0
        self._halt_flag = False

        while not self._halt_flag:
            opcode, addressing_modes = self._process_instruction(self._memory[self._pc])
            first_operand = self._pc + 1
            last_operand = self._pc + self._instruction_set[opcode]['len']
            raw_operands = self._memory[first_operand:last_operand]
            operands = list(zip(raw_operands, addressing_modes))

            self._instruction_set[opcode]['function'](operands)
            self._pc += self._instruction_set[opcode]['len']

        return self._memory[0]

    def _process_instruction(self, instruction):
        instruction = str(instruction).zfill(2)
        opcode = int(instruction[-2:])

        instruction = instruction.zfill(self._instruction_set[opcode]['len'] + 1)
        modes = list(instruction[-3::-1])
        return opcode, modes

    def _eval_operand(self, operand):
        if operand[1] == '0':
            return self._memory[operand[0]]
        elif operand[1] == '1':
            return operand[0]

    def _add(self, operands):
        self._memory[operands[-1][0]] = self._eval_operand(operands[0]) + self._eval_operand(operands[1])

    def _mult(self, operands):
        self._memory[operands[-1][0]] = self._eval_operand(operands[0]) * self._eval_operand(operands[1])

    def _input(self, operands):
        if self._input_queue:
            val = self._input_queue[0]
            del self._input_queue[0]
        else:
            val = int(input('Input: '))
        self._io_log.append(val)
        self._memory[operands[0][0]] = val

    def _output(self, operands):
        val = str(self._eval_operand(operands[0]))
        self._io_log.append(val)
        print('Output: ' + val)

    def _halt(self, operands):
        self._halt_flag = True
