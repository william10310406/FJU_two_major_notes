x = int(input("x: "))
y = int(input("y: "))


def gcd_brute_force(x, y):
    ans = 1
    for i in range(2, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            ans = i
    return ans

def gcd_sub(x, y):
    while x != y:
        if x > y:
            x = x - y
        else:
            y = y - x
    return x

def gcd_mod(x, y):
    while y != 0:
        x, y = y, x % y
    return x

print(gcd_brute_force(x, y))
print(gcd_sub(x, y))
print(gcd_mod(x, y))
