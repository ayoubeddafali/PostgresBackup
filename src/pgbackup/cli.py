import argparse

class DriverAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination


def create_parser():
    parser = argparse.ArgumentParser(
                description="""
                Back up PostgreSQL databases locally or to AWS S3.
                """
            )
    parser.add_argument('url', help='URL of database to backup')
    parser.add_argument('--driver', help='How & where to store backtup',
            nargs=2,
            action=DriverAction,
            required=True)
    return parser


