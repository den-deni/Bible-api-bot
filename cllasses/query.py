import requests

from config import BIBLE_KEY, BIBLE_ID, BIBLE_URL


class SearchQuery:
    def __init__(self):
        self.bible_id = BIBLE_ID
        self.url = BIBLE_URL

    def get_data(self, query: str):
        url = self.url + f'/v1/bibles/{self.bible_id}/search?query={query}&sort=relevance'
        response = requests.get(url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']['verses']
        list_name = []
        list_verses = []
        for item in content:
            name = item.get('reference')
            list_name.append(name)
            book = item.get('text')
            list_verses.append(book)
        text_name = '\n'.join(list_name)
        text = '\n'.join(list_verses)
        return f'{text}\n{text_name}'

    def get_right(self):
        url = self.url + (f'/v1/bibles/{BIBLE_ID}/verses/MAT.1.3?content-type=json&include-notes=false&include'
                          f'-titles=true&include-chapter-numbers=false&include-verse-numbers=true&include'
                          f'-verse-spans=false&use-org-id=false')
        response = requests.get(url, headers=BIBLE_KEY)
        data = response.json()
        content = data['data']['copyright']
        return content
