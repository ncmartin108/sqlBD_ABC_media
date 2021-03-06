#*******************************************************************************
#
#	Project: Part 1
#	Team: Mari Langford-Pavao, Nasley Chumacero-Martin, Matt Horrocks
#	CS482 Database Management Systems I
#
#	Description:	This file creates an SQL database with the required tables,
#	foreign keys, and value constraints. The schema for this database is in 
#	the Project Part 1 documents for a fictional company named ABC Media.
#
#*******************************************************************************

# Step One: The schema has to be defined so that tables can be inserted.
# Comment out if you're re-running on a system where the database already
# exists.
#drop database abc_media_db; # comment out when not using to test
CREATE database abc_media_db;
use abc_media_db;

# Step Two: Creates the database tables with the specific columns as described in
#           the project documentation.

# Table 1: Creates a table with two columns for Video. Neither column should be empty.
# Video (videoCode: integer, videoLength: integer)
CREATE TABLE Video(
  videoCode INT,
  videoLength INT,
  # Since video lengths can be the same, only video codes need to be unique and
  # the primmary key.
  PRIMARY KEY(videoCode)
);

# Table 2: Creates a table with 6 columns for Model. None of the columns should be left
# empty so the defaults are set to zero. The numeric datatype specifies
# that parentheses are (precision, scale), so (6,2) is a number of maximum
# 6 digits and a maximum of 2 decimal places.
# Model (modelNo: char(10), width: numeric (6,2), height: numeric (6,2),
#   weight: numeric (6,2), depth: numeric (6,2), screenSize: numeric (6,2))
CREATE TABLE Model(
	modelNo CHAR(10),
	width NUMERIC(6,2) ,
	height NUMERIC(6,2) ,
	weight NUMERIC(6,2) ,
	depth NUMERIC(6,2) ,
	screenSize NUMERIC(6,2) ,
	# The model number is the primary key in this table and should be unique.
	PRIMARY KEY(modelNo)
);

# Table 3: Creates a table for Site with 4 columns.
# Site (siteCode: integer, type: varchar (16), address: varchar(100), phone: varchar(16))
CREATE TABLE Site(
	siteCode INT,
    # The type of site is constrained by only a bar or restaurant, so it cannot be empty
    # and there are only 2 choices.
    type VARCHAR(16)
		CHECK (type = 'bar' OR type = 'restaurant'),
    address VARCHAR(100),
    phone VARCHAR(16),
    PRIMARY KEY(siteCode)
);

# Table 4: Creates a table for DigitalDisplay with 3 columns.
# DigitalDisplay (serialNo: char(10), schedulerSystem: char(10), modelNo: char(10))
# Foreign key: modelNo references Model (modelNo)
CREATE TABLE DigitalDisplay(
  serialNo CHAR(10),
  schedulerSystem CHAR(10),
  modelNo CHAR(10),
  # NCM: Added comma, and changed primary key to serialNo because it's the only 
  # one underlined in DB specification.
  PRIMARY KEY(serialNo),
  FOREIGN KEY(modelNo) REFERENCES Model(modelNo)
    ON DELETE CASCADE
	 ON UPDATE CASCADE,
  # NCM: Added constraint so that digital display is only random, smart or virtue.
  CHECK (schedulerSystem IN ('random', 'smart', 'virtue'))
);

# Table 5: Creates a table for Client with 4 columns.
# Client (clientId: integer, name: varchar (40), phone: varchar (16), address: varchar (100)))
CREATE TABLE Client(
  # Constraints do not require all client information
  # to not be optional, however the client unique ID cannot be null.
  clientId INT,
  name VARCHAR(40),
  phone VARCHAR(16),
  address VARCHAR(100),
  # NCM: added the primary key.
  PRIMARY KEY (clientId)
);

# Table 6: Creates a table for Technical Support with 3 columns.
# TechnicalSupport (empId: integer, name: varchar (40), gender: char (1))
CREATE TABLE TechnicalSupport(
	# The employee ID should be a unique identifier and never left null.
	empId INT,
    # A name doesn't have to be unique, but it should also not be empty.
    name VARCHAR(40),
    gender CHAR(1),
    PRIMARY KEY (empId)
);

# Table 7: Creates a table for Administrator with 3 columns.
# Administrator (empId: integer, name: varchar(40), gender: char(1))
CREATE TABLE Administrator(
  empId INT,
  name VARCHAR(40),
  gender CHAR(1),
  # NCM: Added primary key.
  PRIMARY KEY (empId)
);

# Table 8: Creates a table for Salesman with 3 columns.
# Salesman (empId: integer, name: varchar (40), gender: char (1))
CREATE TABLE Salesman(
# The employee ID has to be unique and not empty. Names can be non-unique but should
# also not be empty.
empId INT,
name VARCHAR(40),
gender CHAR(1),
PRIMARY KEY(empId)
);

# Table 9: Creates a table for Airtime Package with 6 columns.
# AirtimePackage (packageId: integer, class: varchar (16), startDate: date, lastDate: date, 
#    frequency: integer, videoCode: integer)
CREATE TABLE AirtimePackage(
	# Since the package ID is the primary key, it should be unique and not null.
	packageId INT,
    class VARCHAR(16),
    # The DATE format is YYYY-MM-DD
    startDate DATE,
    lastDate DATE,
    frequency INT,
    videoCode INT,
    PRIMARY KEY(packageId),
    CHECK (class IN('economy', 'whole day', 'golden hours'))
);

# Table 10: Creates a table for Admin Work Hours with 3 columns.
# AdmWorkHours (empId: integer, day: date, hours: numeric (4,2))
# Foreign key: empId references Administrator (empId)
CREATE TABLE AdmWorkHours(
	empId INT,
    day DATE,
    hours NUMERIC(4,2),
    PRIMARY KEY(empId, day)
);

# Table 11: Creates a table for Broadcasts. The videoCode column matches the one from Video (table 1).
# The siteCode column matches (table 3) Site, so it will not matter if either column isnt unique.
# Broadcasts (videoCode: integer, siteCode: integer)
# Foreign key: videoCode references Video (videoCode)
# Foreign key: siteCode references Site (siteCode)
CREATE TABLE Broadcasts(
	# Neither of these fields have to be unique because they reference other tables.
	videoCode INT,
	siteCode INT,
	PRIMARY KEY(videoCode, siteCode),
    # The column videoCode matches the videoCode from the Video table, so it gets declared as
    # a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY (videoCode) REFERENCES Video(videoCode)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	# The column siteCode matches the siteCode from the Site table, so it gets declared as
	# a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY(siteCode) REFERENCES Site(siteCode)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

# Table 12: Creates a table for Administers. The empId column matches the one from Adminstrator(table 7).
# The siteCode column matches (table 3) Site, so it will not matter if either column isnt unique.
# Administers(empId: integer, siteCode: integer)
# Foreign key: empId references Adminstrator(empId)
# Foreign key: siteCode references Site(siteCode)
CREATE TABLE Administers(
	# Neither of these fields are unique because an employee can administrate more than 1 site,
    # and a site can potentially have more than 1 administrator.
	empId INT,
	siteCode INT,
	PRIMARY KEY (empId, siteCode),
	# The column empId matches the empId from the Administrator table, so it gets declared as
	# a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY (empId) REFERENCES Administrator(empId)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	# The column siteCode matches the siteCode from the Site table, so it gets declared as
    # a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY (siteCode) REFERENCES Site(siteCode)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);

# Table 13: This creates a table for specializes with 2 columns.
# Specializes (empId: integer, modelNo: char(10)) 
# Foreign key: empId references TechnicalSupport (empId)
# Foreign key: modelNo references Model (modelNo)
CREATE TABLE Specializes (
	empId INT,
    modelNo CHAR(10),
    PRIMARY KEY (empId, modelNo),
    FOREIGN KEY(empId) REFERENCES TechnicalSupport(empId)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY(modelNo) REFERENCES Model(modelNo)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Table 14: Creates a table for Purchases with 4 columns.
# Purchases (clientId: integer, empId: integer, packageId: integer, commissionRate: numeric (4,2))
#	Foreign key: clientId references Client (clientId)
#	Foreign key: empId references Salesman (empId)
#	Foreign key: packageId references AirtimePackage (packageId)
CREATE TABLE Purchases(
	# Clients should be able to make more than one purchase so the ID does not need to be unique.
	clientId INT,
    # The same employee can help the same client, so this column also does not need to be unique.
    empId INT,
    # The package ID should be different to avoid duplicate row entries.
    packageId INT,
    # The comission rate doesnt need to be unique.
    comissionRate NUMERIC(4,2),
    # Three columns together make up the primary key in this table.
    PRIMARY KEY(clientId, empId, packageId),
	# The column clientID appears a primary key in table 5 Client and is declared here as a foreign key.
    # The action "CASCADE", guarantees that if the parent table gets deleted or updated, the
	# database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(clientId) REFERENCES Client(clientId)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    # The column empID is a foreign key in many tables, but this one references Salesman, table 8.
    # The action "CASCADE", guarantees that if the parent table gets deleted or updated, the
	# database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(empId) REFERENCES Salesman(empId)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	# The column packageID appears in AirtimePackage table as a primary key, so is referenced here
    # as a foreign key. The action "CASCADE", guarantees that if the parent table gets deleted or
    # updated, the database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(packageId) REFERENCES AirtimePackage(packageId)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Table 15: Creates a table for Locates. The serialNo column matches the one from DigitalDisplay(table 4).
# The siteCode column matches (table 3) Site, so it will not matter if either column isnt unique.
# Locates (serialNo: char (10), siteCode: integer)
# Foreign key: serialNo references DigitalDisplay (serialNo)
# Foreign key: siteCode references Site (siteCode)
CREATE TABLE Locates(
	serialNo CHAR(10),
	siteCode INT,
	PRIMARY KEY (serialNo, siteCode),
	# The column serialNo matches the serialNo from the DigitalDisplay table, so it gets declared as
	# a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY (serialNo) REFERENCES DigitalDisplay(serialNo)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	# The column siteCode matches the siteCode from the Site table, so it gets declared as
	# a foreign key here. The action "CASCADE", guarantees that if the parent table gets deleted
	# or updated, the database will automatically delete the corresponding value in this child table.
	FOREIGN KEY (siteCode) REFERENCES Site(siteCode)
		ON DELETE CASCADE
		ON UPDATE CASCADE
);
