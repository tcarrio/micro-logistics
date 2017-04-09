from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
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
def root():
    global _session
    return redirect(url_for('index'))

@app.route("/index")
def index():
    global _session
    if(_session.has_key('authenticated')):
        return render_template('home.html',sesh=_session)
    else:
        # not logged in, show login page
        return render_template('welcome.html',sesh=_session)

@app.route("/login", methods=['POST'])
def login():
    global _session
    # check database for customerID
    customer=request.args.get('login')
    if(customer!="" and user_in_db(customer)):
        # set _session variables
        _session['authenticated']=True
        return redirect(url_for('home'))        
    else:
        return render_template('error.html',error='Incorrect login information',sesh=_session)

@app.route("/home")
def home():
    global _session
    auth_check = check_authenticated()
    if(auth_check):
        return auth_check
    # continue on if authenticated
    return render_template('home.html',sesh=_session)

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
        return render_template('packages.html',packages=customer_packages,sesh=_session)
    else:
        tracking_info=get_specific_package() # use given packageID
        return render_template('packages.html',tracking=tracking_info,sesh=_session)

@app.route("/about")
def about():
    return render_template('about.html',sesh=_session)

@app.route("/logout")
def logout():
    global _session
    _session = {}
    return redirect(url_for('index'))

def get_customer_packages(packageID=None):
    return []

def user_in_db(c):
    return True

def check_authenticated():
    global _session
    if not _session.has_key('authenticated'):
        return redirect(url_for('index'))