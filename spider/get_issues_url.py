import requests
import re
import spider.SQL
from bs4 import BeautifulSoup
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                        "AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/65.0.3325.146 Safari/537.36"}


def get_url(url):
    html = requests.get(url, headers=headers)
    content = html.text
    html.close()
    return content


def save_issue_href(i, open_url1):
    content1 = get_url(open_url1)
    soup = BeautifulSoup(content1, 'lxml')
    issue_hrefs = soup.findAll("a", class_="link-gray-dark v-align-middle no-underline h4 js-navigation-open")
    sql = spider.SQL.save_mysql()

    for issue_href in issue_hrefs:
        issue_url = issue_href.get('href')
        issue_title1 = issue_href.text
        try:
            # python UCS-4 build的处理方式
            highpoints = re.compile(u'[\U00010000-\U0010ffff]')
        except re.error:
            # python UCS-2 build的处理方式
            highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
        issue_title = highpoints.sub(u'', issue_title1)  # 过滤掉表情
        issue_id = re.sub("\D", "", issue_url)
        print(issue_id)
        print(issue_url)
        print(issue_title)
        sql.save_issue_href(i, issue_id, issue_url, issue_title, )
        i += 1
    return i


if __name__ == "__main__":
#   1-8
    id = 12076
    for page in range(8, 9):
        close_url = "https://github.com/freeCodeCamp/freeCodeCamp/issues?page="+str(page)+"&q=is%3Aissue+is%3Aclosed"
        open_url = ("https://github.com/freeCodeCamp/freeCodeCamp/issues?page=" + str(page) + "&q=is%3Aopen")
        print(open_url)
        id = save_issue_href(id, open_url)

