# -*- coding: utf-8 -*-
import nltk
from nltk import word_tokenize, pos_tag
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger_ru')
from nltk.corpus import stopwords
from collections import Counter


def extract_title(text):
    # Токенизация текста
    words = word_tokenize(text)

    # Удаление стоп-слов (предлогов, союзов и пр.)
    stop_words = set(stopwords.words('russian'))
    filtered_words = [word.lower() for word in words if word.isalnum() and word.lower() not in stop_words]

    # Определение частей речи и отбор существительных и прилагательных
    tagged_words = pos_tag(filtered_words, lang='rus')
    relevant_words = [word for word, pos in tagged_words if pos in ('NOUN', 'ADJ')]

    # Подсчет частоты встречаемости слов
    word_counts = Counter(relevant_words)

    # Выбор первых 5 наиболее часто встречающихся слов
    title_words = [word for word, count in word_counts.most_common(5)]

    # Формирование заголовка из выбранных слов
    title = ' '.join(title_words)

    return title


# Пример использования
text = """
Встречайте новый выпуск проекта студентов Высшей школы кино и телевидения ВВГУ «СТУДиЯ»! Алексей Ковалёв и Наталья Гуреева познакомят вас с участниками кастинга телеведущих, который ВШКТВ провела среди студентов ВВГУ – это ребята и девушки из разных институтов, которые на собственном опыте попробовали, как это – быть лицом медиапроекта. В программе – сюжеты о предстоящем новогоднем конкурсе видеоработ, очередной номер авторской рубрики Алины Ушановой «Каракули», а также интервью с выпускником ВШКТВ Станиславом Васильченко. Ставь сердечки – поддержи молодых журналистов ❤
"""

title = extract_title(text)
print("Выделенный заголовок:", title)