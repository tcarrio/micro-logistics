from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
import MySQLdb

app = Flask(__name__)
_session = {}
db = MySQLdb.connect(
    host='cse345.carrio.me',
    user='tlcarrio',
    passwd='By$RLLupf#',
    db='project'
)
cur = db.cursor()

@app.route("/")
def index():
    global _session
    if(_session.has_key('authenticated')):
        return render_template('home.html')
    else:
        # not logged in, show login page
        return render_template('welcome.html')

@app.route("/login", methods=['POST'])
def login(customer=None,password=None):
    global _session
    # check database for customerID
    if(user_in_db(customer)==None):
        return render_template('error.html',error='Incorrect login information')
    else:
        # set _session variables
        _session['authenticated']=True
        return redirect(url_for('home'))

@app.route("/home")
def home():
    global _session
    auth_check = check_authenticated()
    if(auth_check):
        return auth_check
    # continue on if authenticated
    return render_template('home.html')
        

@app.route("/packages")
@app.route("/packages/<packgeID>")
def packages(packageID=None):
    global _session
    auth_check = check_authenticated()
    if(auth_check):
        return auth_check
    # continue on if authenticated
    if(packageID==None):
        customer_packages=get_customer_packages() # use _session['customerID']
        return render_template('packages.html',packages=customer_packages)
    else:
        tracking_info=get_specific_package() # use given packageID
        return render_template('packages.html',tracking=tracking_info)

@app.route("/about")
def about():
    return render_template('about.html')



def get_customer_packages(packageID=None):
    return []

def user_in_db(c):
    return True

def check_authenticated():
    global _session
    if not _session.has_key('authenticated'):
        return redirect(url_for('login'))