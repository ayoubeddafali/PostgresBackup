import argparse

class DriverAction(argparse.Action):
    known_drivers = ['s3', 'local']
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        if driver.lower() not in self.known_drivers:
            parser.error("Unknown driver")
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
            metavar=("DRIVER", "DESTINATION"),
            action=DriverAction,
            required=True)
    return parser


if __name__== "__main__":
    parser = create_parser()
    parser.parse_args()

def main():
    from pgbackup import pgdump, storage
    args = create_parser().parse_args()
    dump = pgdump.dump(args.url)
    outfile = open(args.destination, "w")
    storage.local(dump.stdout, outfile)






