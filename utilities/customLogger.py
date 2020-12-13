import logging


class LogGen:
    @staticmethod
    def logGen():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)
        logging.basicConfig(filename=".\\Logs\\automation.log", format='%(asctime)s:%(levelname)s:%(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
