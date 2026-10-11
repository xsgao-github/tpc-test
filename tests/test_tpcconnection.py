from unittest.mock import MagicMock, patch

from tpcconnection import get_trino_connection, get_trino_version


@patch("tpcconnection.connect")
def test_get_trino_connection(mock_connect):
    """Test that get_trino_connection passes the correct arguments to the Trino driver."""
    get_trino_connection(host="my-custom-host", port=9090, user="developer")

    mock_connect.assert_called_once_with(
        host="my-custom-host",
        port=9090,
        user="developer",
        catalog="tpch",
        schema="tiny",
    )


@patch("tpcconnection.connect")
def test_get_trino_version(mock_connect):
    """Test that get_trino_version executes the query and returns the version string."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ["483"]

    mock_conn = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_connect.return_value = mock_conn

    version = get_trino_version(mock_conn)

    mock_cursor.execute.assert_called_once_with("SELECT version()")
    assert version == "483"
