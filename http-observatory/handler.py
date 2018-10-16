import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

import s3_helper


def run(event, context):
    # Test out S3 upload capability
    scan_result = "test"
    hostname = "www.mozilla.org"

    send_to_s3(hostname, scan_result)
