import util
from computer.computer import Computer

# inp = util.get_input(False, '09')
inp = util.get_input(True, '09')
opcodes = [int(i) for i in inp[0].split(',')]
program = {}
for x, op in enumerate(opcodes):
    program[x] = op


hal = Computer(program)
out = hal.run()
print(out)

