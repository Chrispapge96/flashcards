# Write your code here

import os

def options(action, flashcards, terms, definitions):
    if action == "add":
#        file = open('flashcards.txt', 'a+')
#        card = input("The card:")
#        while card in file.read():
#            card = input("The term \"{}\" already exists. Try again:\n".format(card))
#        defi = input("The definition of the card:")
#        while defi in file.read():
#            defi = input("The term \"{}\" already exists. Try again:\n".format(defi))
#        file.write('"{}":"{}"\n'.format(card, defi))
#        file.close()

    ## here I redo the process without file system
        term = input("The card: \n")
        while term in terms:
            term = input("The term \"{}\" already exists. Try again:\n".format(term))

        terms.append(term)

        definition = input("The definition of the card:\n")
        while definition in definitions:
            definition = input("The definition \"{}\" already exists. Try again:\n".format(definition))

        definitions.append(definition)
        flashcards.update({term: definition})
        print('The pair ("{}":"{}") has been added.'.format(term, definition))

    elif action == "remove":
        term = input("Which card?")
#        with open("flashcards.txt", 'r') as input:
#            if card not in input:
#                print('Can\'t remove "{}": there is no such card.'.format(card))
#            else:
#                with open("temp.txt", 'w') as output:
#                    for line in input:
#                        if card not in line.strip("\n"):
#                            output.write(line)

#            os.replace('temp.txt', 'flashcards.txt')

            ##here I redo the process without file system
        if term not in terms:
            print('Can\'t remove "{}": there is no such card.'.format(term))
        else:
            terms.remove(term)
            definitions.remove(flashcards[term])
            flashcards.pop(term)
            print("The card has been removed.")

    elif action == "import":
        filename = input("File name:")
        if os.path.isfile(filename):
            file = open(filename + '.txt', 'r', encoding='utf-8')
            to_import = file.read().split(":")
            file.close()
            for i in range(len(to_import)-1):
                flashcards.update({to_import[i] : to_import[i+1]})
                terms.append(to_import[i])
                definitions.append(to_import[i+1])
            print("{} cards have been loaded.".format(int((len(to_import)+1)/2)))
        else:
            print("File not found.")


    elif action == "export":
        filename = input("File name:")
        cwd = os.getcwd()
        print(cwd)
        file = open(cwd + "\\" + filename, 'w', encoding='utf-8')
        for k , v in flashcards.items():
            file.write(k + ":" + v + "\n")
        file.close()
        print("{} cards have been saved.".format(len(flashcards)))

    elif action == "ask":
        ask_times = int(input("How many times to ask?"))
        for i in range(ask_times):
            k = i % len(terms)
            user = input("Print the definition of \"{}\":\n".format(terms[k]))
            if user == flashcards[terms[k]]:
                print('Correct!')
            else:
                if user in definitions:
                    inde = definitions.index(user)
                    print("Wrong.The right answer is \"{}\", but your definition is correct for \"{}\".".format(
                        flashcards[terms[k]], terms[inde]))
                else:
                    print("Wrong.The right answer is \"{}\".".format(flashcards[terms[k]]))

    elif action == "exit":
        print("Bye bye!")
        global stopi
        stopi = 1


#variable initialization
stopi = 0
flashcards = {}
terms = list()
definitions = list()

while stopi == 0:
    action = input("Input the action (add, remove, import, export, ask, exit):\n")
    options(action, flashcards, terms, definitions)