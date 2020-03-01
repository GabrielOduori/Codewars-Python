from collections import deque

def is_palindrome(characters):
    character_deque = deque(characters)

    while len(character_deque) > 1:
        first_char = character_deque.popleft()
        last_char = character_deque.pop()

        if first_char != last_char:
            return False
        return True


print(is_palindrome('02022020'))
print(is_palindrome('radar'))
print(is_palindrome('morning'))