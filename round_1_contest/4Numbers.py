def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_of_four(a, b, c, d):
    return gcd(gcd(a, b), gcd(c, d))


def calculate_max_gcd(a1, a2, a3, a4):
    max_gcd = 0
    possiblity = [-1, 0, 1]
    for d1 in possiblity:
        for d2 in possiblity:
            for d3 in possiblity:
                for d4 in possiblity:
                    new_a1 = a1 + d1
                    new_a2 = a2 + d2
                    new_a3 = a3 + d3
                    new_a4 = a4 + d4

                    current_gcd = gcd_of_four(new_a1, new_a2, new_a3, new_a4)

                    if current_gcd > max_gcd:
                        max_gcd = current_gcd

    return max_gcd

a, b,c,d = map(int, input().split())
print(calculate_max_gcd(a, b, c, d))