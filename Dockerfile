FROM tensorflow/tensorflow:2.10.0
WORKDIR /prod
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
# Copy and install requirements
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Copy dog_prediction logic
COPY autism autism
COPY setup.py setup.py
#RUN pip install .
# Copy the model to container
RUN pip install 'protobuf<=3.20.1' --force-reinstall
RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

CMD uvicorn autism.api.fast:app --host 0.0.0.0 --port $PORT
#--port 8000
