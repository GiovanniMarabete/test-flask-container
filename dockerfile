FROM python:3-alpine
LABEL key="Giovanni Marabete"
COPY app /app
WORKDIR /app
RUN pip3 install -r requirements.txt
# EXPOSE 80
CMD ["python", "app.py"]