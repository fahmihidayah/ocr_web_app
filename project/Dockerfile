FROM python:3.9-bullseye
#FROM python:3.9-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /src
RUN mkdir /logs
WORKDIR /src

RUN pip install --upgrade pip
RUN apt-get -y update -qq \
    && apt-get -y install --no-install-recommends  \
    postgresql-client libpng-dev libjpeg-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists && true
RUN apt-get update -qq && apt-get install -y build-essential

RUN pip install importlib_metadata
RUN pip install torch>=1.9.0 torchvision>=0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

#RUN apk add --update --no-cache postgresql-client jpeg-dev
#RUN apk add --update --no-cache --virtual .tmp-build-deps \
#    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev libffi-dev gfortran build-base wget freetype-dev libpng-dev openblas-dev
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h
#RUN apk add make automake gcc g++ subversion python3-dev
#
#RUN pip3 install importlib_metadata numpy
#RUN pip3 install --default-timeout=100 future torch>=1.9.0 torchvision>=0.9.0 -f https://download.pytorch.org/whl/torch_stable.html

RUN pip3 install -r requirements.txt

EXPOSE 8000
RUN chmod +x entrypoint.sh
CMD ["./entrypoint.sh"]
# CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"] #==1.14.3 scipy pytz>=2011k pandas matplotlib
# CMD ["gunicorn", "-c", "gunicorn.conf.py", "project.wsgi"]
