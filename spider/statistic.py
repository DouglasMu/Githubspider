# coding: utf8
from spider import SQL
from nltk.corpus import stopwords
import nltk
import string


def get_t_c(iss_id):
    sql = SQL.save_mysql()
    title = str(sql.read_iss_title(iss_id)[0][0]).replace('\n', '')
    content = sql.read_iss_content(iss_id)[0][0]
    return title, content


# 分词
def word_token(sent):  # 将单句字符串分割成词
    result = ''
    words_instr = nltk.word_tokenize(sent)
    return words_instr


# 去停用词小写去短词
def clean_words(words_instr):
    clean_words1 = []
    stop_words = list(stopwords.words('english'))
    stop_words = list(string.punctuation)+stop_words
    # print(stop_words)
    for words in words_instr:
        if words not in stop_words:
            clean_words1.append(words.lower())
    return clean_words1


if __name__ == '__main__':
    t, c = get_t_c(1)
    print(t, c)
    disease_list1 = nltk.word_tokenize(t)
    if not str(c).__eq__('null'):
        disease_list2 = nltk.word_tokenize(c)
        print(disease_list2)
    print(disease_list1)
    ee = clean_words(disease_list1)
    print(ee)

