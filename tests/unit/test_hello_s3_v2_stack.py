import json
import pytest

from aws_cdk import core
from hello-s3-v2.hello_s3_v2_stack import HelloS3V2Stack


def get_template():
    app = core.App()
    HelloS3V2Stack(app, "hello-s3-v2")
    return json.dumps(app.synth().get_stack("hello-s3-v2").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
