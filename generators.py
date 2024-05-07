import copy, gcd


def plus(modulo):
    space = list(range(1, modulo))
    generators = []

    for num in space:
        target = set(copy.deepcopy(space))
        killed = set()
        trial = num
        while trial not in killed:
            target.discard(trial)
            killed.add(trial)
            trial += num
            trial %= modulo
        if len(target) == 0:
            generators.append(num)

    return generators


def multiply(modulo):
    generators = []
    space = []
    for i in range(1, modulo):
        if gcd.gcd(i, modulo) == 1:
            space.append(i)

    for num in space:
        target = set(copy.deepcopy(space))
        killed = set()
        trial = num
        while trial not in killed:
            target.discard(trial)
            killed.add(trial)
            trial *= num
            trial %= modulo
        if len(target) == 0:
            generators.append(num)

    return generators