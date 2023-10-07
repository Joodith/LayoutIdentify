FROM python:3.11
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt ./usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r ./usr/src/app/requirements.txt
COPY . /usr/src/app
EXPOSE 8000
CMD ["uvicorn","backend.app.main:main_app","--host 0.0.0.0","--port 8000"]