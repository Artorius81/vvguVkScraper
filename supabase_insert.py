from dotenv import load_dotenv

load_dotenv()

from supabase import create_client, Client


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
        audio_title):
    url: str = "https://hgsbnelwjopuhevsglmm.supabase.co"
    key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imhnc2JuZWx3am9wdWhldnNnbG1tIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTQ3OTg3MTQsImV4cCI6MjAxMDM3NDcxNH0.lf5e52j7wKDwHe9p7wvAtiguW5OfOVigEa7irEMboIM"

    supabase: Client = create_client(url, key)

    data = supabase.table("postsvk").insert(
        {"created_at": f"{time}",
         "title": f"{text_title}",
         "text": f"{text}",
         "image": f"{image}",
         "doc": f"{doc}",
         "doc_title": f"{doc_title}",
         "link": f"{link}",
         "link_title": f"{link_title}",
         "audio": f"{audio}",
         "audio_artist": f"{audio_artist}",
         "audio_title": f"{audio_title}"}
    ).execute()
    assert len(data.data) > 0
