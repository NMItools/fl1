# =====================================================================================================================
# ubuntu server
# ---------------------------------------------------------------------------------------------------------------------

sudo -u postgres psql

# postgres=# CREATE DATABASE test_db;
# postgres=# \q

sudo -u postgres psql test_db

# test_db=# \i ‘/mnt/hgfs/D/git/fl1/pgdb/table_setup.sql’
# test_db=# \copy test_table(id,zip,type,lon,lat) FROM '/mnt/hgfs/D/git/fl1/large_file.csv' DELIMITERS ',' CSV HEADER;
# test_db=# UPDATE test_table SET geom = ST_SETSRID(ST_MakePoint(lon, lat),4326); 
# test_db=# \i 'C:/Users/Nebojsa/git/fl1/pgdb/f_cnt_within_distance.sql'
# test_db=# \i 'C:/Users/Nebojsa/git/fl1/pgdb/f_rows_within_distance.sql'