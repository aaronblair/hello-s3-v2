#!/usr/bin/env python3

from aws_cdk import core

from hello_s3_v2.hello_s3_v2_stack import HelloS3V2Stack


app = core.App()
HelloS3V2Stack(app, "hello-s3-v2")
app.synth()
