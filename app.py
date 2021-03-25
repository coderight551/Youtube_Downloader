from flask import Flask, render_template, request,send_file
from pytube import YouTube
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/download',methods=['GET','POST'])
def download():
    link = request.form['queries']
    video = YouTube(link)
    stream = video.streams.get_highest_resolution()
    filename = stream.title
    stream.download(output_path="D:\Downloads")
    filename = filename+".mp4"
    filename = filename.replace("|","")
    return send_file(os.path.join("D:\Downloads\\", filename), as_attachment=True)
    

if __name__ == '__main__':
    app.run(debug=True)
