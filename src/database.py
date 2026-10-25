import pyodbc


DRIVER_NAME = "SQL Server"
SERVER_NAME = r"NASIRS-LAPTOP\SQLEXPRESS"
DATABASE_NAME = "DecathlonDB"


def get_connection():
    """Create and return a connection to the Decathlon SQL Server database."""

    connection_string = (
        f"DRIVER={{{DRIVER_NAME}}};"
        f"SERVER={SERVER_NAME};"
        f"DATABASE={DATABASE_NAME};"
        "Trusted_Connection=yes;"
    )

    conn = pyodbc.connect(connection_string)

    return conn

