import logging
#proper Config logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logging.debug("This is debug message!")
logging.info("This is info message!")
logging.warning("This is warning message!")
logging.error("This is error message!")
logging.critical("This is critical message!")
