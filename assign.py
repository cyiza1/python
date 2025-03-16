import mysql.connector
import bcrypt

conn = mysql.connector.connect(host = "localhost",user="root",password="")
cursor = conn.cursor()
database_name=cursor.execute("CREATE DATABASE ac_iot_lab")





cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
cursor.execute(f"USE {database_name}")

# Create tables
tables = [
    """
    CREATE TABLE IF NOT EXISTS courses (
        courseId INT(11) NOT NULL AUTO_INCREMENT,
        courseCode VARCHAR(255) NOT NULL,
        courseTitle VARCHAR(255) NOT NULL,
        programmeId INT(11) NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (courseId),
        FOREIGN KEY (programmeId) REFERENCES programmes(programmeId) ON UPDATE CASCADE ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS items (
        itemId INT(11) NOT NULL AUTO_INCREMENT,
        serialNumber VARCHAR(255) NOT NULL,
        labCode VARCHAR(255) NOT NULL,
        name VARCHAR(255) NOT NULL,
        status ENUM('Working', 'Destroyed') NOT NULL,
        comment VARCHAR(255),
        updatedBy VARCHAR(255),
        itemTypeId INT(11) NOT NULL,
        userId INT(11) NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (itemId),
        FOREIGN KEY (itemTypeId) REFERENCES itemtypes(itemTypeId) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (userId) REFERENCES users(userId) ON UPDATE CASCADE ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS itemtypes (
        itemTypeId INT(11) NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (itemTypeId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS positions (
        positionId INT(11) NOT NULL AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (positionId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS programmes (
        programmeId INT(11) NOT NULL AUTO_INCREMENT,
        programmeTitle ENUM('PhD', 'Masters', 'Bachelors') NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (programmeId)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS rents (
        rentId INT(11) NOT NULL AUTO_INCREMENT,
        applicationNum VARCHAR(255) NOT NULL,
        expectedReturn DATETIME NOT NULL,
        returnDate DATETIME,
        rentCondition ENUM('in_lab', 'Rented', 'Returned') NOT NULL DEFAULT 'in_lab',
        rentStatus ENUM('Pending', 'Approved', 'Canceled') NOT NULL DEFAULT 'Pending',
        rentBy VARCHAR(255),
        approvedBy VARCHAR(255),
        returnedBy VARCHAR(255),
        canceledBy VARCHAR(255),
        courseId INT(11) NOT NULL,
        itemId INT(11) NOT NULL,
        userId INT(11) NOT NULL,
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        PRIMARY KEY (rentId),
        FOREIGN KEY (courseId) REFERENCES courses(courseId) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (itemId) REFERENCES items(itemId) ON UPDATE CASCADE ON DELETE CASCADE,
        FOREIGN KEY (userId) REFERENCES users(userId) ON UPDATE CASCADE ON DELETE CASCADE
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS users (
        userId INT(11) NOT NULL AUTO_INCREMENT,
        fname VARCHAR(255) NOT NULL,
        lname VARCHAR(255) NOT NULL,
        userUniversityCode VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL DEFAULT 'Active',
        gender VARCHAR(255) NOT NULL,
        dob DATETIME NOT NULL,
        password VARCHAR(255) NOT NULL,
        profileImage VARCHAR(255),
        createdAt DATETIME NOT NULL,
        updatedAt DATETIME NOT NULL,
        positionId INT(11),
        PRIMARY KEY (userId),
        FOREIGN KEY (positionId) REFERENCES positions(positionId) ON UPDATE CASCADE ON DELETE SET NULL
    )
    """
]

for table_name, table_sql in tables.items():
    cursor.execute(table_sql)
    print(f"Table {table_name} created successfully.")

# Close connection
cursor.close()
conn.close()

print("Database setup complete.")