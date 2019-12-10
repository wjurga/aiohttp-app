FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/aiohttp-app/src


COPY requirements.txt /opt/services/aiohttp-app/src/
WORKDIR /opt/services/aiohttp-app/src
RUN pip install -r requirements.txt
COPY . /opt/services/aiohttp-app/src
EXPOSE 8080
CMD ["python", "app.py"]
