FROM python:3-alpine


WORKDIR /app

ENV FLASK_APP=/app/app.py
# * using cache as much as possible
COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

# copying all source code
COPY . /app


ENTRYPOINT [ "python", "app.py" ]
#CMD ["-h", "0.0.0.0"]