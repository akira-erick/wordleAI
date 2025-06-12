FROM tensorflow/tensorflow:latest

ENV TF_CPP_MIN_LOG_LEVEL=2

WORKDIR /workspace/app

COPY app/requirements.txt /workspace/app/
RUN pip install --no-cache-dir -r /workspace/app/requirements.txt

COPY app/ /workspace/app/

CMD ["python", "machine.py"]