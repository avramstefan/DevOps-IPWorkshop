FROM python:3.10
WORKDIR /home/redis-flask-app/
COPY . .
RUN apt-get update && \
apt-get install -y python3-pip && \  
python3 -m pip install redis[hiredis] &&  \
python3 -m pip install flask
EXPOSE 5000
CMD ["python3", "main.py"]
