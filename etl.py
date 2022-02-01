import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
        Iterates the list of queries that load the data files 
        from s3 bucket to the stage tables.
    """    
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
        Iterates the list of queries that insert the data from stage to final table.
    """    
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
        - Read the credentials from the config file
        - Connect to the database
        - Load the data files from s3 bucket into sage tables
        - Load the final tables from stage tables
        - Close the connection.
    """    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()