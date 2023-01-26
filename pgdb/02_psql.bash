# =====================================================================================================================
# ubuntu server
# ---------------------------------------------------------------------------------------------------------------------

# Create database for testing

sudo -u postgres psql

# postgres=# CREATE DATABASE test_db;
# postgres=# \q


# Login to test_db database and execute commands for setup and loading input data from CSV file and functions with queries

sudo -u postgres psql test_db

# test_db=# \i ‘/mnt/hgfs/D/git/fl1/pgdb/table_setup.sql’
# test_db=# \copy test_table(id,zip,type,lon,lat) FROM '/mnt/hgfs/D/git/fl1/input.csv' DELIMITERS ',' CSV HEADER;
# test_db=# UPDATE test_table SET geom = ST_SETSRID(ST_MakePoint(lon, lat),4326); 
# test_db=# \i '/mnt/hgfs/D/git/fl1/pgdb/f_cnt_within_distance.sql'
# test_db=# \i '/mnt/hgfs/D/git/fl1/pgdb/f_rows_within_distance.sql'