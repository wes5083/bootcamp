from flask import Flask, render_template, request, redirect, Response
import pymysql.cursors
import pymysql
import random

app = Flask(__name__)

correct = 0

@app.route("/api/guessStart", methods=["GET", "POST"])
def guess_start():
    correct = random.randint(1,20)
    print(correct)
    json = '{"status":"Game started."}'
    return Response(json, mimetype="application/json")


@app.route("/api/guessCheck",methods=["GET"])
def guess_check():
    guess = int(request.args.get("guess",0))
    print(guess)
    statusText = ""
    if guess == correct:
        statusText = "Correct! You win the game!"
    elif guess < correct:
        statusText = "The correct number is larger."
    else:
        statusText = "The correct number is smaller."
    json = '{ "guess": "' + str(guess) + '", "status": "' + statusText + '" }'
    return Response(json, mimetype='application/json')


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
