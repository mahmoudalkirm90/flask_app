from flask import Flask , render_template , request , url_for
app = Flask(__name__) 
from DB import DB
import json

# data base implementation
db = DB('codes.db')
db.create_table('codes(code varchar(8) , site varchar(15) , is_active boolean DEFAULT 1)')

@app.route("/")
def home():
     return render_template('index.html' , title = 'Flask')

@app.route('/check_code' , methods = ['POST'])
def check_code():
     code = request.get_json() 
     print(code)
     return json.dumps({'code':code['code'],'is_active':True})

if __name__ == "__main__":
    app.run()   