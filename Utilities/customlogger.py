import logging


class logger:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        fileHandler = logging.FileHandler("D:\\Automation_Program\\phython\\program\\Hybrid_Frame_Work"
                                          "\\Guvi_Orangehmr_project1\\Logs\\Hrm_Automation.log")
        formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(name)s: %(message)s',
                                      datefmt='%d/%m/%Y %I:%M:%S %p')
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger