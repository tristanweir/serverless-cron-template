import boto3
import json
import os
import logging

client = boto3.client('s3')

def send_to_s3(hostname, scan_json):
    key = "{}.{}".format(hostname, "json")
    bucket = 'observatoryresults'
    binary_scan_json = bytearray(scan_json.encode('utf-8'))
    client.put_object(Body=binary_scan_json, Bucket=bucket,
                      Key=key, ACL='public-read')
    url = "https://s3.amazonaws.com/{}/{}".format(bucket, key)
    logging.info("Uploaded result file to URL: {}".format(url))
