import pytest
import subprocess

from pgbackup import pgdump

url = "postgress://bob:password@example.com:5432/db_one"

def test_dump_call_pg_dump(mocker):
    """
    Utilize pg_dump to interact with Database
    """
    proc = mocker.Mock()
    mocker.patch('subprocess.Popen', return_value=proc)
    assert pgdump.dump(url) == proc
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)

def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns an error if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("NO such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)


