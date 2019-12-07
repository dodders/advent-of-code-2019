def get_input(prod, day):
    if prod:
        fname = 'data.txt'
    else:
        fname = 'test.txt'

    f = open('day' + day + '/' + fname, 'r')
    lines = f.readlines()
    return [line.strip("\n") for line in lines]


def get_number_input(prod, day):
    return [int(num) for num in get_input(prod, day)]


class Node():
    def __init__(self, n, parent=None):
        self.value = n
        self.children = []
        if parent is not None:
            parent.add_child(self)

    def add_child(self, n):
        self.children.append(n)

    def child_values(self):
        return [c.value for c in self.children]

    def contains(self, node_val):
        # print("%s finding %s" % (self.value, node_val))
        if len(self.children) == 0:
            # print("%s not found %s returning 0" % (self.value, node_val))
            return 0
        if node_val in [c.value for c in self.children]:
            # print("%s found %s returning 1" % (self.value, node_val))
            return 1
        else:
            for child in self.children:
                found = child.contains(node_val)
                if found > 0:
                    return found + 1
            return 0

    def __repr__(self):
        return '%s ->: %s' % (self.value, self.child_values())


