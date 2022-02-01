import configparser
import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def drop_tables(cur, conn):
    """
        Iterates and executes all the drop table instructions.
    """    
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
        Iterates and executes all the create table instructions.
    """ 
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
        - Read the credentials from the config file
        - Connect to the database
        - Drop and create tables
    """    
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()