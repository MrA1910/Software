def decode_instructions(filename):
    with open(filename, 'r') as f:
        instructions = [line.strip().split(' -> ') for line in f]
    instructions = {instr[1]: instr[0].split(' ') for instr in instructions}
    registers = {}

    def get_value(register):
        if register.isdigit():
            return int(register)
        if register not in registers:
            instr = instructions[register]
            if "AND" in instr:
                registers[register] = get_value(instr[0]) & get_value(instr[2])
            elif "OR" in instr:
                registers[register] = get_value(instr[0]) | get_value(instr[2])
            elif "NOT" in instr:
                registers[register] = ~get_value(instr[1]) & 0xffff
            elif "LSHIFT" in instr:
                registers[register] = get_value(instr[0]) << get_value(instr[2])
            elif "RSHIFT" in instr:
                registers[register] = get_value(instr[0]) >> get_value(instr[2])
            else:
                registers[register] = get_value(instr[0])
        return registers[register]

    return get_value('a')

print("Value of register 'a':", decode_instructions('input.txt'))
