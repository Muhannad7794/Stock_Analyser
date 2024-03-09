FROM python:3
ENV PYTHONUNBUFFERED 1

WORKDIR /Stock_Analyser_dockerized

COPY . /Stock_Analyser_dockerized/

# Install dependencies
COPY requirements.txt /Stock_Analyser_dockerized/
RUN pip install -r requirements.txt