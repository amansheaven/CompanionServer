FROM python:3.7-alpine
RUN apk update 
COPY . /app
WORKDIR /app
RUN pip install gunicorn
RUN pip install -r requirements.txt
#SHELL ["/bin/sh"]
#RUN ECHO We shifted to sh!!
ENV DEBUG False
RUN chmod +x start.sh
CMD ["./start.sh"]
