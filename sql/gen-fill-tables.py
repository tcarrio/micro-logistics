import random

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
StreetNumGenerator = lambda: random.randint(1,4000)

Cities = [ "White Lake", "Rochester Hills", "Waterford", "Clarkston", 
    "Bloomfield Hills", "Auburn Hills", "Detroit", "Birmingham" ]

States = [ "Michigan", "Rhode Island", "New York", "California",
    "Iowa", "Tennessee", "Kentucky" ]

ZIPCodes = lambda: random.randint(1,99999)

phoneNumbers = lambda: str(random.randint(1000000000,9999999999))

Content = [ "Books","Movies","Electronics","Games" ]

Statuses = {
    1 : "In-Transit",
    2 : "Delivered",
    3 : "Building",
    4 : "Processing Request"
}

### TEMPLATES

CustomerInsert = "INSERT INTO Customer (fName,lName) values "
CustValTempl = "('%s','%s')"
CustomerCount = 200

AddressInsert = "INSERT INTO Address (fullName,addressLine1,addressLine2,city,state,zipcode,country,phoneNumber) values "
AddrValTempl = "('%s','%s','%s','%s','%s',%d,'%s','%s')"
AddressCount = 300

AccountInsert = "INSERT INTO Account (balance,customerId,billAddress,shipAddress) values "
AcctValTempl = "(%d,%d,%d,%d)"
AccountCount = 200

CardVendorInsert = "INSERT INTO CardVendor (vendorName) values "
CardVendTempl = "('%s')"
CardVendCount = 200

CreditInsert = "INSERT INTO Credit (cardNum,expDate,vendor,customerId,billAddress) values "
CredValTempl = "(%d,'%s',%d,%d,%d)"


PackageInsert = "INSERT INTO Package (dimension,weight,customerId,destination) values "
PackValTempl = "('%s',%d,%d,%d)"
Dimensions = lambda: "%dx%dx%d"%(random.randint(1,60),random.randint(1,60),random.randint(1,60))

### LET'S GET GOING

GEN_FILE = "fill-tables.sql" #likely irrelevant, I'm gonna pipe output with bash anyway
JOINER=",\n\t"
ENDSQL=";"

fullNames = [(firstNames[random.randint(0,len(firstNames))-1],
    lastNames[random.randint(0,len(lastNames))-1]) for x in range(AddressCount)]

CustomerInsertBlock = CustomerInsert + JOINER.join([
    CustValTempl % (f,l) for f,l in fullNames]) + ENDSQL

# Find out how many addresses we're gonna put in
IdsToFullNames = [x for x in range(len(fullNames)) if random.randint(0,1)]
AccountCount = len(IdsToFullNames)

AddressInsertBlock = AddressInsert + JOINER.join([
    AddrValTempl % (
        " ".join(fullNames[custId]),
        "%d %s" % (StreetNumGenerator(),Streets[random.randint(0,len(Streets)-1)]),
        "", # line2
        Cities[random.randint(0,len(Cities)-1)],
        States[random.randint(0,len(States)-1)],
        ZIPCodes(),
        "United States",
        phoneNumbers()
    )
    for custId in IdsToFullNames]) + ENDSQL

# some totally jenky crap here to get some stuff working..
addr=1
def AccountIterate():
    global addr
    addr = addr + 1
    return True

AccountInsertBlock = AccountInsert + JOINER.join([
    AcctValTempl % (
        random.randint(0,1000), #balance
        id, #customerId
        addr, #billAddress
        addr #shipAddress
    )
    for id in IdsToFullNames if AccountIterate()]) + ENDSQL

CardVendorInsertBlock = CardVendorInsert + JOINER.join(VendorList) + ENDSQL

addr=1
CreditInsertBlock = CreditInsert + JOINER.join([
    CredValTempl % (
        random.randint(1000000000000000,9999999999999999),
        "%02d/%2d" % (random.randint(1,12),random.randint(18,25)),
        random.randint(1,len(VendorList)),
        id,
        addr
    )
    for id in IdsToFullNames if AccountIterate()]) + ENDSQL

PackagesInSys = []
for c in IdsToFullNames:
    for x in range(1,10):
        PackagesInSys.append(c)

PackageInsertBlock = PackageInsert + JOINER.join([
    PackValTempl % (
        Dimensions(),
        random.randint(0,800),
        id,
        random.randint(1,AccountCount)
    )
    for id in PackagesInSys]) + ENDSQL

# And output it for use
print(CustomerInsertBlock)
print(AddressInsertBlock)
print(AccountInsertBlock)
print(CardVendorInsertBlock)
print(CreditInsertBlock)
print(PackageInsertBlock)