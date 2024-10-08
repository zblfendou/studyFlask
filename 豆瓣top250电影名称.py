from bs4 import BeautifulSoup
import requests

top250_movie_names = []

for start_num in range(0, 250, 25):
    response = requests.get(f'https://movie.douban.com/top250?start={start_num}', headers={
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'})
    if not response.ok:
        print('请求失败')

    soup = BeautifulSoup(response.text, 'html.parser')
    response.close()
    all_titles = soup.findAll('span', attrs={'class': 'title'})
    for movie in all_titles:
        movie_name = movie.string
        if '/' not in movie_name:
            top250_movie_names.append(movie_name)

print(top250_movie_names)
