# Flaskを使って現在時刻を表示する
from flask import Flask
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    dt = datetime.datetime.now()
    html = "<!DOCTYPE html>"
    html += "<html>"
    html += "<head><title>Flask Sample</title></head>"
    html += "<body>"
    html += f"{dt.year}年{dt.month}月{dt.day}日 {dt.hour}時{dt.minute}分{dt.second}秒です"
    html += "</body></html>"
    return html


if __name__ == "__main__":
    app.run()
