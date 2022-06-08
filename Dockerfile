FROM python:3.8.13
COPY ./rest_cervices/ /var/www/rest_cervices
RUN pip install -r /var/www/rest_cervices/requirements.txt
EXPOSE 5000
CMD ["python", "/var/www/rest_cervices/run.py"]