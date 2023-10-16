FROM python:3.10

ENV APP_ROOT /app
WORKDIR $APP_ROOT
COPY packages/partner-api/requirements.txt $APP_ROOT/requirements.txt
RUN pip install --no-cache-dir --upgrade -r $APP_ROOT/requirements.txt
COPY packages/partner-api $APP_ROOT/

# CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80","--reload"]
CMD ["python", "main.py"]
# CMD [ "tail", "-f", "/dev/null" ]