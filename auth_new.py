# import json
# import os
# from supabase import create_client
# from datetime import datetime
#
# import requests
#
# url = "https://hgsbnelwjopuhevsglmm.supabase.co"
# key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhnc2JuZWx3am9wdWhldnNnbG1tIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NDc5ODcxNCwiZXhwIjoyMDEwMzc0NzE0fQ.l0LQs2V1serM8JomNcyYOtr5F56MHao0LivqJaJk6zg"
#
# token = 'vk1.a.KOIWBFmXerwYS8GQaDkmXV_jEaNil8Xwx0dEN21xM9FHpOTmyI2t_WQRfcT9WFJzlSPifkkF6_Ew1dZDnOE48qVf5fgBcPniymXnxbmfrkjhrBADmsI_9hZ9tgeript9qBcD_bBMd6DAQ0Dhra1K_2Lkunz-OYsG1SSm9kVJbC3s3sYoUZ-jvnBAmz65N_egpkjhWNR_w1ijyCNED67BOQ'
#
# supabase = create_client(url, key)
#
#
# def get_wall_posts(group_name):
#     url = f'https://api.vk.com/method/wall.get?domain={group_name}&count=15&access_token={token}&v=5.137'
#     req = requests.get(url)
#     src = req.json()
#
#     if os.path.exists(f'{group_name}'):
#         print(f'Директория группы {group_name} существует.')
#     else:
#         os.mkdir(group_name)
#
#     with open(f'{group_name}/{group_name}.json', 'w', encoding='utf-8') as file:
#         json.dump(src, file, indent=4, ensure_ascii=False)
#
#     new_posts_id = []
#     posts = src['response']['items']
#
#     for new_post_id in posts:
#         new_post_id = new_post_id["id"]
#         new_posts_id.append(new_post_id)
#
#     if not os.path.exists(f'{group_name}/existed_posts.txt'):
#         print(f'Файла с id постов группы {group_name} не найдено.')
#         with open(f'{group_name}/existed_posts.txt', 'w') as file:
#             for item in new_posts_id:
#                 file.write(str(item) + '\n')
#
#         for post in posts:
#
#             post_id = post['id']
#             print(f'Пост с id {post_id}\n')
#
#             post_date = post['date']
#             post_date = datetime.fromtimestamp(post_date)
#             print(f'Дата поста {post_date}\n')
#
#             post_text = None
#             post_photos = []
#             docs = []
#             links = []
#             audios = []
#             videos = []
#
#             try:
#                 # если пост это репост с другого поста
#                 if 'copy_history' in post:
#                     repost = post['copy_history'][0]
#                     # проверка есть ли текст в посте
#                     if 'text' in repost:
#                         post_text = repost['text']
#                         print("Post text:", post_text)
#
#                     #  проверка есть ли прикрепленные файлы в том посте
#                     if 'attachments' in repost:
#                         for attachment in repost['attachments']:
#                             if attachment['type'] == 'photo':
#                                 if len(attachment) == 1:
#                                     sizes = attachment[0]['photo']['sizes']
#                                     for size in sizes:
#                                         if size['type'] == 'z':  # берём лучшее качество
#                                             post_photos.append(size['url'])
#                                             # post_photo = size['url']
#                                 else:
#                                     sizes = attachment['photo']['sizes']
#                                     for size in sizes:
#                                         if size['type'] == 'z':  # берём лучшее качество
#                                             post_photos.append(size['url'])
#                                             # post_photo = size['url']
#
#                             #  проверка есть ли прикрепленные документы
#                             elif attachment['type'] == 'doc':
#                                 doc_title = attachment['doc']['title']
#                                 docs.append(doc_title)
#                                 doc_url = attachment['doc']['url']
#                                 docs.append(doc_url)
#
#                             #  проверка есть ли прикреплённые ссылки
#                             elif attachment['type'] == 'link':
#                                 link_title = attachment['link']['title']
#                                 links.append(link_title)
#                                 link_url = attachment['link']['url']
#                                 links.append(link_url)
#
#                             #  проверка есть ли прикреплённые аудио
#                             elif attachment['type'] == 'audio':
#                                 audio_artist = attachment['audio']['artist']
#                                 audios.append(audio_artist)
#                                 audio_title = attachment['audio']['title']
#                                 audios.append(audio_title)
#                                 audio_url = attachment['audio']['url']
#                                 audios.append(audio_url)
#
#                             # проверка есть ли видео в посте
#                             elif attachment['type'] == 'video':
#                                 video_access_key = attachment['video']['access_key']
#                                 video_post_id = attachment['video']['id']
#                                 video_owner_id = attachment['video']['owner_id']
#
#                                 video_get_url = f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.137'
#                                 req = requests.get(video_get_url)
#                                 res = req.json()
#                                 video_title = res['response']['items'][0]['title']
#                                 videos.append(video_title)
#                                 video_date = res['response']['items'][0]['date']
#                                 video_date = datetime.fromtimestamp(video_date)
#                                 videos.append(video_date)
#                                 video_url = res['response']['items'][0]['player']
#                                 videos.append(video_url)
#
#                                 for item in res['response']['items'][0]['image']:
#                                     if (item['width'] and item['height']) == (
#                                             res['response']['items'][0]['width'] and res['response']['items'][0][
#                                         'height']):
#                                         video_presplash = item['url']
#                                         videos.append(video_presplash)
#                         print("Photos:", post_photos)
#                         print("Docs:", docs)
#                         print("Links:", links)
#                         print("Audios:", audios)
#                         print("Videos:", videos)
#                     # table_data = (supabase.table("vkvvguposts")
#                     #               .insert(
#                     #     {"created_at": f"{post_date}",
#                     #      "title": f"{post_text}",
#                     #      "text": f"{post_text}",
#                     #      "image": f"{post_photos}",
#                     #      "docs": f"{docs}",
#                     #      "links": f"{links}",
#                     #      "audios": f"{audios}",
#                     #      "videos": f"{videos}",
#                     #      }
#                     # )
#                     #               .execute())
#                     # assert len(table_data.data) > 0
#                 # если это просто пост
#                 else:
#                     if 'text' in post:  # проверка есть ли текст в посте
#                         post_text = post['text']
#                         print("Post text:", post_text)
#                     # если это не репост другого поста
#                     if 'attachments' in post:  # проверка есть ли какие-либо прикреплённые файлы
#                         for attachment in post['attachments']:
#                             if attachment['type'] == 'photo':
#                                 if len(attachment) == 1:  # проверяем если одно фото
#                                     sizes = attachment[0]['photo']['sizes']
#                                     for size in sizes:
#                                         if size['type'] == 'z':  # берём лучшее качество
#                                             post_photos.append(size['url'])
#                                             # post_photo = size['url']
#                                 else:  # если несколько фото
#                                     sizes = attachment['photo']['sizes']
#                                     for size in sizes:
#                                         if size['type'] == 'z':  # берём лучшее качество
#                                             post_photos.append(size['url'])
#                                             # post_photo = size['url']
#
#                             #  проверка есть ли прикреплённые ссылки
#                             elif attachment['type'] == 'doc':
#                                 doc_title = attachment['doc']['title']
#                                 docs.append(doc_title)
#                                 doc_url = attachment['doc']['url']
#                                 docs.append(doc_url)
#
#                             #  проверка есть ли прикреплённые ссылки
#                             elif attachment['type'] == 'link':
#                                 link_title = attachment['link']['title']
#                                 links.append(link_title)
#                                 link_url = attachment['link']['url']
#                                 links.append(link_url)
#
#                             #  проверка есть ли прикреплённые аудио
#                             elif attachment['type'] == 'audio':
#                                 audio_artist = attachment['audio']['artist']
#                                 audios.append(audio_artist)
#                                 audio_title = attachment['audio']['title']
#                                 audios.append(audio_title)
#                                 audio_url = attachment['audio']['url']
#                                 audios.append(audio_url)
#
#                             #  проверка есть ли видео в посте
#                             elif attachment['type'] == 'video':
#                                 video_access_key = attachment['video']['access_key']
#                                 video_post_id = attachment['video']['id']
#                                 video_owner_id = attachment['video']['owner_id']
#
#                                 video_get_url = f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.137'
#                                 req = requests.get(video_get_url)
#                                 res = req.json()
#                                 video_title = res['response']['items'][0]['title']
#                                 videos.append(video_title)
#                                 video_date = res['response']['items'][0]['date']
#                                 video_date = datetime.fromtimestamp(video_date)
#                                 videos.append(video_date)
#                                 video_url = res['response']['items'][0]['player']
#                                 videos.append(video_url)
#
#                                 for item in res['response']['items'][0]['image']:
#                                     if (item['width'] and item['height']) == (
#                                             res['response']['items'][0]['width'] and res['response']['items'][0][
#                                         'height']):
#                                         video_presplash = item['url']
#                                         videos.append(video_presplash)
#                         print("Photos:", post_photos)
#                         print("Docs:", docs)
#                         print("Links:", links)
#                         print("Audios:", audios)
#                         print("Videos:", videos)
#                     # table_data = (supabase.table("vkvvguposts")
#                     #               .insert(
#                     #     {"created_at": f"{post_date}",
#                     #      "title": f"{post_text}",
#                     #      "text": f"{post_text}",
#                     #      "image": f"{post_photos}",
#                     #      "docs": f"{docs}",
#                     #      "links": f"{links}",
#                     #      "audios": f"{audios}",
#                     #      "videos": f"{videos}",
#                     #      }
#                     # )
#                     #               .execute())
#                     # assert len(table_data.data) > 0
#             except Exception:
#                 print('Что-то пошло не так.')
#     else:
#         print(f'Файл с id постов группы {group_name} найден.')
#
#
# def main():
#     group_name = 'vvsu_dv'
#     get_wall_posts(group_name)
#
#
# if __name__ == '__main__':
#     main()