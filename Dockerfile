FROM python:3.9

WORKDIR /app

COPY ./bin/models/u2net.onnx /root/.u2net/u2net.onnx

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]