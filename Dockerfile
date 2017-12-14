FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
ADD . /code/
WORKDIR /code
RUN pip install -r requirements.txt
RUN python2 manage.py migrate

RUN apt-get update && apt-get upgrade -y

RUN apt-get -y install nodejs
RUN ln -s /usr/bin/nodejs /usr/bin/node
RUN apt-get -y install npm
RUN npm -y install bower -g
RUN echo '{ "allow_root": true }' > /root/.bowerrc
RUN python2 manage.py bower install
RUN python2 manage.py collectstatic --noinput