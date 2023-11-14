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
                    else:
                        sizes = attachment['photo']['sizes']
                        for size in sizes:
                            if size['type'] == 'z':  # берём лучшее качество
                                post_photos.append(size['url'])
                                # post_photo = size['url']

                #  проверка есть ли прикрепленные документы
                elif attachment['type'] == 'doc':
                    doc_title = attachment['doc']['title']
                    docs.append(doc_title)
                    doc_url = attachment['doc']['url']
                    docs.append(doc_url)

                #  проверка есть ли прикреплённые ссылки
                elif attachment['type'] == 'link':
                    link_title = attachment['link']['title']
                    links.append(link_title)
                    link_url = attachment['link']['url']
                    links.append(link_url)

                #  проверка есть ли прикреплённые аудио
                elif attachment['type'] == 'audio':
                    audio_artist = attachment['audio']['artist']
                    audios.append(audio_artist)
                    audio_title = attachment['audio']['title']
                    audios.append(audio_title)
                    audio_url = attachment['audio']['url']
                    audios.append(audio_url)

                # проверка есть ли видео в посте
                elif attachment['type'] == 'video':
                    video_access_key = attachment['video']['access_key']
                    video_post_id = attachment['video']['id']
                    video_owner_id = attachment['video']['owner_id']

                    video_get_url = f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.137'
                    req = requests.get(video_get_url)
                    res = req.json()
                    video_title = res['response']['items'][0]['title']
                    videos.append(video_title)
                    video_date = res['response']['items'][0]['date']
                    video_date = datetime.fromtimestamp(video_date)
                    videos.append(video_date)
                    video_url = res['response']['items'][0]['player']
                    videos.append(video_url)

                    for item in res['response']['items'][0]['image']:
                        if (item['width'] and item['height']) == (
                                res['response']['items'][0]['width'] and res['response']['items'][0][
                            'height']):
                            video_presplash = item['url']
                            videos.append(video_presplash)
            # print("Photos:", post_photos)
            # print("Docs:", docs)
            # print("Links:", links)
            # print("Audios:", audios)
            # print("Videos:", videos)
        table_data = (supabase.table("vkvvguposts")
                      .insert(
            {"created_at": f"{post_date}",
             "title": f"{post_text}",
             "text": f"{post_text}",
             "image": f"{post_photos}",
             "docs": f"{docs}",
             "links": f"{links}",
             "audios": f"{audios}",
             "videos": f"{videos}",
             }
        )
                      .execute())
        assert len(table_data.data) > 0
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
                    else:  # если несколько фото
                        sizes = attachment['photo']['sizes']
                        for size in sizes:
                            if size['type'] == 'z':  # берём лучшее качество
                                post_photos.append(size['url'])
                                # post_photo = size['url']

                #  проверка есть ли прикреплённые ссылки
                elif attachment['type'] == 'doc':
                    doc_title = attachment['doc']['title']
                    docs.append(doc_title)
                    doc_url = attachment['doc']['url']
                    docs.append(doc_url)

                #  проверка есть ли прикреплённые ссылки
                elif attachment['type'] == 'link':
                    link_title = attachment['link']['title']
                    links.append(link_title)
                    link_url = attachment['link']['url']
                    links.append(link_url)

                #  проверка есть ли прикреплённые аудио
                elif attachment['type'] == 'audio':
                    audio_artist = attachment['audio']['artist']
                    audios.append(audio_artist)
                    audio_title = attachment['audio']['title']
                    audios.append(audio_title)
                    audio_url = attachment['audio']['url']
                    audios.append(audio_url)

                #  проверка есть ли видео в посте
                elif attachment['type'] == 'video':
                    video_access_key = attachment['video']['access_key']
                    video_post_id = attachment['video']['id']
                    video_owner_id = attachment['video']['owner_id']

                    video_get_url = f'https://api.vk.com/method/video.get?videos={video_owner_id}_{video_post_id}_{video_access_key}&access_token={token}&v=5.137'
                    req = requests.get(video_get_url)
                    res = req.json()
                    video_title = res['response']['items'][0]['title']
                    videos.append(video_title)
                    video_date = res['response']['items'][0]['date']
                    video_date = datetime.fromtimestamp(video_date)
                    videos.append(video_date)
                    video_url = res['response']['items'][0]['player']
                    videos.append(video_url)

                    for item in res['response']['items'][0]['image']:
                        if (item['width'] and item['height']) == (
                                res['response']['items'][0]['width'] and res['response']['items'][0][
                            'height']):
                            video_presplash = item['url']
                            videos.append(video_presplash)
            # print("Photos:", post_photos)
            # print("Docs:", docs)
            # print("Links:", links)
            # print("Audios:", audios)
            # print("Videos:", videos)
        table_data = (supabase.table("vkvvguposts")
                      .insert(
            {"created_at": f"{post_date}",
             "title": f"{post_text}",
             "text": f"{post_text}",
             "image": f"{post_photos}",
             "docs": f"{docs}",
             "links": f"{links}",
             "audios": f"{audios}",
             "videos": f"{videos}",
             }
        )
                      .execute())
        assert len(table_data.data) > 0
except Exception:
    print('Что-то пошло не так.')