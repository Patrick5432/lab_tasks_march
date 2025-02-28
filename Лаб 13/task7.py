class Word:
    def __init__(self, the_word):
        self.the_word = the_word
        self.page_numbers = []

    @property
    def number_of_pages(self):
        return len(self.page_numbers)

    def __str__(self):
        return f"{self.the_word} - Страницы: {', '.join(map(str, self.page_numbers))}"


class WordManager:
    def __init__(self):
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def get_words_on_more_than_n_pages(self, n):
        return [word for word in self.words if word.number_of_pages > n]

    def get_words_in_alphabetical_order(self):
        return sorted(self.words, key=lambda w: w.the_word)

    def get_page_numbers_for_word(self, word):
        for w in self.words:
            if w.the_word.lower() == word.lower():
                return w.page_numbers
        return None

    def print_words(self, words):
        for word in words:
            print(word)


# Пример использования
wm = WordManager()
word1 = Word("Яблоко")
word1.page_numbers.extend([2, 3, 6, 7])
wm.add_word(word1)

word2 = Word("Бананы")
word2.page_numbers.extend([3, 5, 7])
wm.add_word(word2)

word3 = Word("Апельсины")
word3.page_numbers.extend([1, 2])
wm.add_word(word3)

print("Слова повторяющиеся более чем в 2 страницах:")
wm.print_words(wm.get_words_on_more_than_n_pages(2))

print("\nСлова в алфавитном порядке:")
wm.print_words(wm.get_words_in_alphabetical_order())

print("\nНомера страниц где встречается яблоко:")
apple_pages = wm.get_page_numbers_for_word("Яблоко")
if apple_pages:
    print(", ".join(map(str, apple_pages)))