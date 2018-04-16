# coding:utf8
import pymysql


class save_mysql:
    def __init__(self):
        self.user = 'root'
        self.password = 'dong'
        self.host = 'localhost'
        self.database = 'Github'

    def save_issue_href(self, i, issue_id, issue_url, issue_title):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = "insert into issue_url(id,issue_id, issue_title,  issue_url, issue_state) " \
              "values(%s , %s, %s,%s, %s)"
        cursor.execute(sql, (i, issue_id, issue_title, issue_url, "open"))  # url插入到数据库中
        conn.commit()
        conn.close()

    def read_issue(self, id):
        conn = pymysql.connect(user=self.user, passwd=self.password,host=self.host,db=self.database,charset="utf8")
        cursor = conn.cursor()
        sql = "select issue_id,issue_title,issue_url,issue_state from issue_url where id=%s"%id
        cursor.execute(sql)
        issues_info = cursor.fetchall()
        conn.close()
        return issues_info

    def save_issue(self, num, issue_id, issue_state,
                   issue_title, issue_content,
                   issue_author, issue_time, issue_url):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = "insert into issue(id, issue_id, issue_state, " \
              "issue_title, issue_content, issue_author,issue_time,issue_url) " \
              "VALUE (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (num, issue_id, issue_state, issue_title,
                            issue_content, issue_author,issue_time,issue_url))
        conn.commit()
        conn.close()

    def read_issue_url(self):
        conn = pymysql.connect(user=self.user,passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = 'SELECT issue_url FROM issue'
        cursor.execute(sql)
        issue_urls = cursor.fetchall()
        conn.close()
        return issue_urls

    def save_commenter(self, c_id, name, data_time,iss_id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql ='INSERT INTO comment_p(id, name, data_time,iss_id) VALUE(%s,%s, %s, %s)'
        cursor.execute(sql,(c_id, name, data_time,iss_id))
        conn.commit()
        conn.close()

    def read_iss_title(self, id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = 'select issue_title from issue WHERE id=%s'
        cursor.execute(sql,id)
        title = cursor.fetchall()
        conn.close()
        return title

    def read_iss_content(self, id):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = 'select issue_content from issue WHERE id=%s'
        cursor.execute(sql, id)
        content = cursor.fetchall()
        conn.close()
        return content


    def sava_persion_info(self, following, language, data_count):
        conn = pymysql.connect(user=self.user, passwd=self.password, host=self.host, db=self.database, charset="utf8")
        cursor = conn.cursor()
        sql = ' INTO '