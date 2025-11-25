# Write a function that takes String as input & returns count of Vowel present in String.

userInput = input("Enter a string: ")
def vowelConsCount(userInput):
    vowels = "aeiouAEIOU"
    countVowel = 0
    countConsonants = 0

    for eachChar in userInput:
        if eachChar.isalpha():
            if eachChar in vowels:
                countVowel += 1
            else:
                countConsonants += 1
    return countVowel, countConsonants
vowels, consonants = vowelConsCount(userInput)
print(f"Vowels present : {vowels}")
print(f"Consonants present : {consonants}")