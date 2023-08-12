FROM python

RUN apt update

RUN pip install redis flask requests

COPY cron.py .

CMD ["python3" , "cron.py"]
