# multicorn\_urllib

This is a foreign data wrapper using multicorn and python's urllib module in order to download any data as a table within PostgreSQL.

## How to Use

1. Install multicorn
2. Install this module from this directory.
3. Enable multicorn in the database
4. Create the server in PostgreSQL
5. Create the foreign table
6. Run simple SELECT queries filtering for a single URL.

```
$ sudo apt install postgresql-12-python3-multicorn # 1
$ sudo python3 ./setup.py install # 2
$ sudo -u postgres psql target_database 
```

```SQL
CREATE EXTENSION multicorn; -- 3
CREATE SERVER multicorn_urllib FOREIGN DATA WRAPPER multicorn OPTIONS ( wrapper 'urllibfdw.UrllibForeignDataWrapper' ); --4
CREATE FOREIGN TABLE some_schema.the_internet ( url CHARACTER VARYING, response CHARACTER VARYING ) SERVER multicorn_urllib; --5
SELECT * FROM some_schema.the_internet WHERE url='https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv'; --6
```
