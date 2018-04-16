# coding:utf8
import requests
import re
from bs4 import BeautifulSoup
from spider import SQL


def read_info(url):
    try:
        content = requests.get(url=url, headers=headers, timeout=100)
    except:
        content = requests.get(url=url, headers=headers)
    html = content.text
    soup = BeautifulSoup(html, "lxml")
    issue_time = soup.select(" div.TableObject-item.TableObject-item--primary > relative-time")
    issue_author = soup.select("div.timeline-comment-header.clearfix > h3 > strong > a")
    html1 = re.sub(r'\s+', '', html)
    try:
        m = re.search(r'(<h3>IssueDescription</h3>'
                      r'|<h4>IssueDescription</h4>'
                      r'|<h4>Description</h4>|'
                      r'<h3>Description</h3>)((.)*?)</p>', html1)
        # print(m[0])
        m1 = re.search(r'<p>(.*?)</p>',m[0])
        print("描述是："+(str(m1[0])))
        print('时间是：'+issue_time[0].text)
        print('作者是:'+issue_author[0].text)
        return (issue_time[0].text, issue_author[0].text,str(m1[0]))
    except IndexError:
        return ('null', issue_author[0].text, 'null')
    except TypeError:
        print('时间是：' + issue_time[0].text)
        print('作者是:' + issue_author[0].text)
        return (issue_time[0].text, issue_author[0].text, 'null')


if __name__ == "__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/65.0.3325.146 Safari/537.36"}
    num = 11908
    mysql = SQL.save_mysql()
    try:
        # python UCS-4 build的处理方式
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        # python UCS-2 build的处理方式
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    for i in range(11908, 12097):
        issues_info = mysql.read_issue(i)
        for issue_info in issues_info:
            issue_id = issue_info[0]
            issue_title = issue_info[1]
            issue_url = "https://github.com" + issue_info[2]
            issue_state = issue_info[3]
            print(issue_id, issue_title, issue_url, issue_state)
            (issue_time, issue_author, issue_content1) = read_info(url=issue_url)
            issue_content = highpoints.sub(u'', issue_content1)  # 过滤掉表情
            mysql.save_issue(num, issue_id, issue_state, str(issue_title), issue_content,
                             issue_author, issue_time, issue_url)
            num += 1
