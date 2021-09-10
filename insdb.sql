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

# Step 3: Populate the Site table (contains columns: siteCode, type, address, phone).
INSERT INTO Site
VALUES(2, bar, '1304 O\'Hara Plains, Suite 122', 583-675-8753);
