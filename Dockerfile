FROM python:3
EXPOSE 8080
ADD FibonacciHttp.py /
ADD Fibonacci.py /
RUN pip install pystrich
RUN pip install Flask
RUN pip install mimerender
CMD [ "python", "./FibonacciHttp.py" ]
