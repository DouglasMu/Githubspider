# coding:utf8
import requests
import re
from bs4 import BeautifulSoup
from spider import SQL


def read_info(url):
    content = requests.get(url=url, headers=headers)
    html = content.text
    soup = BeautifulSoup(html, "lxml")
    issue_time = soup.select(" div.TableObject-item.TableObject-item--primary > relative-time")
    issue_author = soup.select("div.timeline-comment-header.clearfix > h3 > strong > a")
    html1 = re.sub(r'\s+','', html)
    try:
        m = re.search(r'(<h3>IssueDescription</h3>'
                      r'|<h4>IssueDescription</h4>'
                      r'|<h4>Description</h4>|'
                      r'<h3>Description</h3>)((.)*?)</p>', html1)
        # print(m[0])
        m1 = re.search(r'<p>(.*?)</p>', m[0])
        print("描述是："+(str(m1[0])))
        print('时间是：'+issue_time[0].text)
        print('作者是:'+issue_author[0].text)

        return (issue_time[0].text, issue_author[0].text,str(m1[0]))

    except TypeError:
        print('时间是：' + issue_time[0].text)
        print('作者是:' + issue_author[0].text)
        return (issue_time[0].text, issue_author[0].text, 'null')
    # for iss1 in iss:
    #         print(iss1)
    #         if iss1 is "<h4>Issue Description</h4>":
    #             print(iss1)
if __name__=="__main__":
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) "
                             "Chrome/65.0.3325.146 Safari/537.36"}

    mysql = SQL.save_mysql()

    for i in range(1, 19):
        issues_info = mysql.read_issue(i)
        for issue_info in issues_info:
            # url = ("https://github.com"+link[0])
            # print(type(issue_info))
            # print(issue_info)
            issue_id = issue_info[0]
            issue_title = issue_info[1]
            issue_url = "https://github.com" + issue_info[2]
            issue_state = issue_info[3]
            print(issue_id, issue_title, issue_url, issue_state)
            (issue_time, issue_author, issue_content) = read_info(url=issue_url)
            # print(issue_time[0].get('datatime'),issue_author[0].text,issue_content)
            mysql.save_issue(issue_id,issue_state,issue_title,issue_content,issue_author,issue_time,issue_url)