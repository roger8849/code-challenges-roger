# Demonstrate how to customize logging output

import logging

# TODO: add another function to log from
def anotherFunction():
    logging.debug('This is a debug-level message')

extData = {
    'user': 'roger@gmail.com'
}
def main():
    # set the output file and debug level, and
    # use a custom formatting specification
    fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d User:%(user)s %(message)s"
    dateStr = "%m/%d/%Y %I:%M:%S %p"
    logging.basicConfig(filename="output.log",
                        level=logging.DEBUG,
                        format=fmtStr,
                        datefmt=dateStr)

    logging.info("This is an info-level log message", extra=extData)
    logging.warning("This is a warning-level message", extra=extData)


if __name__ == "__main__":
    main()
