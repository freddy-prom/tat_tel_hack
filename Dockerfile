FROM python:3.8-slim-buster
COPY . /shop
RUN pip install -e '/shop'
RUN ln -snf /usr/share/python3/app/bin/shop-* /usr/bin/
CMD shop-db upgrade head && shop-api