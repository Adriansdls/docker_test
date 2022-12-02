FROM python:3.7
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p app
COPY app.py /app
WORKDIR /app
EXPOSE 8080
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]