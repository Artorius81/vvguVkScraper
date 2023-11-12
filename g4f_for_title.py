# -*- coding: utf-8 -*-
import g4f
# Automatic selection of provider

# # Streamed completion
# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}],
#     stream=True,
# )
#
# for message in response:
#     print(message, flush=True, end='')

# Normal response
response = g4f.ChatCompletion.create(
    model="palm",
    provider=g4f.Provider.Bard,
    messages=[{"role": "user", "content": "Проанализируй текст и создай к нему заголовок. Максимум 5 слов в заголовке. Вот теккст: Как стать для абитуриентов приоритетом номер один, чем оживить привычную профориентационную работу со школьниками – эти темы стали главными на заседании Ученого Совета ВВГУ. Об итогах прошедшей приемной кампании и планах на будущий набор читай на сайте: https://vk.cc/csfILJ"}],
)  # Alternative model setting

print(response)
