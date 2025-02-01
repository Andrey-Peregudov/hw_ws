FROM tiangolo/uvicorn-gunicorn:python3.10-slim

# set work directory
WORKDIR /fastapi_jinja2

ENV PATH="${PATH}:/root/.local/bin"
ENV PYTHONPATH=.

COPY ./fastapi_jinja2/requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./fastapi_jinja2 .

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]