FROM python:3.11.2-apline3.17

ENV PYTHONUNFBUFFERED 1
ENV PYTHONDONTWRITECODE=1

WORKDIR /serverDjango

COPY requeriments.txt /serverDjango/

RUN pip install -r requeriments.txt

COPY . /serverDjango/


EXPOSE 4200

# Iniciar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:4200"]

