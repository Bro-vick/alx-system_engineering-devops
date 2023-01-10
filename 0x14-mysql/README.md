##This is an sql task
# To create a MySQL user named "holberton_user" on both web-01 and web-02 with the host name set to "localhost" and the password "projectcorrection280hbtn", you can run the following commands on each server:

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

# This command creates a new MySQL user with the username "holberton_user" and the password "projectcorrection280hbtn", and sets the hostname to "localhost". The user can only connect to the MySQL server from the localhost.

# Then you can give the user the right access to the desired database:

mysql> GRANT ALL PRIVILEGES ON database_name.* TO 'holberton_user'@'localhost';

# This grants all privileges to the user on the specific database and table, replace the database_name with the actual name of the database, and run the command on both web-01 and web-02

## It's important to note that you need to run the command above as an admin user like 'root' otherwise you will face access denied.


 ## TASK 2
 
 * To create a database named "tyrell_corp" in MySQL, you can use the following command:
 mysql> CREATE DATABASE tyrell_corp;
* This command creates a new database with the name "tyrell_corp".
You can then switch to the newly created database with the use command like this:
mysql> USE tyrell_corp;
* Within the tyrell_corp database, you can create a table named "nexus6" by running the following command:
mysql> CREATE TABLE nexus6 (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) NOT NULL);
This command creates a new table named "nexus6" with two columns, an "id" column which is an integer, the primary key and an auto-increment, and a "name" column which is a VARCHAR of size 255.

To insert data into this table, you can use the INSERT INTO statement like this:

mysql> INSERT INTO nexus6 (name) VALUES ('Roy Batty');

This command insert a row into the nexus6 table, with the 'name' column being set to 'Roy Batty'.

To grant the SELECT permissions on the table "nexus6" to the user "holberton_user", you can run the following command:
mysql> GRANT SELECT ON tyrell_corp.nexus6 TO 'holberton_user'@'localhost';

As a reminder, you also need to run the FLUSH PRIVILEGES command to make sure the changes take effect:

As a reminder, you also need to run the FLUSH PRIVILEGES command to make sure the changes take effect:
mysql> FLUSH PRIVILEGES;
After that you can check if the holberton_user has access to the table by running a SELECT statement like this:
 mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
 or
 mysql> SELECT * FROM nexus6;
