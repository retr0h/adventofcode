OP_ADD = 1
OP_MUL = 2
OP_END = 99


def get_opcode_chunks(codes, n=4):
    return [codes[i : i + n] for i in range(0, len(codes), n)]


def intcode(opcodes):
    codes = opcodes.copy()

    # Slice opcodes into chunks of instructions.
    chunks = get_opcode_chunks(codes)
    for chunk in chunks:
        if len(chunk) == 4:
            opcode, input1, input2, output = chunk
            if opcode != OP_END:
                i1 = codes[input1]
                i2 = codes[input2]
                if opcode == OP_ADD:
                    codes[output] = i1 + i2
                elif opcode == OP_MUL:
                    codes[output] = i1 * i2
                else:
                    pass

    return codes


# Part 1
with open('input', 'r') as f:
    opcodes = list(map(int, f.read().split(',')))

    # To do this, before running the program, replace position 1
    # with the value 12 and replace position 2 with the value 2.
    opcodes[1] = 12
    opcodes[2] = 2

    codes = intcode(opcodes)
    print(codes)
