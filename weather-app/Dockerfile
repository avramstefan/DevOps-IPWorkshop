FROM python:3.10
WORKDIR /home/weather-app//
COPY . .
RUN apt-get update && \
apt-get install -y python3-pip && \
python3 -m pip install flask && \
python3 -m pip install requests
EXPOSE 5001
CMD ["python3", "main.py"]
