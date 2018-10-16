import datetime
import logging
import s3_helper

from s3_helper import send_to_s3

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)



def run(event, context):
    # Test out S3 upload capability
    scan_result = "test"
    hostname = "www.mozilla.org"

    send_to_s3(hostname, scan_result)
