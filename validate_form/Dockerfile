FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . .

CMD ["bash", "-c", "while !</dev/tcp/mongo/27017; do sleep 1; done; python manage.py migrate"]
#CMD ["bash", "-c", "while !</dev/tcp/mongo/27017; do sleep 1; done; python manage.py loaddata app/fixtures/001_form_temlate.json app/fixtures/002_form_data.json"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
