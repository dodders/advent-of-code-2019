class Computer:

    def __init__(self, program):
        self.ptr = 0
        self.param_ct = 0
        self.op, self.m1, self.m2, self.m3, self.p1, self.p2, self.p3 = None, None, None, None, None, None, None
        self.input = None
        self.output = []
        self.halted = False
        self.stack = program
        self.stack[len(program)] = 0  # RTFM
        self.relative_base = 0

    def __repr__(self):
        return 'Comp in=%s out=%s' % (self.input, self.output)

    def put_addr(self, addr, value, mode):
        # relative mode
        if mode == 2:
            self.stack[self.relative_base + addr] = value
        # position mode
        else:
            self.stack[addr] = value

    def get_addr(self, mode, addr):
        # immediate mode
        if mode == '1':
            return addr
        # relative mode
        elif mode == '2':
            return self.stack.get(self.relative_base + addr, 0)
        # position mode 0
        else:
            return self.stack.get(addr, 0)

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
        else:
            self.m1 = s[-3:-2]
            self.m2 = s[-4:-3]
            self.m3 = s[-5:-4]
            self.p1 = self.stack[self.ptr + 1]
            self.p2 = self.stack[self.ptr + 2]

    def do_op(self):
        if self.op == 1:
            # add 2 parameters and store in 3rd param
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            # self.p3 = self.stack[self.ptr + 3]
            self.p3 = self.get_addr(self.m3, self.ptr + 3)
            res = v1 + v2
            self.put_addr(self.p3, res, self.m3)
            self.ptr += 4
        elif self.op == 2:
            # multiply 2 parameters and store in 3rd param
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            # self.p3 = self.stack[self.ptr + 3]
            self.p3 = self.get_addr(self.m3, self.ptr + 3)
            self.put_addr(self.p3, v1 * v2, self.m3)
            self.ptr += 4
        elif self.op == 3:
            # print('using parameter:', param)
            param = input('-->')
            self.put_addr(self.p1, int(param), self.m3)
            self.param_ct += 1
            self.ptr += 2
        elif self.op == 4:
            self.output.append(self.get_addr(self.m1, self.p1))
            print('output:', self.output)
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
                self.ptr = self.get_addr(self.m2, self.p2)
            else:
                self.ptr += 3
        # less than
        elif self.op == 7:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            # self.p3 = self.stack[self.ptr + 3]
            self.p3 = self.get_addr(self.m3, self.ptr + 3)
            if v1 < v2:
                self.put_addr(self.p3, 1, self.m3)
            else:
                self.put_addr(self.p3, 0, self.m3)
            self.ptr += 4
        # equals
        elif self.op == 8:
            v1 = self.get_addr(self.m1, self.p1)
            v2 = self.get_addr(self.m2, self.p2)
            # self.p3 = self.stack[self.ptr + 3]
            self.p3 = self.get_addr(self.m3, self.ptr + 3)
            if v1 == v2:
                self.put_addr(self.p3, 1, self.m3)
            else:
                self.put_addr(self.p3, 0, self.m3)
            self.ptr += 4
        elif self.op == 9:
            offset = self.get_addr(self.m1, self.p1)
            self.relative_base += offset
            self.ptr += 2
        else:
            # print('invalid opcode:', self.op)
            self.halted = True

    def pprint(self):
        for x in range(0, self.ptr):
            print(self.stack.get(x, 0), ' ', end='')
        print('*%s' % self.stack.get(self.ptr, 0), ' ', end='')
        for x in range(self.ptr + 1, max(self.stack.keys()) + 1):
            print(self.stack.get(x, 0), ' ', end='')
        print()

    def run(self):
        self.output = []  # dur...
        while True:
            self.parse_operation()
            if self.op == 99:
                print('halting.')
                exit(0)
            self.pprint()
            print('ptr %s opcode %s rel base %s' % (self.ptr, self.op, self.relative_base))
            self.do_op()
            # if self.output is not None:
            #     # print('returning:', self.output)
            #     return self.output
            if self.halted:
                return None
