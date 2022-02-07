import logging
import argparse
parser = argparse.ArgumentParser()
parser.add_argument( '-log',
                    '--loglevel',
                    default='error',
                    help='Provide Logging level, Example --loglevel debug, default=error')

args = parser.parse_args()

# logging.basicConfig(level=args.loglevel.upper())

log_level = getattr(logging,args.loglevel.upper(), None)
if not isinstance(log_level,int):
    raise ValueError("Invalid log level: %s" %args.loglevel)
logging.basicConfig(level=args.loglevel.upper())
logging.info("This is warning Message")
logging.warning("This is Warning Message")
logging.debug("This is Debug Message")
logging.error("This is error Message")