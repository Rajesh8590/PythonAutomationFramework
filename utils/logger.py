import logging
import os

class Logger:
    @staticmethod
    def get_logger():
        log_folder = "logs"
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)
        logger = logging.getLogger("AutomationFramework")
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
            file_handler = logging.FileHandler("logs/execution.log")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger