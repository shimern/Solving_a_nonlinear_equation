import math

def f(x):
    return math.cos(x) + 2*x

def integral(a, b, accuracy):
    h = 0
    n = 0
    s = [0, 0]
    delta = accuracy + 1
    count = 0

    # КФ метод Симпсона 3/8
    for i in range(1, int(accuracy)):
        n = 3 * i
        h = (b - a) / n  # шаг

        s[1] = 0
        x = a + h

        while x <= b:
            s[1] += f(x - h) + 3 * f((2 * (x - h) + x) / 3) + 3 * f((x - h + 2 * x) / 3) + f(x)
            x += h

        s[1] *= h / 8

        delta = abs(s[1] - s[0])
        s[0] = s[1]
        count = i

    return s[1]  # находим значение в точке F_b

def main():
    print("Введите коэффициенты a, b: ")
    a = float(input())
    b = float(input())
    accuracy = float(input("Введите точность измерения: "))
    x0 = float(input("Введите начальное приближение: "))
    delta = accuracy + 1

    F1, F2 = 0, 0
    h = 3 * accuracy / 10

    while abs(delta) >= accuracy:
        F1 = integral(a, x0, accuracy) - b
        F2 = integral(a, x0 + h, accuracy) - b
        print(F1,F2)
        x1 = x0 - F1 * h / (F2 - F1)
        delta = x1 - x0

        x0 = x1

    print("Ответ:", x1)

if __name__ == "__main__":
    main()