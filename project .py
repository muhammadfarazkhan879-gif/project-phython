import random
import string
def generate_random_chars(n=3):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(n))
def code_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        rest = word[1:] + first_letter
        start_random = generate_random_chars(3)
        end_random = generate_random_chars(3)
        return start_random + rest + end_random
    else:
        return word[::-1]
def decode_word(word):
    if len(word) < 3:
        return word[::-1]
    else:
        core = word[3:-3]
        last_letter = core[-1]
        rest = core[:-1]
        return last_letter + rest
def main():
    choice = input("Do you want to code or decode? (a/b): ").strip().lower()
    message = input("Enter your message: ").strip().split()
    if choice == 'a':
        result = [code_word(w) for w in message]
        print("Coded message:", ' '.join(result))
    elif choice == 'b':
        result = [decode_word(w) for w in message]
        print("Decoded message:", ' '.join(result))
    else:
        print("Invalid choice!")
if __name__ == "__main__":
    main()
