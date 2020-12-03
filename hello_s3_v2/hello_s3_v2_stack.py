from aws_cdk import (
    core,
    aws_s3 as _s3,
    aws_lambda as _lambda,
    aws_lambda_python as _lambda_python,
    aws_events as _events,
    aws_events_targets as _targets
)


class HelloS3V2Stack(core.Stack):
    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = _s3.Bucket(self,
                            id='hello-s3-bucket'
                            )

        hello_lambda = _lambda_python.PythonFunction(self,
                                                     id='hello-s3-lambda',
                                                     entry='hello_s3_lambda',
                                                     handler='lambda_handler',
                                                     index='app.py',
                                                     runtime=_lambda.Runtime.PYTHON_3_8,
                                                     environment={'OUTPUT_BUCKET_NAME': bucket.bucket_name}
                                                     )

        sched_event = _events.Rule(self,
                                   id='hello-s3-sched',
                                   schedule=_events.Schedule.rate(core.Duration.minutes(5))
                                   )

        sched_event.add_target(
            _targets.LambdaFunction(hello_lambda)
        )

        # Permissions
        bucket.grant_write(hello_lambda)
