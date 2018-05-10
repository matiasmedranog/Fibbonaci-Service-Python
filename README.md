# Fibbonaci-Service-Python
Rest Service - Python - Fibonacci serie

Execute this with Python:
```
python FibonacciHttp.py
```

Execute this as Docker Container:
```
sudo docker run pythonfibonacci
```

----------------------------------------

And send a test curl:
```
curl -i -H "Accept: application/json" localhost:8080/9
curl -i -H "Accept: application/json" localhost:8080/10
curl -i -H "Accept: application/json" localhost:8080/11
curl -i -H "Accept: application/json" localhost:8080/[Nº]
```
