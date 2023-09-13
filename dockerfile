FROM python:3.11.2-alpine3.17

LABEL Maintainer="PEAKUP/SerhanAyberkKilic"
WORKDIR /code
RUN python -m pip install --upgrade pip
COPY ./requirements.txt /code/requirements.txt
RUN pip install -r requirements.txt
COPY ./app /code/app

# Bu adımda çevresel değişkenler yerine ARG kullanıyoruz
ARG AZURE_ENDPOINT
ARG AZURE_KEY
ARG OPENAI_API_TYPE
ARG OPENAI_API_BASE
ARG OPENAI_API_VERSION
ARG OPENAI_API_KEY

ENV AZURE_ENDPOINT=$AZURE_ENDPOINT
ENV AZURE_KEY=$AZURE_KEY
ENV OPENAI_API_TYPE=$OPENAI_API_TYPE
ENV OPENAI_API_BASE=$OPENAI_API_BASE
ENV OPENAI_API_VERSION=$OPENAI_API_VERSION
ENV OPENAI_API_KEY=$OPENAI_API_KEY

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]
