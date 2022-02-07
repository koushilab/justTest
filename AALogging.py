import logging
import argparse
import mylib
parser = argparse.ArgumentParser()





parser.add_argument( '-log',
                    '--loglevel',
                    default='error',
                    help='Provide Logging level, Example --loglevel debug, default=error')

args = parser.parse_args()



log_level = getattr(logging,args.loglevel.upper(), None)
if not isinstance(log_level,int):
    raise ValueError("Invalid log level: %s" %args.loglevel)

logger = logging.getLogger('sdv.VehicleClass')
logger.setLevel(args.loglevel.upper())
ch = logging.StreamHandler()
ch.setLevel(args.loglevel.upper())

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')

mylib.do_something()