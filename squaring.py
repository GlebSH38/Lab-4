def main():
    numbers = [x for x in range(1, 11)]
    squaring_numbers = list(map(lambda x: x**2, numbers))
    print("Исходный список:", numbers)
    print("Измененный список(в квадрате):", squaring_numbers)


if __name__ == "__main__":
    main()
