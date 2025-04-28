def individual_serial(article) -> dict:
    return {
        "id": int(article["_id"]),
        "title" : article["_title"],
        "name": article["_name"],
        "date": article["_date"],
    }

def list_serial(articles) -> list:
    return [individual_serial(article) for article in articles]