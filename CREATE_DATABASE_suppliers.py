CREATE DATABASE suppliers;
conn = psycopg2.connect("dbname=mid_term_project user=lhl_student password=lhl_student")
conn = psycopg2.connect(
    host="lhl-data-bootcamp.crzjul5qln0e.ca-central-1.rds.amazonaws.com",
    port=5432
    database="mid_term_project",
    user="lhl_student",
    password="lhl_student")


