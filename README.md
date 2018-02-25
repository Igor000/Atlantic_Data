# Atlantiic_Data

The current directory structure has the following sub directories:
~/python
~input_data
~sql


The main python file is parse_input_file.py
It parses input_data/demo_input_data.txt and creates 2 separated output files:
customer.csv
purchase.csv

These 2 files (customer.csv and purchase.csv) are to be loaded into Postgres db

Inside Postgres db there are 2 tables for these files:
atlantic_customer
atlantic_purchase

The Postgres database schema is in ~sql directory inside this file:
customer_purchase_sql.txt
