import requests
import urllib.parse

class Request:
    def __init__(self,method,args):
        self.args=args
        self.method=method

request = Request('GET',{'search':"Galvin"})

if request.method == 'GET':
    search=urllib.parse.quote(request.args.get('search'))
    url=f"https://www.googleapis.com/books/v1/volumes?q={search}&maxResults=5"
    response=requests.get(url)
    # print(response.json())

    if response.status_code==200:
        data=response.json()
        for item in data.get('items',[]):
            volume_info=item.get('volumeInfo',{})
            title=volume_info.get('title','N/A')
            publisher=volume_info.get('publisher','N/A')
            published_date=volume_info.get('publishedDate','N/A')
            author=volume_info.get('authors',['N/A'])
            rating=volume_info.get('averageRating',['N/A'])
            image_links=volume_info.get('imageLinks',{})
            image=image_links.get('thumbnail')  if 'thumbnail' in image_links else 'N/A'

            print(title)
            print(publisher)
            print(published_date)
            print(author)
            print(rating)
            print(image)
            