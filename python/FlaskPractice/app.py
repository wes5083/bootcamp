from flask import Flask, render_template, request, redirect
import pymysql.cursors
import pymysql

app = Flask(__name__)


@app.route("/numbers/operate")
def numbers_operate():
    return render_template("numbers_guess.html")


@app.route("/numbers/generate", methods=["POST"])
def numbers_generate():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='123456', db='python_demo', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql_del = "delete from t_numbers "
    cursor.execute(sql_del)
    conn.commit()

    sql_add = "insert into t_numbers(number_value) values(%s)"
    generate_number = request.form.get("generate_number")
    cursor.execute(sql_add, [generate_number])
    conn.commit()
    cursor.close()
    conn.close()
    return redirect("/numbers/operate")


@app.route("/numbers/guess", methods=["POST"])
def numbers_guess():
    conn = pymysql.connect(host="127.0.0.1", port=3306, user='root', passwd='123456', db='python_demo', charset='utf8')
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "select * from t_numbers order by id desc"
    cursor.execute(sql)
    data = cursor.fetchone()
    cursor.close()
    conn.close()
    db_num = int(data["number_value"])
    guess_num = int(request.form.get("guess_number"))
    if db_num == guess_num:
        return "Success"
    elif db_num > guess_num:
        return "Smaller"
    else:
        return "Bigger"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='8001')
