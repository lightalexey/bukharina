
for n in range(100):
    nb = bin(n)
    # if nb.count('1')%2 ==0:
    #     nb += '0'
    # else:
    #     nb += '1'
    # if nb.count('1')%2 ==0:
    #     nb += '0'
    # else:
    #     nb += '1'
    nb += str(nb.count('1')%2)
    nb += str(nb.count('1') % 2)
    if int(nb,2) > 43:
        print(int(nb,2))
        break
