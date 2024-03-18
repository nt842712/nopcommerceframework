import logging

class LoginGen:

    @staticmethod
    def loggen():
        logging.basicConfig(filename="/Users/nareshntalesha/PycharmProjects/nopcommerceframework/Logs/automation.log")
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
