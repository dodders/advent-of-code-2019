from util import get_input
from util import Node

# raw = get_input(False, '06')
raw = get_input(True, '06')
inp = [e.split(")") for e in raw]


def part1(inp):
    q = []
    cts = {}
    for i in inp:
        if i[0] == 'COM':
            q.append(i)
            inp.remove(i)
            cts[i[1]] = 1
            break

    print('starting:', q)

    # process edges. each edge is scored 1 + parent edge score.
    # edge scores are in cts.
    while len(q) > 0:
        again = []
        node = q.pop()
        node_score = cts[node[1]]
        for i in inp:
            if node[1] == i[0]:
                new_node = i[1]
                cts[new_node] = node_score + 1
                q.append(i)
            else:
                again.append(i)
        inp = again.copy()  # need this because removing items from the original list aint safe.
        print(cts, q, inp)

    # part 1 273985
    p1 = sum(cts.values())
    print(p1)


def get_node(bag, node_val):
    if node_val in bag:
        return bag[node_val]
    else:
        node = Node(node_val)
        bag[node_val] = node
        return node


def part2(inp):
    # same tree search but in reverse, starting from YOU.
    # q = []
    # scores = {}
    # for i in inp:
    #     if i[1] == 'YOU':
    #         q.append(i)
    #         inp.remove(i)
    #         scores[i[0]] = 1
    #         break
    #
    # print('starting:', q)
    #
    # # ugh. need to process edges in both directions, same scoring as above.
    # while len(q) > 0:
    #     again = []
    #     curr = q.pop()
    #     curr_score = scores[curr[0]]
    #     for i in inp:
    #         if curr[0] == i[1]:
    #             scores[i[0]] = curr_score + 1
    #             q.append(i)
    #         else:
    #             again.append(i)
    #     inp = again.copy()  # need this because removing items from the original list aint safe.
    #     print(scores, q, inp)
    #
    # # part 2
    # print('cts:', scores)


# part1(inp)
    nodes = {}
    for i in inp:
        node_val = i[1]
        parent_val = i[0]
        parent_node = get_node(nodes, parent_val)
        node = get_node(nodes, node_val)
        parent_node.add_child(node)
        # print(list(nodes.values()))

    distances = {}
    for node in nodes.values():
        n1 = node.contains('YOU')
        n2 = node.contains('SAN')
        if n1 > 0 and n2 > 0:
            distances[node.value] = (n1, n2)
    print(distances)
    mind = None
    for d in distances.values():
        absd = d[0] + d[1]
        if mind is None or absd < mind:
            mind = absd

    # part2 is 460
    print('part 2:', mind - 2)  # discount the YOU and SAN orbits.


# part1(inp)
part2(inp)
