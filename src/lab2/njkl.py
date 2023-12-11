def gcd(a: int, b: int) -> int:
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def multiplicative_inverse(e: int, phi: int) -> int:
    def extended_euclidean_algorithm(a: int, b: int) -> tuple[int, int, int]:
        if b == 0:
            return a, 1, 0
        else:
            d, x, y = extended_euclidean_algorithm(b, a % b)
            return d, y, x - y * (a // b)

    d, x, y = extended_euclidean_algorithm(e, phi)
    if d != 1:
        raise ValueError("e не является взаимно простым с phi.")
    else:
        return x % phi
print(multiplicative_inverse(7,40))