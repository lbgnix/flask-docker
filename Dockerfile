FROM python:3.6
LABEL maintainer="lal.vishwakarma88@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV APP_COLOR=blue
ENV VERSION=v1 
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["app/app.py"]
