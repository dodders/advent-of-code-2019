def get_input(prod, day):
    if prod:
        fname = 'data.txt'
    else:
        fname = 'test.txt'

    f = open('day' + day + '/' + fname, 'r')
    return f.readlines()
