FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
RUN apt-get install -y nodejs
RUN pip install -r requirements.txt
RUN python2 manage.py makemigrations
RUN python2 manage.py migrate

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install npm
RUN npm -y install bower -g
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN python2 manage.py bower install
RUN python2 manage.py collectstatic --noinput