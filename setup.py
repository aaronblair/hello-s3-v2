import setuptools

setuptools.setup(
    name="hello_s3_v2",
    version="0.0.2",
    description="A sample CDK Python app",
    author="author",
    package_dir={"": "hello_s3_v2"},
    packages=setuptools.find_packages(where="hello_s3_v2"),

    install_requires=[
        "aws-cdk.core==1.89.0",
        "aws-cdk.aws_iam==1.89.0",
        "aws-cdk.aws_s3==1.89.0",
        "aws-cdk.aws_lambda_python==1.89.0",
        "aws-cdk.aws_events_targets==1.89.0",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
