def numberOfWords():
    return sum(1 for _ in open('words.txt'))

def existInDictionary(word):
    file = open("words.txt")
    return word in file.read()

def searchEngine(hintValue, hintNumber, result, validWord = []):
    return "Search Engine"

def main():
    print("--------------------------------------------------------------------------------------")
    print("--                                  Wordle Solver                                   --")
    print("--------------------------------------------------------------------------------------")
    print("There is ", numberOfWords(), "five letters words in my dictionary (words.txt)")
    print("Hint the first word (how about \"ADIEU\" or \"OUIJA\" to find a maximum of vowels ?) :")
    i = 1
    while i <= 5:
        print("Your hint number ", i, " : ")
        hint = input()
        # Is this a 5 letter word ? 
        if type(hint) == str and len(hint)==5:
            # Does it exist in the word.txt file ? 
            if(existInDictionary(hint)):
                print("Your hint is :", hint)
                print("What is the result (example : \"__X_O\" where \"_\" doesn't exist, \"X\" exist, \"O\" is correct) :")
                result = input()
                if type(result) == str and len(result)==5:
                    print(searchEngine(hint, i, result))
                    i += 1
                else : print("The result is not well formatted")
            else : print("The word doesn't exist in my dictionary (words.txt)")
        else : print("That's not a 5 letters word")

if __name__ == '__main__':
    main()