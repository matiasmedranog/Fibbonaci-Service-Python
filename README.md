# Fibbonaci-Service-Python
Rest Service - Python - Fibonacci serie

----------------------------------------

Execute this with Python:
```
python FibonacciHttp.py
```

----------------------------------------

Execute this as Docker Container: (With Docker Compose)
- Run Container:
```
docker-compose up
```

- Run Container as Daemon:
```
docker-compose up -d
```
----------------------------------------

And send a test curl:
```
curl -X GET http://localhost:5000/10
curl -X GET http://localhost:5000/11
curl -X GET http://localhost:5000/12
curl -X GET http://localhost:5000/[Nº]
```
