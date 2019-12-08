class Computer:

    def __init__(self, program, phase):
        self.ptr = 0
        self.param_ct = 0
        self.op, self.m1, self.m2, self.m3, self.p1, self.p2, self.p3 = None, None, None, None, None, None, None
        self.input = None
        self.output = None
        self.halted = False
        self.stack = program
        self.phase = phase

    def __repr__(self):
        return 'Comp ph=%s in=%s out=%s' % (self.phase, self.input, self.output)

    def put_addr(self, addr, value):
        self.stack[addr] = value

    def get_addr(self, mode, addr):
        if mode == '1':
            return addr
        else:
            return self.stack[addr]

    def print_stack(self):
        ts = list((enumerate(self.stack)))
        print('ptr:', self.ptr, ' ', end='')
        for t in ts:
            print("%d:%d, " % (t[0], t[1]), sep=' ', end='')
        print()

    def print_op(self):
        print("op: %s modes :%s %s %s params: %s %s %s" % (
            self.op, self.m1, self.m2, self.m3, self.p1, self.p2, self.p3))

    def parse_operation(self):
        s = str(self.stack[self.ptr])
        self.op = int(s[-2:])
        if self.op == 99:
            # print('99! halting.')
            self.halted = True

        self.m1 = s[-3:-2]
        self.m2 = s[-4:-3]
        self.m3 = s[-5:-4]
        self.p1 = self.stack[self.ptr + 1]
        self.p2 = self.stack[self.ptr + 2]

    def do_op(self, param):
        if self.op == 1:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            self.p3 = self.stack[self.ptr + 3]
            res = v1 + v2
            self.put_addr(self.p3, res)
            self.ptr += 4
        elif self.op == 2:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            self.p3 = self.stack[self.ptr + 3]
            self.put_addr(self.p3, v1 * v2)
            self.ptr += 4
        elif self.op == 3:
            # print('using parameter:', param)
            self.put_addr(self.p1, int(param))
            self.param_ct += 1
            self.ptr += 2
        elif self.op == 4:
            self.output = self.get_addr(self.m1, self.p1)
            # print('output:', self.output)
            self.ptr += 2
        # jump if true
        elif self.op == 5:
            v1 = self.get_addr(self.m1, self.p1)
            if v1 > 0:
                self.ptr = self.get_addr(self.m2, self.p2)
            else:
                self.ptr += 3
        # jump if false
        elif self.op == 6:
            v1 = self.get_addr(self.m1, self.p1)
            if v1 == 0:
                return self.get_addr(self.m2, self.p2)
            else:
                self.ptr += 3
        # less than
        elif self.op == 7:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            self.p3 = self.stack[self.ptr + 3]
            if v1 < v2:
                self.put_addr(self.p3, 1)
            else:
                self.put_addr(self.p3, 0)
            self.ptr += 4
        # equals
        elif self.op == 8:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            self.p3 = self.stack[self.ptr + 3]
            if v1 == v2:
                self.put_addr(self.p3, 1)
            else:
                self.put_addr(self.p3, 0)
            self.ptr += 4
        else:
            # print('invalid opcode:', self.op)
            self.halted = True

    def run(self, amp_input):
        self.output = None  # dur...
        # print('running amp phase %s param_ct %s' % (self.phase, self.param_ct))
        while True:
            self.parse_operation()
            # first param is the phase setting, second is the program input.
            # count is in param_ct
            # first run with phase as the parameter for opcode 3
            if self.param_ct == 0:
                self.do_op(self.phase)
            else:
                self.do_op(amp_input)
            if self.output is not None:
                # print('returning:', self.output)
                return self.output
            if self.halted:
                return None
