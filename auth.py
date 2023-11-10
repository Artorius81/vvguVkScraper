import json
import os
from datetime import datetime
from supabase_insert import *

import requests

token = 'fae69343fae69343fae6934300f9f0ae6effae6fae693439faa0217340b775d4aa36904'


def get_wall_posts(group_name):
    url = f'https://api.vk.com/method/wall.get?domain={group_name}&count=40&access_token={token}&v=5.137'
    req = requests.get(url)
    src = req.json()

    if os.path.exists(f'{group_name}'):
        print(f'Директория группы {group_name} существует.')
    else:
        os.mkdir(group_name)

    with open(f'{group_name}/{group_name}.json', 'w', encoding='utf-8') as file:
        json.dump(src, file, indent=4, ensure_ascii=False)

    new_posts_id = []
    posts = src['response']['items']

    for new_post_id in posts:
        new_post_id = new_post_id["id"]
        new_posts_id.append(new_post_id)

    if not os.path.exists(f'{group_name}/existed_posts.txt'):
        print(f'Файла с id постов группы {group_name} не найдено.')
        with open(f'{group_name}/existed_posts.txt', 'w') as file:
            for item in new_posts_id:
                file.write(str(item) + '\n')

        for post in posts:

            post_id = post['id']
            print(f'Пост с id {post_id}\n')

            post_date = post['date']
            post_date = datetime.fromtimestamp(post_date)
            print(f'Дата поста {post_date}\n')

            post_text = None
            post_photos = []
            doc_url = None
            doc_title = None
            link_url = None
            link_title = None
            audio_url = None
            audio_artist = None
            audio_title = None

            try:
                # если пост это репост с другого поста
                if 'copy_history' in post:
                    repost = post['copy_history'][0]
                    # проверка есть ли текст в посте
                    if 'text' in repost:
                        post_text = repost['text']
                        # print("Post text:", post_text)

                    #  проверка есть ли прикрепленные файлы в том посте
                    if 'attachments' in repost:
                        for attachment in repost['attachments']:
                            if attachment['type'] == 'photo':
                                if len(attachment) == 1:
                                    sizes = attachment[0]['photo']['sizes']
                                    for size in sizes:
                                        if size['type'] == 'z':  # берём лучшее качество
                                            post_photos.append(size['url'])
                                            # post_photo = size['url']
                                            # print(post_photos)
                                else:
                                    sizes = attachment['photo']['sizes']
                                    for size in sizes:
                                        if size['type'] == 'z':  # берём лучшее качество
                                            post_photos.append(size['url'])
                                            # post_photo = size['url']
                                            # print(post_photos)

                            #  проверка есть ли прикрепленные документы
                            elif attachment['type'] == 'doc':
                                doc_title = attachment['doc']['title']
                                doc_url = attachment['doc']['url']
                                # print("Doc Title:", doc_title)
                                # print("Doc URL:", doc_url)

                            #  проверка есть ли прикреплённые ссылки
                            elif attachment['type'] == 'link':
                                link_title = attachment['link']['title']
                                link_url = attachment['link']['url']
                                # print("Link Title:", link_title)
                                # print("Link URL:", link_url)

                            #  проверка есть ли прикреплённые аудио
                            elif attachment['type'] == 'audio':
                                audio_artist = attachment['audio']['artist']
                                audio_title = attachment['audio']['title']
                                audio_url = attachment['audio']['url']
                                # print("Audio Artist:", audio_artist)
                                # print("Audio Title:", audio_title)
                                # print("Audio URL:", audio_url)
                    sup_insert(
                        time=post_date,
                        text_title=post_text,
                        text=post_text,
                        image=post_photos,
                        doc=doc_url,
                        doc_title=doc_title,
                        link=link_url,
                        link_title=link_title,
                        audio=audio_url,
                        audio_artist=audio_artist,
                        audio_title=audio_title
                    )
                # если это просто пост
                else:
                    if 'text' in post:  # проверка есть ли текст в посте
                        post_text = post['text']
                        # print("Post text:", post_text)
                    # если это не репост другого поста
                    if 'attachments' in post:  # проверка есть ли какие-либо прикреплённые файлы
                        for attachment in post['attachments']:
                            if attachment['type'] == 'photo':
                                if len(attachment) == 1:  # проверяем если одно фото
                                    sizes = attachment[0]['photo']['sizes']
                                    for size in sizes:
                                        if size['type'] == 'z':  # берём лучшее качество
                                            post_photos.append(size['url'])
                                            # post_photo = size['url']
                                            # print(post_photos)
                                else:  # если несколько фото
                                    sizes = attachment['photo']['sizes']
                                    for size in sizes:
                                        if size['type'] == 'z':  # берём лучшее качество
                                            post_photos.append(size['url'])
                                            # post_photo = size['url']
                                            # print(post_photos)

                            #  проверка есть ли прикреплённые ссылки
                            elif attachment['type'] == 'doc':
                                doc_title = attachment['doc']['title']
                                doc_url = attachment['doc']['url']
                                # print("Doc Title:", doc_title)
                                # print("Doc URL:", doc_url)

                            #  проверка есть ли прикреплённые ссылки
                            elif attachment['type'] == 'link':
                                link_title = attachment['link']['title']
                                link_url = attachment['link']['url']
                                # print("Link Title:", link_title)
                                # print("Link URL:", link_url)

                            #  проверка есть ли прикреплённые аудио
                            elif attachment['type'] == 'audio':
                                audio_artist = attachment['audio']['artist']
                                audio_title = attachment['audio']['title']
                                audio_url = attachment['audio']['url']
                                # print("Audio Artist:", audio_artist)
                                # print("Audio Title:", audio_title)
                                # print("Audio URL:", audio_url)
                    sup_insert(
                        time=post_date,
                        text_title=post_text,
                        text=post_text,
                        image=post_photos,
                        doc=doc_url,
                        doc_title=doc_title,
                        link=link_url,
                        link_title=link_title,
                        audio=audio_url,
                        audio_artist=audio_artist,
                        audio_title=audio_title
                    )
            except Exception:
                print('Что-то пошло не так.')
    else:
        print(f'Файл с id постов группы {group_name} найден.')


def main():
    group_name = 'vvsu_dv'
    get_wall_posts(group_name)


if __name__ == '__main__':
    main()
