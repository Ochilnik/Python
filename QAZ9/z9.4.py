input_sentence = input("Введіть речення: ")
sentence_to_compare = input("Введіть речення для порівняння: ")
new_word = input("Введіть нове слово, яке потрібно додати в кінець речення: ")
input_word_to_remove = input("Введіть слово яке потрібно вилучити: ")


class Sentence:
    # your code goes here
    def __init__(self, sentence):
        self.sentence = sentence
        return

    def is_similar(self, b):
        if self.sentence.lower() == b.lower():
            return True
        else:
            return False

    def add_word(self, c):
        self.sentence = self.sentence + c
        return

    def to_lower(self):
        self.sentence = self.sentence.lower()
        return

    def remove_word(self, d):
        self.sentence = self.sentence.replace(d, "")
        return


my_sentence = Sentence(input_sentence)
print(my_sentence.is_similar(sentence_to_compare))

my_sentence.add_word(new_word)
my_sentence.to_lower()
print(my_sentence.sentence)

my_sentence.remove_word(input_word_to_remove)
print(my_sentence.sentence)
