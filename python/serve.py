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
    customer = request.form.get('customerID')
    print(customer)
    if(customer and db_authenticate_customer(customer)):
        # set _session variables
        return redirect(url_for('home'))
    else:
        return render_template('welcome.html',error='Incorrect login information',sesh=_session)

@app.route("/home")
def home():
    global _session
    auth_check = check_authenticated()
    if(auth_check):
        return auth_check
    # continue on if authenticated
    return render_template('home.html',sesh=_session)

@app.route("/packages/")
@app.route("/packages/<packageID>")
def packages(packageID=None):
    global _session
    auth_check = check_authenticated()
    if(auth_check):
        return auth_check
    # continue on if authenticated
    if(packageID==None):
        customer_packages=db_get_customer_packages(_session['customerID']) # use _session['customerID']
        return render_template('packages.html',packages=customer_packages,sesh=_session)
    else:
        tracking_info=db_get_specific_package(packageID) # use given packageID
        return render_template('packages.html',tracking=tracking_info,sesh=_session)

@app.route("/about")
def about():
    return render_template('about.html',sesh=_session)

@app.route("/logout")
def logout():
    global _session
    _session = {}
    return redirect(url_for('index'))

@app.route("/user")
def settings():
    global _session
    credit = db_get_credit_for(_session['customerID'])
    account = db_get_account_for(_session['customerID'])
    return render_template('user.html',credit=credit,account=account,sesh=_session)

def db_get_credit_for(id):
    global cur
    cred = []
    if(id):
        cur.execute("""select c.cardNum,c.expDate,v.vendorName,a.fullName,a.addressLine1,a.addressLine2,a.city,
            a.state,a.zipcode,a.country,a.phoneNumber from Credit c join CardVendor v on c.vendor = v.vendorID
            join Address a on a.addressId = c.billAddress where c.customerId = %s;""" % id)
        for c in cur.fetchall():
            tmp_card={}
            tmp_card['cardNum']="X"*12+c[0][-4:]
            tmp_card['expDate']=c[1]
            tmp_card['vendor']=c[2]
            tmp_card['fullName']=c[3]
            tmp_card['addr1']=c[4]
            tmp_card['addr2']=c[5]
            tmp_card['city']=c[6]
            tmp_card['state']=c[7]
            tmp_card['zipcode']=c[8]
            tmp_card['country']=c[9]
            tmp_card['phone']=phone_number_formatted(c[10])
            cred.append(tmp_card)
        for line in c:
            print(line)
    return cred

def db_get_account_for(id):
    global cur
    acct = []
    if(id):
        cur.execute("""select ac.accountNum,ac.balance,ba.fullName,ba.addressLine1,ba.addressLine2,ba.city,
            ba.state,ba.zipcode,ba.country,ba.phoneNumber,sa.fullName,sa.addressLine1,sa.addressLine2,
            sa.city,sa.state,sa.zipcode,sa.country,sa.phoneNumber from Account ac 
            join Address ba on ac.billAddress = ba.addressID 
            join Address sa on ac.shipAddress = sa.addressID
            where ac.customerID = %s""" % id)
        for line in cur.fetchall():
            a={}
            a['misc']={}
            a['bill']={}
            a['ship']={}
            a['misc']['accountNum']=line[0]
            a['misc']['balance']=line[1]            
            a['bill']['fullName']=line[2]
            a['bill']['addr1']=line[3]
            a['bill']['addr2']=line[4]
            a['bill']['city']=line[5]
            a['bill']['state']=line[6]
            a['bill']['zipcode']=line[7]
            a['bill']['country']=line[8]
            a['bill']['phone']=phone_number_formatted(line[9])
            a['ship']['fullName']=line[10]
            a['ship']['addr1']=line[11]
            a['ship']['addr2']=line[12]
            a['ship']['city']=line[13]
            a['ship']['state']=line[14]
            a['ship']['zipcode']=line[15]
            a['ship']['country']=line[16]
            a['ship']['phone']=phone_number_formatted(line[17])
            acct.append(a)
        return acct

def db_get_customer_packages(id=None):
    global cur
    list_of_packages = []
    if(id):
        cur.execute("SELECT * FROM Package WHERE customerID = %s" % id)
        for row in cur.fetchall():
            p = {}
            p['id']=row[0]
            p['width']=row[1]
            p['length']=row[2]
            p['height']=row[3]
            p['weight']=weight_by_pounds(row[4])
            p['hazardous'] = 'Yes' if(row[5]) else 'No'
            p['international'] = 'Yes' if(row[6]) else 'No'
            p['destination']=db_get_location_by_id(row[7])
            list_of_packages.append(p)
        for l in list_of_packages:
            print(l)
    return list_of_packages

def db_get_specific_package(package=None):
    global cur
    list_of_tracking_info = []
    if(package):
        q = "SELECT * FROM Tracking WHERE packageID = %s;" % package
        print(q)
        cur.execute(q)
        for row in cur.fetchall():
            t = {}
            t['trackID']=row[0]
            t['location']=row[1]
            t['lastUpdate']=row[2]
            t['status']=db_get_status_for(row[3])
            t['packageID']=row[4]
            list_of_tracking_info.append(t)
        for l in list_of_tracking_info:
            print(l)
    return list_of_tracking_info

def db_get_status_for(code):
    global cur
    stat = code
    if(code):
        cur.execute("SELECT statusDescription FROM Status WHERE statusID = %s" % code)
        stat = cur.fetchone()[0]
    return stat

def db_get_location_by_id(id):
    global cur
    loc = str(id)
    if(id):
        cur.execute("select city,state,country from Address where addressID = %s" % id)
        loc_list = cur.fetchone()
        if(loc_list):
            loc = ", ".join(loc_list)
    return loc

def db_authenticate_customer(id,password=None):
    global cur
    global _session
    if(id):
        cur.execute("SELECT * FROM Customer WHERE customerID = %s;" % id)
        cust = cur.fetchone()
        print(cust)
        if(cust != None):
            _session['authenticated'] = True
            _session['customerID'] = cust[0]
            _session['fName'] = cust[1]
            _session['lName'] = cust[2]
            return True
    _session = {}
    return False

def phone_number_formatted(p):
    return "(%s)-%s-%s" % (p[:3],p[3:6],p[6:])

def weight_by_pounds(ounces=0):
    return "%.2f" % (ounces / 16.0)

def check_authenticated():
    global _session
    if not _session.has_key('authenticated'):
        return redirect(url_for('index'))