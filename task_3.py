def is_balanced(expression: str) -> bool:
    stack = []
    brackets = {')': '(', ']': '[', '}': '{'}
    open_brackets = set(brackets.values())

    for char in expression:
        if char in open_brackets:
            stack.append(char)
        elif char in brackets:
            if not stack or stack.pop() != brackets[char]:
                return False

    return not stack


def main():
    test_cases = [
        "( ){[ 1 ]( 1 + 3 )( ){ } }",  # Симетрично
        "( 23 ( 2 - 3) )",             # Симетрично
        "())",                         # Несиметрично
        "{{([][])}()} ",               # Симетрично
        "[[{{}}]]",                    # Симетрично
        "( ( ( )",                     # Несиметрично
        "( 11 }",                      # Несиметрично
        "([)]"                         # Несиметрично
    ]

    print("Перевірка симетричності дужок:")
    for expression in test_cases:
        if is_balanced(expression):
            print(f'"{expression}": Симетрично')
        else:
            print(f'"{expression}": Несиметрично')


if __name__ == "__main__":
    main()
