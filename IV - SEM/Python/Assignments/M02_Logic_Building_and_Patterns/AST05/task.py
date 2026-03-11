def number_triangle(n: int) -> str:
    #number triangle pattern
    return "\n".join(["".join(str(i) for i in range(1, j + 1)) for j in range(1, n + 1)])

if __name__ == "__main__":
    n = int(input())
    print(number_triangle(n))
