from functools import reduce


def pipe(*functions):
    """Возвращает функцию: применяет functions слева направо."""
    return lambda x: reduce(lambda acc, f: f(acc), functions, x)


def main():
    result = pipe(
        str.strip,
        str.upper,
        lambda s: s.replace(" ", "_"),
    )("  hello world  ")
    print(result)


if __name__ == "__main__":
    main()
