FROM python:3.8.13
COPY ./rest_services/ /var/www/rest_services
RUN pip install -r /var/www/rest_services/requirements.txt
CMD ["python", "/var/www/rest_services/run.py"]
