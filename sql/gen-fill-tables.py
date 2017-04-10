from random import randint
from random import randrange
from datetime import timedelta
from datetime import datetime

### SAMPLE DATA
firstNames = [ 
    "Modesta", "Rosaura", "Shana", "Daniela", "Mozella", "Romona",
    "Cayla", "Kirstin", "Florentino", "Dionne", "Susanne", "Heath",
    "Coretta", "Mee", "Lona", "Parthenia", "Joaquina", "Reyna",
    "Haley", "Sheridan", "Alton", "Milda", "Cherelle", "Alvaro",
    "Wilfred", "Estela", "Vennie", "Patrick", "Latoria", "Ada",
    "Dennis", "Chantell", "Devin", "Brice", "Felicita", "Lila",
    "Dudley", "Kina", "Lyla", "Sau", "Lamar", "Madalene",
    "Werner", "Barbie", "Norbert", "Venetta", "Roselia", "Natalie",
    "Lessie", "Gabriele", "Julianne", "Thao", "Dusty", "Nickolas",
    "Karie", "Sam", "Alita", "Willard", "Frederic", "Else",
    "Delicia", "Piedad", "Lou", "Chaya", "Bobbi", "Bebe",
    "Harley", "Susie", "Myron", "Julieann", "Robbie", "Stephane",
    "Ying", "Ollie", "Georgianna", "Bree", "Grisel", "Mariann",
    "Mathilde", "Colette", "Michell", "Annalisa", "Leandra", "Jaimie",
    "Raisa", "Dulce", "Nannie", "Iluminada", "Larue", "Helaine",
    "Horace", "Otis", "Elyse", "Maximina", "Floyd", "Robbi",
    "Dorcas", "Iola", "Val", "Devin" ]
lastNames = [
    "Schaner", "Storck", "Schuetz", "Heinrich", "Gram", "Osmond", 
    "Petro", "Delahoussaye", "Corter", "Wiedman", "Cokley", "Toppin",
    "Shevlin", "Dorough", "Lamont", "Sable", "Pantaleo", "Thorson",
    "Serpa", "Dewoody", "Overholt", "Buehler", "Cousin", "Selander",
    "Deveau", "Milone", "Bevilacqua", "Onofrio", "Suire", "Rickards",
    "Mortensen", "Dodds", "Mckelvy", "Gossman", "Dison", "Lafayette",
    "Capel", "Gobert", "Davisson", "Ohagan", "Aurand", "Proulx",
    "Cottman", "Hohman", "Worthley", "Honore", "Barras", "Durr",
    "Neely", "Selleck", "Speakman", "Seelig", "Kaul", "Balser",
    "Mendiola", "Linton", "Dery", "Stults", "Steller", "Simonetti",
    "Pitman", "Shanahan", "Pang", "Pasch", "Dickson", "Pflug",
    "Kaye", "Gambrell", "Kissner", "Gillard", "Jefcoat", "Patlan",
    "Mastro", "Jemison", "Schor", "Tseng", "Stinnett", "Ditullio",
    "Hague", "Astle", "Blanding", "Meaney", "Dunavant", "Round",
    "Palmateer", "Hawthorn", "Schacherer", "Mong", "Poss", "Notter",
    "Elsner", "Fiorentino", "Heston", "Vann", "Arends", "Stotz",
    "Ducksworth", "Wooldridge", "Nicola", "Swinney" ]
VendorList = [ "Visa", "Mastercard", "American Express",
    "Capitol One", "Discover", "Citi" ]
Streets = [ "E. Jack Lane", "Hoover Ave", "Water Rd", "Prentice Dr", "Steephollow Dr" ]
StreetNumGenerator = lambda: randint(1,4000)
Cities = [ "White Lake", "Rochester Hills", "Waterford", "Clarkston", 
    "Bloomfield Hills", "Auburn Hills", "Detroit", "Birmingham" ]
States = [ "Michigan", "Rhode Island", "New York", "California",
    "Iowa", "Tennessee", "Kentucky" ]
ZIPCodes = lambda: randint(1,99999)
phoneNumbers = lambda: str(randint(1000000000,9999999999))
Content = [ "Books","Movies","Electronics","Games" ]
Statuses = {    
    1 : "Processing Request",
    2 : "Building",
    3 : "In-Transit",
    4 : "Delivered"
}
LocationGen = lambda: "%s, %s" % (Cities[randint(0,len(Cities)-1)],States[randint(0,len(States)-1)])
### TEMPLATES
CustomerInsert = "INSERT INTO Customer (fName,lName) values\n\t"
CustValTempl = "('%s','%s')"
CustomerCount = 200
AddressInsert = "INSERT INTO Address (fullName,addressLine1,addressLine2,city,state,zipcode,country,phoneNumber) values\n\t"
AddrValTempl = "('%s','%s','%s','%s','%s',%d,'%s','%s')"
AddressCount = 300
AccountInsert = "INSERT INTO Account (balance,customerId,billAddress,shipAddress) values\n\t"
AcctValTempl = "(%d,%d,%d,%d)"
AccountCount = 200
CardVendorInsert = "INSERT INTO CardVendor (vendorName) values\n\t"
CardVendTempl = "('%s')"
CardVendCount = 200
CreditInsert = "INSERT INTO Credit (cardNum,expDate,vendor,customerId,billAddress) values\n\t"
CredValTempl = "('%s','%s',%d,%d,%d)"
PackageInsert = "INSERT INTO Package (width,length,height,weight,isHazardous,isInternational,customerId,destination) values\n\t"
PackValTempl = "(%d,%d,%d,%d,%s,%s,%d,%d)"
PackageDetailsInsert = "INSERT INTO PackageDetails (packageID,content,value) values\n\t"
PackDetValTempl = "(%d,'%s',%d)"
StatusInsert = "INSERT INTO Status (statusID,statusDescription) values\n\t"
StatusValTempl = "(%d,'%s')"
TrackingInsert = "INSERT INTO Tracking (location,lastUpdate,statusID,packageID) values\n\t"
TrackingValTempl = "('%s','%s',%d,%d)"

### LET'S GET GOING
GEN_FILE = "fill-tables.sql" #likely irrelevant, I'm gonna pipe output with bash anyway
JOINER=",\n\t"
ENDSQL=";"
fullNames = [(firstNames[randint(0,len(firstNames))-1],
    lastNames[randint(0,len(lastNames))-1]) for x in range(AddressCount)]
CustomerInsertBlock = CustomerInsert + JOINER.join([
    CustValTempl % (f,l) for f,l in fullNames]) + ENDSQL
# Find out how many addresses we're gonna put in
IdsToFullNames = [x for x in range(len(fullNames)) if randint(0,1)]
AccountCount = len(IdsToFullNames)
AddressInsertBlock = AddressInsert + JOINER.join([
    AddrValTempl % (
        " ".join(fullNames[custId]),
        "%d %s" % (StreetNumGenerator(),Streets[randint(0,len(Streets)-1)]),
        "", # line2
        Cities[randint(0,len(Cities)-1)],
        States[randint(0,len(States)-1)],
        ZIPCodes(),
        "United States",
        phoneNumbers()
    )
    for custId in IdsToFullNames]) + ENDSQL
addr=0
def AccountIterate():
    global addr
    addr = addr + 1
    return True
AccountInsertBlock = AccountInsert + JOINER.join([
    AcctValTempl % (
        randint(0,1000), #balance
        id+1, #customerId
        addr, #billAddress
        addr #shipAddress
    )
    for id in IdsToFullNames if AccountIterate()]) + ENDSQL
CardVendorInsertBlock = CardVendorInsert + JOINER.join([
    CardVendTempl % vendor
    for vendor in VendorList]) + ENDSQL
addr=0
CreditInsertBlock = CreditInsert + JOINER.join([
    CredValTempl % (
        "%d" % randint(1000000000000000,9999999999999999),
        "%02d/%2d" % (randint(1,12),randint(18,25)),
        randint(1,len(VendorList)),
        id+1,
        addr
    )
    for id in IdsToFullNames if AccountIterate()]) + ENDSQL
PackagesInSys = []
for c in IdsToFullNames:
    for x in range(1,10):
        PackagesInSys.append(c)
DetailedPackages = []
def DoHazardous(p):
    global DetailedPackages
    if(randint(0,10)==10):
        DetailedPackages.append(p)
        return 'TRUE'
    return 'FALSE'
def DoInternational(p):
    # global DetailedPackages
    # if(randint(0,2)>1 and DetailedPackages[-1]!=p):
    #     DetailedPackages.append(p)
    #     return 'TRUE'
    return 'FALSE' # Currently unsupported as all addresses are USA
PackageInsertBlock = PackageInsert + JOINER.join([
    PackValTempl % (
        randint(1,60),
        randint(1,60),
        randint(1,60),
        randint(0,800),
        DoHazardous(id),
        DoInternational(id),
        id+1,
        randint(1,AccountCount-1)
    )
    for id in PackagesInSys]) + ENDSQL
PackageDetailsInsertBlock = PackageDetailsInsert + JOINER.join([
    PackDetValTempl % (
        p, # packageID
        Content[randint(0,len(Content)-1)], # content
        randint(1,100) # value
    )
    for p in DetailedPackages]) + ENDSQL
StatusInsertBlock = StatusInsert + JOINER.join([
    StatusValTempl % (
        k,
        v
    )
    for k,v in Statuses.items()]) + ENDSQL
def RandDate(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
def IterDate():
    global start_date
    itermin = (0.25 * 24 * 60 * 60)
    itermax = (3 * 24 * 60 * 60)
    iteramount = randrange(itermin,itermax)
    start_date = start_date + timedelta(seconds=iteramount)
def PrintDate(d):
    return d.strftime('%Y-%m-%d %H:%M:%S')
TrackUpdates = []
for p in PackagesInSys:
    # set real package id
    packageID = p+1
    # pick a random date for this package to start shipping
    start_date = RandDate(
        datetime.strptime('1/1/2016 1:00 PM', '%m/%d/%Y %I:%M %p'),
        datetime.now()
    )
    # move the date along for every successive status update
    IterDate()
    TrackUpdates.append((packageID,1,PrintDate(start_date)))
    if(randint(0,1)>0):
        IterDate()
        TrackUpdates.append((packageID,2,PrintDate(start_date)))
    for x in range(randint(1,4)):
        IterDate()
        TrackUpdates.append((packageID,3,PrintDate(start_date)))
    IterDate()
    TrackUpdates.append((packageID,4,PrintDate(start_date)))
TrackingInsertBlock = TrackingInsert + JOINER.join([
    TrackingValTempl % (
        LocationGen(), #location
        d, #lastUpdate
        s, #statusID
        p, #packageID
    )
    for p,s,d in TrackUpdates]) + ENDSQL
# And output it for use
print(CustomerInsertBlock)
print(AddressInsertBlock)
print(AccountInsertBlock)
print(CardVendorInsertBlock)
print(CreditInsertBlock)
print(PackageInsertBlock)
print(PackageDetailsInsertBlock)
print(StatusInsertBlock)
print(TrackingInsertBlock)