FROM python:latest

VOLUME /app
WORKDIR /app

#install dependencies
RUN pip install --upgrade pip
RUN pip install requests
RUN pip install bs4
RUN pip install lxml
RUN pip install pandas

#command to run on container start
CMD ["python","space_launches_reentries.py"]