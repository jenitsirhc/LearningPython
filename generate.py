townpop = {'sca' : 61.7, 'hull':256.4, 'york':208}

def gen():
    print("--Start--")
    print(townpop['hull'])
    yield 1
    print("--Middle--")
    print(townpop['sca'])
    yield 1
    print("-- End --")
    townpop ['leeds'] = 801
    print(townpop)
    yield 3

gen = gen()
next(gen)
next(gen)
next(gen)