from flask import Flask,render_template,request
from jinja2 import Template
import sqlite3
app = Flask(__name__)





@app.route('/')
def render_login():
    return render_template('homepage.html')

@app.route('/home')
def render_home():
    return render_template('homepage.html')

@app.route('/infosys')
def render_infosys():
    return render_template('infosys.html')


@app.route('/microsoft')
def microsoft():
    return render_template('microsoft.html')

@app.route('/ibm')
def ibm():
    return render_template('ibm.html')


@app.route('/add_infosys')
def render_add_infosys():
    return render_template("infosys.html")


@app.route('/add_question_button', methods=['POST'])
def add_question_button():
    with sqlite3.connect("place.db") as conn:
        c = conn.cursor()

        qid = request.form.get("id")
        quest = request.form.get("questions")
        diff = request.form.get("difficultylevel")
        number = request.form.get("nooftimesasked")
        year = request.form.get("year")
        c.execute("""
                    INSERT INTO questions(q_id, question, dif_level,year,no_of_times) VALUES(?,?,?,?,?)
                    """, (qid,quest,diff,year,number))
        ques = c.execute("""SELECT * FROM QUESTIONS  """).fetchall()

        return render_template('viewquestion.html', questions=ques)

@app.route('/add_answers')
def render_ans():
    return render_template("answers.html")

@app.route('/add_answers_button', methods=['POST'])
def add_answers_button():
    with sqlite3.connect("place.db") as conn:
        c = conn.cursor()

        answerid = request.form.get("ansid")
        answr = request.form.get("answer")
        qid = request.form.get("id")
        # ssn = request.form.get("ssn")
        print(qid)
        c.execute("""
                    INSERT INTO answers(ans_id,solution,q_id) VALUES(?,?,?)
                    """, (answerid,answr,qid))
        ans=c.execute("""SELECT * FROM ANSWERS """).fetchall()
        return render_template('viewanswer.html',answers=ans)

@app.route('/questionanswers', methods=['GET'])
def view_questions_button():
    with sqlite3.connect("place.db") as conn:
        c = conn.cursor()
        qa = c.execute("""SELECT Q.*,A.* FROM QUESTIONS Q,ANSWERS A 
            WHERE Q.q_id=A.q_id""").fetchall()

        return render_template('questionanswers.html', questions=qa)
        



@app.route('/view_question', methods=['POST'])
def view_question():
    with sqlite3.connect("place.db") as conn:
        c = conn.cursor()
        questions=c.execute("""SELECT * FROM questions """).fetchall()
        return render_template("viewquestion.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True) 

