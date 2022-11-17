from flask import Flask,render_template
import pip
pip.main(['install','requests'])
import requests
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Guessing Gender & Age"

@app.route("/guess/<name_grab>")
def guess(name_grab):
    response_gender=requests.get(f"https://api.genderize.io?name={name_grab}")
    data_gender=response_gender.json()
    gender_grab=data_gender["gender"]
    response_age=requests.get(f"https://api.agify.io?name={name_grab}")
    data_age=response_age.json()
    age_grab=data_age["age"]
    return render_template("index.html",name=name_grab,gender=gender_grab,age=age_grab)

@app.route("/blog")
def get_blog():
    blog_url=("https://api.npoint.io/c790b4d5cab58020d391")
    response=requests.get(blog_url)
    all_posts=response.json()
    return render_template("blog.html",posts=all_posts)

@app.route("/blog/<num>")
def each_blog(num):
    blog_url=("https://api.npoint.io/c790b4d5cab58020d391")
    response=requests.get(blog_url)
    all_posts=response.json()
    for post in all_posts:
        blog_id=post["id"]
        if blog_id==num:
            return post["body"]

if __name__=="__main__":
    app.run(debug=True)