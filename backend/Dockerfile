FROM python:3.7.5-stretch
COPY . /app
WORKDIR /app
RUN pip install flask flask-restful flask_mysqldb flask-cors
EXPOSE 5000
RUN chmod +x api.py
ENTRYPOINT ["python"]
CMD ["api.py"]
