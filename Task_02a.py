# Task 02a - Count Vowels
# Write a function called count_vowels(text)
# that returns the number of vowels in the string.
# Count both uppercase and lowercase vowels.
#
# Vowels are: a, e, i, o, u
#
# Example:
# count_vowels("Education") -> 5

def count_vowels(text):
    # Write your code here
    text = text.lower()
    letters = list(text) 
    count = 0
    for value in letters:
        if value == 'a':
            count += 1
        elif value == 'e':
            count += 1
        elif value == 'i':
            count += 1
        elif value == 'o':
            count += 1
        elif value == 'u':
            count += 1
    return count
    pass


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
