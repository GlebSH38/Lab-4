import random


def random_ints(a, b):
    while True:
        yield random.randint(a, b)


def main():
    gen = random_ints(20, 50)
    print([next(gen) for _ in range(10)])


if __name__ == "__main__":
    main()
