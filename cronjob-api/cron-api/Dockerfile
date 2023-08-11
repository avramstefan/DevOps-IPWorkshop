FROM python:3.10
WORKDIR /home/guess-server-cron/
COPY . .
RUN apt-get update && \
apt-get install -y python3-pip && \
python3 -m pip install redis[hiredis]
CMD ["python3", "guess-cron.py"]
