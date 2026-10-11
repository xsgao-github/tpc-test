from trino.dbapi import Connection, connect


def get_trino_connection(
    host: str = "localhost", port: int = 8080, user: str = "user"
) -> Connection:
    """Get a Trino connection."""
    return connect(
        host=host,
        port=port,
        user=user,
        catalog="tpch",
        schema="tiny",
    )


def get_trino_version(conn: Connection) -> str:
    """Get the Trino server version from the connection."""
    cursor = conn.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    return row[0] if row else "Unknown"
