FROM python:3
ADD . /code
WORKDIR /code
RUN pip3 install pillow
RUN pip install pystrich
RUN pip install Flask
RUN pip install mimerender
CMD [ "python", "FibonacciHttp.py" ]
