FROM python:3.8

WORKDIR /location

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY location.py .

CMD ["python", "location.py"]

