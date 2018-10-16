import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import s3_helper

def run(event, context):
    # Test out S3 upload capability
    filename = 'test.txt'

    with open(filename, 'w') as file:
        file.write('test')

    send_to_s3(filename)
