from __future__ import annotations
from typing import List

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class TextModel:
    # разбивает текс на предложения, чистит от пробелов сохраняет резульатт
    def __init__(self, text: str) -> None:
        raw_sentences = text.split(".") if isinstance(text, str) else []
        self.sentences: List[str] = []
        for s in raw_sentences:
            s_clean = s.strip()
            if s_clean:
                self.sentences.append(s_clean)

        if len(self.sentences) == 0:
            self.vectorizer: TfidfVectorizer | None = None
            self.X = None
            return
        self.vectorizer = TfidfVectorizer()
        self.X = self.vectorizer.fit_transform(self.sentences)


# проверка входных данных, подготовка вопроса, вычисление косинусной схожести, сортировка и возврат ответов


    def getAnswers(self, question: str, nAnswers: int) -> List[str]:
        if (
            not isinstance(question, str)
            or len(question.strip()) == 0
            or not isinstance(nAnswers, int)
            or nAnswers <= 0
            or self.vectorizer is None
            or self.X is None
            or len(self.sentences) == 0
        ):
            return []
        q = question.strip()
        q_vec = self.vectorizer.transform([q])
        sims = cosine_similarity(q_vec, self.X)[0]

        pairs: List[tuple[int, float]] = []
        for i, s in enumerate(sims):
            if s > 0.0:
                pairs.append((i, float(s)))

        if len(pairs) == 0:
            return []

        pairs.sort(key=lambda t: t[1], reverse=True)

        result: List[str] = []
        count = 0
        for idx, _score in pairs:
            result.append(self.sentences[idx])
            count += 1
            if count >= nAnswers:
                break

        return result


# поиск ответа
if __name__ == "__main__":
    text = (
        "Питон - популярный язык программирования. "
        "fullstack разработчики используют Питон для создания веб-приложений."
        "Он подходит для анализа данных. "
        "С помощью TF-IDF можно измерять схожесть текстов. "
        "Машинное обучение помогает находить ответы."
    )

    model = TextModel(text)
# вопрос
    question = "Что такое Питон?"
#     примеры вопросов:
# 1-2
# "Что такое Питон?"
# "Почему Питон популярен?"
# 2
# "Кто использует Питон для создания сайтов?"
# "Для чего fullstack разработчики применяют Питон?"
# 3
# "Для чего подходит Питон?"  
# "Можно ли анализировать данные с помощью Питона?"
# 4  
# "Как измерять схожесть текстов?"  
# "Что делает TF-IDF?"  
# 5
# "Что помогает находить ответы?"  
# "Как машинное обучение помогает?" 

answers = model.getAnswers(question, nAnswers=3)

print("Вопрос:", question)
print("Ответы:")
for i, ans in enumerate(answers, 1):
    print(f"{i}. {ans}")
