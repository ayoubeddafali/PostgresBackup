import pytest
from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one"

@pytest.fixture()
def parser():
    return cli.create_parser()

def test_parser_without_driver(parser):
	"""
	Without a specified driver, the parser will exit
	"""
	with pytest.raises(SystemExit):
		parser.parse_args([url])


def test_parser_with_driver(parser):
    """
    The parser will exit if it receivers a driver without a destination
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'local'])


def test_parser_with_driver_and_destination(parser):
    """
    The parser will not exit if it receives a driver and a destination
    """
    args = parser.parse_args([url, '--driver', 'Local', '/some/path'])
    assert args.driver == 'local'
    assert args.destination == '/some/path'

def test_unkown_driver(parser):
    """
    The parser will exit if the driver is unkwown"
    """
    with pytest.raises(SystemExit):
        parser.parse_args([url, '--driver', 'azure', '/dest'])


def test_driver_argument_must_be_knwon(parser):
    """
    The parser will exit if the driver is unknown
    """
    assert parser.parse_args([url, '--driver', 'local', '/path'])
















