# Build an image that can serve mlflow models.
FROM python:3.13.1-slim

RUN apt-get -y update && apt-get install -y --no-install-recommends nginx

WORKDIR /opt/mlflow

# Install MLflow
RUN pip install mlflow==2.19.0

# Copy model to image and install dependencies
COPY model_dir/model /opt/ml/model
RUN python -c "from mlflow.models import container as C; C._install_pyfunc_deps('/opt/ml/model', install_mlflow=False, enable_mlserver=False, env_manager='local');"

ENV MLFLOW_DISABLE_ENV_CREATION=True
ENV ENABLE_MLSERVER=False
ENV GUNICORN_CMD_ARGS="--timeout 60 -k gevent"

RUN chmod o+rwX /opt/mlflow/

RUN rm -rf /var/lib/apt/lists/*

ENTRYPOINT ["python", "-c", "from mlflow.models import container as C; C._serve('local')"]