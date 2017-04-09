import random

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

CustomerInsert = "INSERT INTO Customer (fName,lName) values "
CustValTempl = "(%s,%s)"

AddressInsert = "INSERT INTO Address (fullName,addressLine1,addressLine2,city,state,zipcode,country,phoneNumber) values "
AcctValTempl = "(%s,%s,%s,%s,%s,%d,%s,%s)"

AccountInsert = "INSERT INTO Account (balance,customerId,billAddress,shipAddress) values "
AcctValTempl = "(%d,%s,%s,%s)"

CardVenderInsert = "INSERT INTO CardVendor (vendorName) values "
CardVendTempl = "(%s)"

CreditInsert = "INSERT INTO Credit (cardNum,expDate,vendor,customerId,billAddress) values "
CredValTempl = "(%d,%s,%d,%d,%d)"

PackageInsert = "INSERT INTO Package (dimension,weight,customerId,destination) values "
PackValTempl = "(%s,%s,%d,%d)"