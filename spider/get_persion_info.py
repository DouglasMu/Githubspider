# coding: utf8

import re
import requests
import json
from bs4 import BeautifulSoup


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/65.0.3325.146 Safari/537.36"}


# 获取github的个人following个数
def get_person_follow(name):
    url = 'https://api.github.com/users' + name
    html = requests.get(url=url, headers=headers)
    content = html.text
    info_dic = json.loads(content)
    html.close()
    return info_dic['followers']


# 获取github的个人代码语言
def get_person_rep(name):
    language = {}
    url = 'https://github.com'+name+'?tab=repositories'
    print(url)
    html = requests.get(url=url, headers=headers)
    content = html.text
    soup = BeautifulSoup(content, 'lxml')
    content_list = soup.findAll('span', itemprop='programmingLanguage')
    # print(content_list)
    for i in content_list:
        lang = i.text
        lang = lang.replace('\t', '').replace("\n", "").replace(' ', '')
        if lang not in language:
            language[lang] = 1
        else:
            language[lang] += 1
    html.close()
    return language


# 获取github的个人datacount（每日的提交数量）
# 最近5周
def get_data_count(name):
    url = 'https://github.com'+name
    html = requests.get(url=url, headers=headers)
    content = html.text
    soup = BeautifulSoup(content, 'lxml')
    data_count = []

    data_count_1 = soup.find('g', transform="translate(676, 0)")
    for i in data_count_1:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))


    data_count_2 = soup.find('g', transform="translate(663, 0)")
    for i in data_count_2:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))


    data_count_3 = soup.find('g', transform="translate(650, 0)")
    for i in data_count_3:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))


    data_count_4 = soup.find('g', transform="translate(637, 0)")
    for i in data_count_4:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))


    data_count_5 = soup.find('g', transform="translate(624, 0)")
    for i in data_count_5:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))


    data_count_6 = soup.find('g', transform="translate(611, 0)")
    for i in data_count_6:
        count_list = str(i).split(' ')
        for key, ii in enumerate(count_list):
            if key is 2:
                # print(re.sub("\D", "", ii))
                data_count_c = re.sub("\D", "", ii)
                data_count.append(int(data_count_c))

    print(data_count)
    return data_count


# 测试用 主函数
if __name__ == "__main__":
    num = get_person_follow('/7sDream')
    print(num)
    lang_dic = get_person_rep('/7sDream')
    print(lang_dic)
    count = get_data_count('/7sDream')
    print(sum(count))
