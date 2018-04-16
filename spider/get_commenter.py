from spider import SQL
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/65.0.3325.146 Safari/537.36"}
sq = SQL.save_mysql()


def get_comment(url1, num):
    html = requests.get(url=url1, headers=headers)
    content = html.text
    soup = BeautifulSoup(content, 'lxml')
    # comment = soup.find_all('td', class_='d-block comment-body markdown-body js-comment-body')
    # print(comment)
    # persons = soup.find_all('a', class_='author text-inherit')
    ll = soup.select('div.timeline-comment-header.clearfix > h3')
    iss_id = str(url1).split('/')
    for i in ll:
        # print(i)
        print(i.find('a').text)
        print(i.find('a', class_='timestamp').text)
        name = i.find('a').text
        time = i.find('a', class_='timestamp').text
        sq.save_commenter(int(num), name, str(time).replace(',', ''),iss_id[-1])
        num += 1
    return num
# d - block comment - body markdown - body js - comment - body


if __name__ == '__main__':
    # get_comment('https://github.com/freeCodeCamp/freeCodeCamp/issue_urls/17038')
    urls = sq.read_issue_url()
    c_id = 1
    for url in urls:
        print(url[0])
        c_id = get_comment(url[0], c_id)
