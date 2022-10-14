from collections import defaultdict
from math import log

CORPUS = [
    "Crock Pot Pasta Never boil pasta again",
    "Pasta Pomodoro Fresh ingredients Parmesan to taste",
]


# задача 1 (класс из дз)
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


class TfidfTransformer:
    """
    Класс для подсчета tf-idf
    """

    # задача 2 - подсчет term frequency
    @staticmethod
    def _tf_transform(matrix: list[list[int]]) -> list[list[float]]:
        """
        Параметры:
        matrix - терм-документная матрица
        Считает матрицу term frequency
        """
        return [[num / sum(row) for num in row] for row in matrix]

    # задача 3 - подсчет inverse document frequency
    @staticmethod
    def _idf_matrix(matrix: list[list[int]]) -> list[float]:
        """
        Параметры:
        matrix - терм-документная матрица
        Считает inverse document frequency
        """
        docs_num = len(matrix)
        docs_for_word_cnt = [sum([num > 0 for num in row]) for row in zip(*matrix)]
        return list(map(lambda x: log((docs_num + 1) / (x + 1)) + 1, docs_for_word_cnt))

    # задача 4 - класс TfidfTransformer с методом fit_transform
    def fit_transform(self, matrix: list[list[int]]) -> list[list[float]]:
        """Считает tf_idf по терм-документной матрице"""
        tf = self._tf_transform(matrix)
        idf = self._idf_matrix(matrix)
        return [[x * y for x, y in zip(row, idf)] for row in tf]


# задача 5, совместить два класса
# нужен класс, который считает tf-idf из корпуса, а не из матрицы
class TfidfVectorizer(CountVectorizer):
    """
    Класс для подсчета tf-idf из коллекции текстов
    """
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list[float]]:
        matrix = super().fit_transform(corpus)
        return self.tfidf_transformer.fit_transform(matrix)


if __name__ == "__main__":
    tfidf_vec = TfidfVectorizer()
    print(tfidf_vec.fit_transform(CORPUS))
    print(tfidf_vec.get_feature_names())
