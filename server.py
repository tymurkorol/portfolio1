from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template("index.html") #file must be in templates folder
#take each html file from folder templates and give the name of this file as path
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_database(data):
    with open("database.txt", mode="a") as database: # a mode allows us to append something to document
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        database.write(f"\n{email}, {subject}, {message}") #write method takes only 1 argument, so we use string format to ad data to file

def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database2: # a mode allows us to append something to document
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        # write_to_database(data)
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "Something went wrong, try again!"

