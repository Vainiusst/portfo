from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('./index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


def write_to_txt(dict):
    with open('database.txt', mode='a', encoding='UTF-8') as db:
        email = dict['email']
        subj = dict['subject']
        mess = dict['message']
        txt = db.write(f"\n{email},{subj},{mess}")


def write_to_csv(dict):
    with open('database.csv', newline='', mode='a', encoding='UTF-8') as db2:
        email = dict['email']
        subj = dict['subject']
        mess = dict['message']
        csv_writer = csv.writer(db2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subj,mess])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('./thank_you.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong, try again'

# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
