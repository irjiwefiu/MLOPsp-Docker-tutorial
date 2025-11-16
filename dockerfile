FROM python:3.8-slim
# create a workDir at docker
WORKDIR /app 

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
# define env variable
ENV FLASK_APP app.py

CMD ["flask","run","--host=0.0.0.0"]



