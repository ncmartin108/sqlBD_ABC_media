#*******************************************************************************
#
#	Project: Part 1
#	Team: Matt Horrocks, Nasley Chumacero-Martin, Mari Langford-Pavao, 
#	CS482 Database Management Systems I
#
#	Description:	These statements insert information into a database 
#					named abc_media_db with 3-5 sample records per table. 
#					The database contains 15 tables.
#
#*******************************************************************************

# Step 1: Populate the Video table (contains columns: videoCode, videoLength).
INSERT INTO Video 
VALUES (2345, 122);

INSERT INTO Video 
VALUES (99578, 224);

INSERT INTO Video 
VALUES (1103, 127);

INSERT INTO Video 
VALUES (1710, 116);

INSERT INTO Video 
VALUES (2417, 88);

#---------------------------------------------------------------------------------------

# Step 2: Populate the Model table (contains columns: modelNo, width, height, weight, depth, screenSize).
INSERT INTO Model
VALUES ('DD19608', 1.78, 1.85, 5, 5.74 );

INSERT INTO Model
VALUES ('DA45229', 3.45, 5.39, 3.02, 6.56 );

INSERT INTO Model
VALUES ('VH356693', 3.25, 3.25, 2, 15.39 );

INSERT INTO Model
VALUES ('BR722344', 12.23, 4.36, 2.1, 55.2 );

INSERT INTO Model
VALUES ('VH971230', 3.76, 12.3, 10.40, 16.9 );

#---------------------------------------------------------------------------------------

# Step 3: Populate the Site table (contains columns: siteCode, type, address, phone).
# The type can only be bar or restaurant.
INSERT INTO Site
VALUES(2, 'bar', '1304 O\'Hara Plains Highway, Suite 122', '583-675-8753');

INSERT INTO Site
VALUES(1, 'restaurant', '28912 Bright Stream Avenue', '358-237-1854');

INSERT INTO Site
VALUES(9, 'bar', '34882 Gleichner Circle', '486-235-4588');

INSERT INTO Site
VALUES(3, 'bar', '8072 Bryce Crossing Place', '585-335-2123');

INSERT INTO Site
VALUES(4, 'restaurant', '160 Baseline Turnpike', '268-555-2487');

#---------------------------------------------------------------------------------------

# Step 4: Populate the Digital Display table (contains columns: serialNo, schedulerSystem, modelNo).
# Scheduler System can only be random, smart, or virtue.
INSERT INTO DigitalDisplay
VALUES('nxdbxys6v4','smart','DD19608');

INSERT INTO DigitalDisplay
VALUES('os4hfh2kki','smart','DA45229');

INSERT INTO DigitalDisplay
VALUES('bf4do2ap2t','random','VH356693');

INSERT INTO DigitalDisplay
VALUES('ktd66rgjfa','virtue','BR722344');

INSERT INTO DigitalDisplay
VALUES('zcwumtpn7e','random','VH971230');

#---------------------------------------------------------------------------------------

# Step 5: Populate the Client table (contains columns: clientId, name, phone, address).
INSERT INTO Client
VALUES (774, 'Nancy Mills', '554-978-9900', '48261 Taylor Park Way, Apt. 896');

INSERT INTO Client
VALUES (15, 'Aiden Freshner', '347-290-1483', '6463 Fichardt Boulevard');

INSERT INTO Client
VALUES (22, 'Melville Longbottom', '145-222-6799', '68883 Bromfield Lakes Circle, Suite 399');

INSERT INTO Client
VALUES (45, 'Mark Rutherford', '224-446-1111', '41235 Sinclair Lakes Drive, Apt. 171');

INSERT INTO Client
VALUES (23, 'Sheryl Green', '220-322-5677', '167 Dixon Road');

#---------------------------------------------------------------------------------------

# Step 6: Populate the Technical Supprt table (contains columns: empId, name, gender).
INSERT INTO TechnicalSupport
VALUES(5986, 'Bernard Garcia', 'M');

INSERT INTO TechnicalSupport
VALUES(4150, 'Jessica Smith', 'F');

INSERT INTO TechnicalSupport
VALUES(8965, 'Laura Johnson', 'F');

#---------------------------------------------------------------------------------------

# Step 7: Populate the Administrator table (contains columns: empId, name, gender).
INSERT INTO TechnicalSupport
VALUES(8965, 'Laura Johnson', 'F');

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------

#---------------------------------------------------------------------------------------
