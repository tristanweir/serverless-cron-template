import boto
import boto.s3
import os
import sys


def send_to_s3(file_path):
    """
    Upload a file to a given s3 bucket
    """
    file = open(file_path)
    key_name = file.name

    param_store = AWSParameterstoreProvider()
    access_key_id = param_store.key('s3_aws_access_key_id')
    secret_access_key = param_store.key('s3_aws_secret_access_key')
    bucket_name = param_store.key('s3_bucket_name')

    conn = boto.connect_s3(aws_access_key_id=access_key_id,
                           aws_secret_access_key=secret_access_key)
    bucket = conn.get_bucket(bucket_name, validate=False)
    key = boto.s3.key.Key(bucket)
    key.key = key_name
    key.set_contents_from_filename(file_path)

    key.set_acl('public-read')
    url = "https://s3.amazonaws.com/{}/{}".format(bucket.name, key.name)
    logging.info("Uploaded result file to URL: {}".format(url))
