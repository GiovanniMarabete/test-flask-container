FROM python:latest
LABEL key="Giovanni Marabete"
COPY app /app
WORKDIR /app
RUN pip install -r requirements.txt
# EXPOSE 80
# EXPOSE 5000
CMD ["python", "app.py"]