def primes():
    yield 2
    n = 3
    while True:
        is_prime = True
        d = 3
        while d * d <= n:
            if n % d == 0:
                is_prime = False
                break
            d += 2
        if is_prime:
            yield n
        n += 2


def main():
    gen = primes()
    for _ in range(10):
        print(next(gen), end=" ")


if __name__ == "__main__":
    main()
