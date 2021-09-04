#*******************************************************************************
#
#	Project: Part 1
#	Team: Mari Langford-Pavao, Nasley Chumacero-Martin, Matt Horrocks
#	CS482 Database Management Systems I
#
#	Description:	This file creates an SQL database with the required tables,
#					foreign keys, and value constraints. The schema for this
#					database is in the Project Part 1 documents for a
#					fictional company named ABC Media.
#
#*******************************************************************************

# Step One: The schema has to be defined so that tables can be inserted.

CREATE SCHEMA abc_media_db;


# Step Two: Creates the database tables with the specific columns as described in
#           the project documentation.

# Table 1: Creates a table with two columns for Video. Neither column should be empty.
# Video (videoCode: integer, videoLength: integer)
CREATE TABLE Video(
  videoCode INT UNIQUE NOT NULL,
  videoLength INT DEFAULT 0,
  # Since video lengths can be the same, only video codes need to be unique and
  # the primmary key.
  PRIMARY KEY(videoCode)
);

# Table 2: Creates a table with 6 columns for Model. None of the columns should be left
#          empty so the defaults are set to zero. The numeric datatype specifies 
#		   that parentheses are (precision, scale), so (6,2) is a number of maximum  
#		   6 digits and a maximum of 2 decimal places.
# Model (modelNo: char(10), width: numeric (6,2), height: numeric (6,2),
#        weight: numeric (6,2), depth: numeric (6,2), screenSize: numeric (6,2))
CREATE TABLE Model(
	modelNo CHAR(10) UNIQUE NOT NULL,
	width NUMERIC(6,2) DEFAULT 0,
	height NUMERIC(6,2) DEFAULT 0,
	weight NUMERIC(6,2) DEFAULT 0,
	depth NUMERIC(6,2) DEFAULT 0,
	screenSize NUMERIC(6,2) DEFAULT 0,
	# The model number is the primary key in this table and should be unique.
	PRIMARY KEY(modelNo)
);

# Table 3: Creates a table for Site with 4 columns.
# Site (siteCode: integer, type: varchar (16), address: varchar(100), phone: varchar(16))
CREATE TABLE Site(
	siteCode INT UNIQUE NOT NULL,
    # The type of site is constrained by only a bar or restaurant, so it cannot be empty
    # and there are only 2 choices.
    type VARCHAR(16) NOT NULL
		CHECK (type = 'bar' OR type = 'restaurant'),
    address VARCHAR(100),
    phone VARCHAR(16),
    PRIMARY KEY(siteCode)
);
# Table 4:

# Table 5:

# Table 6:

# Table 7:

# Table 8:

# Table 9:

# Table 10:

# Table 11: Creates a table for Broadcasts. The videoCode column matches the one from Video (table 1).
#			The siteCode column matches (table 3) Site, so it will not matter if either column isn't unique.
# Broadcasts (videoCode: integer, siteCode: integer)
# 	Foreign key: videoCode references Video (videoCode)
#	Foreign key: siteCode references Site (siteCode)
CREATE TABLE Broadcasts(
videoCode INT NOT NULL,
siteCode INT NOT NULL,
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

# Table 12:

# Table 13:

# Table 14: Creates a table for Purchases with 4 columns. 
# Purchases (clientId: integer, empId: integer, packageId: integer, commissionRate: numeric (4,2)) 
#	Foreign key: clientId references Client (clientId)
#	Foreign key: empId references Salesman (empId) 
#	Foreign key: packageId references AirtimePackage (packageId)
CREATE TABLE Purchases(
	# Clients should be able to make more than one purchase so the ID does not need to be unique.
	clientID INT NOT NULL,
    # The same employee can help the same client, so this column also does not need to be unique.
    empID INT NOT NULL,
    # The package ID should be different to avoid duplicate row entries.
    packageID INT UNIQUE NOT NULL,
    # The comission rate doesn't need to be unique.
    comissionRate NUMERIC(4,2) DEFAULT 0,
    # Three columns together make up the primary key in this table.
    PRIMARY KEY(clientID, empID, packageID),
	# The column clientID appears a primary key in table 5 Client and is declared here as a foreign key.
    # The action "CASCADE", guarantees that if the parent table gets deleted or updated, the
	# database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(clientID) REFERENCES Client(clientID)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    # The column empID is a foreign key in many tables, but this one references Salesman, table 8.
    # The action "CASCADE", guarantees that if the parent table gets deleted or updated, the
	# database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(empID) REFERENCES Salesman(empID)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
	# The column packageID appears in AirtimePackage table as a primary key, so is referenced here
    # as a foreign key. The action "CASCADE", guarantees that if the parent table gets deleted or 
    # updated, the database will automatically delete the corresponding value in this child table.
    FOREIGN KEY(packageID) REFERENCES AirtimePackage(packageID)
		ON DELETE CASCADE
        ON UPDATE CASCADE
);

# Table 15:


# Step Three: TBD
