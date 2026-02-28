def Reverse_String(s: str) -> str:
    rev = ""
    for i in s:
        rev = i + rev
    return rev


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))