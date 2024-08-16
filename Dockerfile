FROM python:3-alpine3.15
WORKDIR /main
COPY . /main
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./main.py
