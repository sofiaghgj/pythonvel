from flask import Flask
from utils import *

app = Flask(__name__)

@app.route("/")
def page_index():
    return main(load_candidates())

@app.route("/candidates/<int:x>")
def page_can(x):
    candi = get_by_pk(x)
    url = "http://mypictures.me/200"
    inform = f'<img src="{candi["picture"]}">\n<pre>Имя кандидата - {candi["name"]}\nПозиция кандидата - {candi["position"]}\nНавыки - {candi["skills"]}</pre>\n'
    return inform

@app.route("/skills/<x>")
def skills(x):
        skill = get_by_skill(x)
        text = ''
        for i in skill:
            text += f'<pre>Имя кандидата - {i["name"]}\n{i["position"]}\n{i["skills"]}'
        return text

app.run()









