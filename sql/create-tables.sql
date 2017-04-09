DROP TABLE IF EXISTS Status;
DROP TABLE IF EXISTS Tracking;
DROP TABLE IF EXISTS PackageDetails;
DROP TABLE IF EXISTS Package;
DROP TABLE IF EXISTS Credit;
DROP TABLE IF EXISTS CardVendor;
DROP TABLE IF EXISTS Account;
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS Customer;

-- Setup tables required for Account
CREATE TABLE Customer(
    customerID INT NOT NULL AUTO_INCREMENT,
    fName VARCHAR(20),
    lName VARCHAR(20),
    PRIMARY KEY (customerID));

CREATE TABLE Address(
    addressID INT NOT NULL AUTO_INCREMENT,
    fullName VARCHAR(50) NOT NULL,
    addressLine1 VARCHAR(100) NOT NULL,
    addressLine2 VARCHAR(100),
    city VARCHAR(20) NOT NULL,
    state VARCHAR(20) NOT NULL,
    zipcode INT NOT NULL,
    country VARCHAR(20) NOT NULL,
    phoneNumber VARCHAR(10),
    PRIMARY KEY (addressID));

CREATE TABLE Account(
    accountNum INT NOT NULL AUTO_INCREMENT,
    balance INT NOT NULL,
    customerID INT NOT NULL,
    billAddress INT NOT NULL,
    shipAddress INT NOT NULL,
    PRIMARY KEY (accountNum),
    FOREIGN KEY (customerID) references Customer(customerID),
    FOREIGN KEY (billAddress) references Address(addressID),
    FOREIGN KEY (shipAddress) references Address(addressID));

-- Set up vendor table (VISA, MasterCard, etc. goes here) before Credit
CREATE TABLE CardVendor(
    vendorID INT NOT NULL AUTO_INCREMENT,
    vendorName VARCHAR(20) NOT NULL,
    vendorSupported BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (vendorID));

CREATE TABLE Credit(
    cardNum INT NOT NULL,
    expDate DATE NOT NULL,
    vendor INT NOT NULL,
    customerID INT NOT NULL,
    billAddress INT NOT NULL,
    FOREIGN KEY (customerID) references Customer(customerID),
    FOREIGN KEY (billAddress) references Address(addressID),
    FOREIGN KEY (vendor) references CardVendor(vendorID));

-- Ready to roll with Package and related with Customer/Address finished
CREATE TABLE Package(
    packageID INT NOT NULL AUTO_INCREMENT,
    dimension INT NOT NULL,
    weight INT NOT NULL,
    isHazardous BOOLEAN DEFAULT FALSE,
    isInternational BOOLEAN DEFAULT FALSE,
    customerID INT NOT NULL,
    destination INT NOT NULL,
    PRIMARY KEY (packageID),
    FOREIGN KEY (customerID) references Customer(customerID),
    FOREIGN KEY (destination) references Address(addressID));

CREATE TABLE PackageDetails(
    packageID INT NOT NULL,
    content VARCHAR(20) NOT NULL,
    value INT NOT NULL,
    FOREIGN KEY (packageID) references Package(packageID));

CREATE TABLE Status(
    statusID INT NOT NULL AUTO_INCREMENT,
    statusDescription VARCHAR(20),
    PRIMARY KEY (statusID));

CREATE TABLE Tracking(
    trackID INT NOT NULL AUTO_INCREMENT,
    location VARCHAR(50) NOT NULL,
    lastUpdate DATE NOT NULL,
    statusID INT NOT NULL,
    packageID INT NOT NULL,
    PRIMARY KEY(trackID),
    FOREIGN KEY (packageID) references Package(packageID),
    FOREIGN KEY (statusID) references Status(statusID));
