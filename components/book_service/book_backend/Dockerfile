FROM python:3.7-slim

WORKDIR /api

COPY setup.py .
COPY setup.cfg .

RUN pip install --no-cache-dir --upgrade -e '.[dev]'

COPY entry_point.sh /usr/bin/
COPY . .

RUN chmod +x /usr/bin/entry_point.sh
