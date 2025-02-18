import oracledb as db

# Oracle Instant Clietn directory
db.init_oracle_client(lib_dir=r"C:\instantclient_21_8")

# Database connection function
def oracle_database_connection():

    # DB Parameters
    username = ''
    password = ''
    service_name = ''

    try:
        # Connection string
        conn = db.connect(user=username, password=password, dsn=service_name)
        print("Successfull connected to database!")

        return conn
    
    except Exception as err:
        print(err)

# Query execution function
def oracle_execution_query():

    try:
        # Connection trigger
        conn = oracle_database_connection()

        # Cursor creation
        cur = conn.cursor()

        query = """
        SELECT *
        FROM DUAL
        """

        # Insert result into variable
        result = cur.execute(query).fetchall()

        print(result)

    except Exception as err:
        print(err)

    finally:
        conn.close()

# Query execution trigger
oracle_execution_query()
