FROM python:3.10
WORKDIR /home/weather-app/
COPY . .
RUN apt-get update && \
apt-get install -y python3-pip && \
pip install flask requests redis
EXPOSE 5001
CMD ["python3", "main.py"]
