This is an sql task
##To create a MySQL user named "holberton_user" on both web-01 and web-02 with the host name set to "localhost" and the password "projectcorrection280hbtn", you can run the following commands on each server:

mysql> CREATE USER 'holberton_user'@'localhost' IDENTIFIED BY 'projectcorrection280hbtn';

##This command creates a new MySQL user with the username "holberton_user" and the password "projectcorrection280hbtn", and sets the hostname to "localhost". The user can only connect to the MySQL server from the localhost.

#Then you can give the user the right access to the desired database:

mysql> GRANT ALL PRIVILEGES ON database_name.* TO 'holberton_user'@'localhost';

##This grants all privileges to the user on the specific database and table, replace the database_name with the actual name of the database, and run the command on both web-01 and web-02

## It's important to note that you need to run the command above as an admin user like 'root' otherwise you will face access denied.


