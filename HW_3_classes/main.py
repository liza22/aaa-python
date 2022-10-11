from collections import defaultdict


CORPUS = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste",
]
CORRECT_FEATURE_NAMES = [
    "again",
    "boil",
    "crock",
    "fresh",
    "ingredients",
    "never",
    "parmesan",
    "pasta",
    "pomodoro",
    "pot",
    "taste",
    "to",
]
CORRECT_COUNT_MATRIX = [
    [1, 1, 1, 0, 0, 1, 0, 2, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
]


class CountVectorizer:
    """
    Класс для получения словаря уникальных слов из коллекции текстов
    и подсчета терм-документной матрицы
    """

    def __init__(self, lowercase: bool = True):
        """
        Параметры:
        lowercase - флаг необходимости перевода слов в нижний регистр
        """
        self._vocabulary = []
        self.lowercase = lowercase

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Заполняет список термов и терм-документную матрицу
        по коллекции corpus
        """
        uniq_words = set()
        counts_by_text: list[defaultdict[str, int]] = []

        for text in corpus:
            words_count = defaultdict(int)
            for word in text.split():
                word = word.lower() if self.lowercase else word
                words_count[word] += 1
                uniq_words.add(word)
            counts_by_text.append(words_count)

        self._vocabulary = list(uniq_words)
        self._vocabulary.sort()

        return [
            [counts_by_text[i][word] for word in self._vocabulary]
            for i in range(len(counts_by_text))
        ]

    def get_feature_names(self) -> list[str]:
        """Выдает список уникальных термов в коллекции"""
        return self._vocabulary


if __name__ == "__main__":
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(CORPUS)
    feature_names = vectorizer.get_feature_names()

    assert feature_names == CORRECT_FEATURE_NAMES, "incorrect feature names"
    assert count_matrix == CORRECT_COUNT_MATRIX, "incorrect count matrix"
