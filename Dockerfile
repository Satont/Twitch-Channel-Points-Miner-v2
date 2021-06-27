FROM python:3.9-slim-buster

COPY . /app
WORKDIR /app

RUN apt-get update \
 && apt-get install gcc libffi-dev rustc zlib1g-dev libjpeg-dev libssl-dev --assume-yes \
 && pip install -r requirements.txt \
 && pip cache purge \
 && apt-get remove gcc rustc --assume-yes \
 && apt-get autoremove --assume-yes \
 && rm -rf /var/lib/apt/lists/*

CMD [ "python", "./run.py" ]
