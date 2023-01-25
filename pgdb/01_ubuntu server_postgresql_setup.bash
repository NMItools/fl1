sudo apt update -y
sudo apt install -y postgresql postgresql-contrib postgresql-client
sudo dpkg --status postgresql
sudo systemctl start postgresql.service
sudo systemctl status postgresql.service

# Log in to the PostgreSQL shell (psql):
sudo -u postgres psql

# Run the following command at the prompt to initiate a password change. 
# Provide a strong password of your choice and press Enter.

\password

sudo nano /etc/postgresql/14/main/pg_hba.conf
# host	all			all			0.0.0.0/0		scram-sha-256

sudo nano /etc/postgresql/14/main/postgresql.conf
# listen_addresses = '*'

sudo systemctl restart postgresql

sudo apt-get install postgis