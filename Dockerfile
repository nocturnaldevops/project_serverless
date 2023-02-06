FROM python
ADD . /code
WORKDIR /code
RUN pip install flask
EXPOSE 5050
CMD python main.py
