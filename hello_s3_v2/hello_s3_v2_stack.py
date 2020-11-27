from aws_cdk import (
    aws_iam as iam,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
    core
)


class HelloS3V2Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "HelloS3V2Queue",
            visibility_timeout=core.Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "HelloS3V2Topic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))
