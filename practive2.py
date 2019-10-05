import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('127.0.0.1', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta                      # 'dbsparta'라는 이름의 db를 만듭니다.

# URL을 읽어서 HTML를 받아오고,
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20190909',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
#soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
#movies = soup.select('#old_content > table > tbody > tr')

# movies (tr들) 의 반복문을 돌리기
# rank = 1
# for movie in movies:
    # movie 안에 a 가 있으면,
#    a_tag = movie.select_one('td.title > div > a')
#    if not a_tag == None:
#        title = a_tag.text
#        star = movie.select_one('td.point').text
#        db.movies.insert_one({'Rank': rank, 'Title': title, 'Star': star})
#        rank += 1

target_movie = db.movies.find_one({'Title':'사운드 오브 뮤직'})
target_star = target_movie['Star']

db.movies.update_many({'Star':'9.39'},{'$set':{'Star':0}})
shit_list = list(db.movie.find({'Star':'0'}))
print(shit_list)