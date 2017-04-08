CREATE TABLE Customer(
  customerID INT, 
  fname VARCHAR(20), 
  lName VARCHAR(20),
  PRIMARY KEY (customerID));

CREATE TABLE Account(
  accountNum INT NOT NULL, 
  shipAddress VARCHAR(50) NOT NULL, 
  billAddress VARCHAR(50) NOT NULL, 
  balance INT NOT NULL, 
  customerID INT NOT NULL,
  PRIMARY KEY (accountNum),
  FOREIGN KEY (customerID) references Customer(customerID));

CREATE TABLE Credit(
  cardNum INT NOT NULL, 
  expDate INT NOT NULL, 
  billAddress VARCHAR(50) NOT NULL, 
  vendor VARCHAR(20) NOT NULL, 
  customerID INT NOT NULL,
  FOREIGN KEY (customerID) references Customer(customerID));
  
CREATE TABLE Package(
  packageID INT NOT NULL,
  dimension INT NOT NULL,
  weight INT NOT NULL,
  destinationAddress VARCHAR(50) NOT NULL,
  isHazardous BOOLEAN DEFAULT FALSE,
  isInternational BOOLEAN DEFAULT FALSE,
  customerID INT NOT NULL,
  PRIMARY KEY (packageID),
  FOREIGN KEY (customerID) references Customer(customerID));

CREATE TABLE PackageDetails(
  packageID INT NOT NULL,
  content VARCHAR(20) NOT NULL,
  value INT NOT NULL,
  FOREIGN KEY (packageID) references Package(packageID));
  
CREATE TABLE Tracking(
  trackID INT NOT NULL,
  location VARCHAR(50) NOT NULL,
  date DATE NOT NULL,
  status VARCHAR(20) NOT NULL,
  packageID INT NOT NULL,
  PRIMARY KEY(trackID),
  FOREIGN KEY(packageID) references Package(packageID));