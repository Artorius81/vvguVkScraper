from supabase import create_client


def sup_insert(
        time,
        text_title,
        text,
        image,
        doc,
        doc_title,
        link,
        link_title,
        audio,
        audio_artist,
        audio_title,
        video,
        video_title,
        video_date,
        video_presplash):

url = "https://hgsbnelwjopuhevsglmm.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhnc2JuZWx3am9wdWhldnNnbG1tIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY5NDc5ODcxNCwiZXhwIjoyMDEwMzc0NzE0fQ.l0LQs2V1serM8JomNcyYOtr5F56MHao0LivqJaJk6zg"

supabase = create_client(url, key)

data = (supabase.table("vkvvguposts")
        .insert(
    {"created_at": f"1111-11-11 11:11:11",
     "title": f"2",
     "text": f"2",
     "image": f"2",
     "doc": f"2",
     "doc_title": f"2",
     "link": f"2",
     "link_title": f"2",
     "audio": f"2",
     "audio_artist": f"2",
     "audio_title": f"2"}
)
        .execute())
assert len(data.data) > 0
