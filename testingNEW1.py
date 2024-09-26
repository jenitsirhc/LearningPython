def are_you_playing_banjo(name):
    if ("R" in name) or ("r" in name):
        print(name + " plays banjo")
        return name
    else:
        print(name + " does not play banjo")
        return name

are_you_playing_banjo("nera")
are_you_playing_banjo("Neil")