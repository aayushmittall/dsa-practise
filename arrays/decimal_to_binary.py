binary_str: str = ""


def decimal_to_binary_recursion(num: int) -> str:

    if num > 1:
        decimal_to_binary_recursion(num//2)
    global binary_str
    binary_str = binary_str+str(num % 2)
    return binary_str


def decimal_to_binary(num: int) -> str:
    binary_str = str(num % 2)
    while num > 1:
        num = num//2
        binary_str = str(num % 2)+binary_str

    return binary_str


if __name__ == "__main__":
    res = decimal_to_binary_recursion(9)
    print(res)

    res = decimal_to_binary(9)
    print(res)
