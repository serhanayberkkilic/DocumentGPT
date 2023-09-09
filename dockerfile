FROM python:3.11.2-alpine3.17

LABEL Maintainer="PEAKUP/SerhanAyberkKilic"
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./app /code/app

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]