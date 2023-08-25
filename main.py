from flask import Flask,request,render_template,redirect
import os
user_data = {}
app = Flask(__name__)

@app.route('/')
def index():
        return render_template("admin.html",data={"reason":""})

@app.route("/<username>",methods=["GET"])
def protfolio(username):
      return render_template("portfolio.html",data = user_data[username])
      
@app.route("/portfolio", methods=['GET','POST'])
def admin():
    username = request.form.get("uname")
    try:  
        if user_data[username]==None and len(user_data[username]) == 0:     
            pass
        return render_template("admin.html", data={"success":False,"alert": True,"reason":"Username Already exists"})
    except:
          pass
    name = request.form.get("name")
    email = request.form.get("email")
    college = request.form.get("clg")
    language = request.form.get("lng")
    experience = request.form.get("year")
    about = request.form.get("abt")
    image = request.form.get("image")
    skill = [request.form.get("skill1"),
             request.form.get("skill2"),
             request.form.get("skill3"),
             request.form.get("skill4"),
             request.form.get("skill5")]
    linkedin = request.form.get("linkedin")
    github = request.form.get("github")
    instagram = request.form.get("insta")
    twitter = request.form.get("tweet")


    user_data[username] = {"username": username,
                                "name": name,
                                "email":email,
                                "college": college,
                                "lang": language,
                                "expe": experience,
                                "about":about,
                                "image":image,
                                "skill":skill,
                                "linkedin": linkedin,
                                "github": github,
                                "instagram": instagram,
                                "twitter": twitter
                                }
    # Adding data to a file
    filename = "data.txt"
    a_path = os.path.abspath(filename)
    w = open(f"{a_path}", "a")
    w.write(f"username: {username}\n data: {str(user_data[username])}]\n")
    w.close()
    return redirect(f"/{username}")    

app.run(debug=True)

# Removing data after shutting server
filename = "data.txt"
a_path = os.path.abspath(filename)
r = open(a_path, 'r+')
r.truncate(0)
r.close()