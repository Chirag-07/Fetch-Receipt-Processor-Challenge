FROM python:3.10-slim

WORKDIR /Fetch-Receipt-Processor-Challenge

COPY . /Fetch-Receipt-Processor-Challenge

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
