from collections import deque


def is_palindrome(s: str) -> bool:
    formatted_s = "".join(char for char in s.lower() if char.isalnum())
    d = deque(formatted_s)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False

    return True


def main():
    test_cases = [
        "A man a plan a canal Panama",
        "Was it a car or a cat I saw",
        "No lemon no melon",
        "Hello World",
        "madam",
        "racecar",
        "12321",
        "GoIT"
    ]

    for test_str in test_cases:
        result = "є паліндромом" if is_palindrome(test_str) else "не є паліндромом"
        print(f"Рядок '{test_str}' - {result}.")


if __name__ == "__main__":
    main()
