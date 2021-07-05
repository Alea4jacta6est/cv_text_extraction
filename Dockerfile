FROM python:3.7


RUN apt-get update
RUN apt-get install libleptonica-dev -y
RUN apt-get install tesseract-ocr -y
RUN apt-get install libtesseract-dev -y

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ADD . /cv_text_extraction
WORKDIR /cv_text_extraction
ENV PYTHONPATH /cv_text_extraction

EXPOSE 4200
CMD streamlit run app.py