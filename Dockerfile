FROM python:3.8
RUN pip install -r requirements.txt
CMD ["python", "manage.py", "runserver"]