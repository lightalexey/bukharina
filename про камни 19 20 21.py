from functools import lru_cache
def move(h):
    a, b = h
    return (a+1, b),(a, b+1),(a*4, b),(a, b*4)
@lru_cache(None)
def game(h):
    if sum(h) >= 61:
        return 'W'
    if any(game(m) == 'W' for m in move(h)):
        return 'P1'
    if all(game(m) == 'P1' for m in move(h)):
        return 'B1'
    if any(game(m) == 'B1' for m in move(h)):
        return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in move(h)):
        return 'B2'
for S in range(1, 58):
    # if game((3, S)) == 'P2':
    #    print(S)
    print(S, game((3, S)))