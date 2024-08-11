FROM python:3.11.9

ARG user_password=
ARG user=
ARG user_email=

USER root

RUN adduser --shell /bin/bash --gecos '' --disabled-password app

USER app

COPY --chown=app:app ./ /webapi-lesson

VOLUME /webapi-lesson/db

WORKDIR /webapi-lesson

RUN pip install --upgrade pip
RUN python --version && pip --version
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$user_email', '$user_password')" | python manage.py shell

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
