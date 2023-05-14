from flask import Flask, render_template, request
import pymysql.cursors
import pymysql

app = Flask(__name__)


@app.route("/users/add", methods=["GET", "POST"])
def users_add():
    if request.method == "GET":
        return render_template("users_add.html")
    print(request.form)
    username = request.form.get("user");
    pwd = request.form.get("pwd");
    mobile = request.form.get("mobile");

    # operate mysql
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='123456', db='python_demo', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "insert into  t_users(name, pwd, mobile) values(%s, %s,%s)"
    cursor.execute(sql, [username, pwd, mobile])

    conn.commit()
    cursor.close()
    conn.close()
    return "success"


@app.route("/users/list")
def users_list():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='123456', db='python_demo', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from t_users"
    cursor.execute(sql)
    data_list = cursor.fetchall();

    cursor.close()
    conn.close()

    print(data_list)
    return render_template("users_list.html", data_list=data_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='8000')
