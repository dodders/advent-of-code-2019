import util
from computer.computer import Computer

# inp = util.get_input(False, '07')
inp = util.get_input(True, '07')
program = [int(i) for i in inp[0].split(',')]
# phases = [4, 3, 2, 1, 0]
# phases = [1,0,4,3,2]


def between(i, minn, maxx):
    return maxx >= i >= minn


def gen_phases(start, end, minn=0, maxx=4):
    for phase in ['{:0>5}'.format(str(x)) for x in range(start, end)]:
        if len([ch for ch in phase if not between(int(ch), minn, maxx)]) == 0:
            if util.uniq(phase):
                yield phase


def run_amplifiers(amps):
    param = 0
    for x in range(0, len(amps.keys())):
        hal = amps[x]
        param = hal.run(param)
        # print('amp %s output %s halted %s' % (x, hal.output, hal.halted))
    return param


def cycle_amplifiers(amps):
    param = 0
    while True:
        for x in range(0, len(amps.keys())):
            hal = amps[x]
            # print('amp %s output %s halted %s' % (x, hal.output, hal.halted))
            out = hal.run(param)
            if hal.halted:
                # print('amp halted. returning')
                return param
            param = out


def part1():
    max_signal = None
    for phase in gen_phases(1234, 43211):
        amps = gen_amps(phase)
        thrust = run_amplifiers(amps)
        print('phase %s thrust %s max %s' % (phase, thrust, max_signal))
        if max_signal is None or thrust > max_signal:
            max_signal = thrust
    print('part1:', max_signal)


def gen_amps(phase):
    amps = {}
    for comp_id, phase in enumerate(phase):
        fixed_program = program.copy()
        amps[comp_id] = Computer(fixed_program, phase)
    return amps


def part2():
    max_signal = None
    for phase in gen_phases(56789, 98766, 5, 9):
        amps = gen_amps(phase)
        thrust = cycle_amplifiers(amps)
        print('phase %s thrust %s max %s' % (phase, thrust, max_signal))
        if max_signal is None or thrust > max_signal:
            max_signal = thrust
    print('part2:', max_signal)


# part1 51679
# part1()
part2()

# amps = gen_amps([9,7,8,5,6])
# thrust = cycle_amplifiers(amps)
# print('thrust:', thrust)
