FROM python:3.11-rc-alpine

RUN apk add ca-certificates \
    gcc \
    postgresql-dev \
    linux-headers \
    musl-dev \
    libffi-dev \
    jpeg-dev zlib-dev \
    && pip install django-ninja

WORKDIR /usr/src
COPY . .
RUN pip install -r requirements.txt

WORKDIR /usr/src/skill_matrix_api
RUN python /usr/src/skill_matrix_api/manage.py collectstatic --no-input

EXPOSE 8000

CMD python /usr/src/skill_matrix_api/manage.py makemigrations skill_matrix_api && python /usr/src/skill_matrix_api/manage.py migrate && python /usr/src/skill_matrix_api/manage.py runserver 0.0.0.0:8000
