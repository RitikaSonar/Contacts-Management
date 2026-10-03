# Contacts-Project

A Contact Management System built using Python and MySQL. The application allows users to add, view, update, and delete contacts stored in a MySQL database.

## Features

* Add Contact
* View Contacts
* Update Contact
* Delete Contact
* Store contacts in MySQL database

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AtharvKhambayate/Contacts-Project.git
cd Contacts-Project
```

### 2. Install Dependencies

```bash
pip install mysql-connector-python
```

### 3. Create the Database

Open MySQL Command Line Client and run:

```sql
CREATE DATABASE contacts_db;

USE contacts_db;

CREATE TABLE contact (
    name VARCHAR(50) NOT NULL,
    number VARCHAR(10) NOT NULL
);
```

### 4. Update Database Credentials

Edit the connection settings in `contacts_app.py`:

```python
host = "localhost"
user = "root"
password = "your_password"
database = "contacts_db"
```

### 5. Run the Application

```bash
python contacts_app.py
```

## Technologies Used

* Python
* MySQL
* mysql-connector-python
