class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
        return self.word+' ('+self.meaning+')'
flash = []
print("Welcome to flashcard aplication")
while(True):
    word = input("Enter the name you want to put in the flashcard:")
    meaning = input("Enter the meaning of the the word:")
    flash.append(flashcard(word, meaning))
    option = int(input("enter 0, if you want to add another flashcard or enter 1:"))
    if(option):
        break
print("Your Flashcards")
for i in flash:
    print(">", i)