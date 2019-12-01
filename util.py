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
