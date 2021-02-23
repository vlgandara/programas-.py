def maior_primo(x):
    y = x
    while y > 2:
        if éPrimo(y):
            return y
        y -= 1
    return 2

def éPrimo(k):
    z = 2
    while z * z <= k:
        if k % z == 0:
            return False
        z += 1
    return True