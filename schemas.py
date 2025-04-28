def individual_serial(article) -> dict:
    return {
        "id": str(article["_id"]),
        "title" : article["title"],
        "description": article["description"],
        "date": article["date"],
    }

def list_serial(articles) -> list:
    return [individual_serial(article) for article in articles]