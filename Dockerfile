FROM node:10.17.0-jessie
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN apt-get update && apt-get upgrade -y
RUN apt-get install python python-pip python-dev -y
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN npm -y install bower -g
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN python manage.py bower install
RUN python manage.py collectstatic --noinput
