FROM public.ecr.aws/lambda/python:3.8
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt ${LAMBDA_TASK_ROOT}
RUN pip install -r requirements.txt
CMD ["app.lambda_handler"]