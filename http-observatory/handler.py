import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from s3_helper import send_to_s3


def run(event, context):
    # Test out S3 upload capability
    filename = 'test.txt'

    with open(filename, 'w') as file:
        file.write('test')

    send_to_s3(filename)
