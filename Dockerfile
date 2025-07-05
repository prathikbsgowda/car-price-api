FROM python:3.10

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=7860


RUN python train_model.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "7860"]
