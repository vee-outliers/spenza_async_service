FROM python:3.11.0

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y \
    binutils \
    libproj-dev \
    gdal-bin \
    libgdal-dev

# Set GDAL_LIBRARY_PATH
ENV GDAL_LIBRARY_PATH /usr/lib/libgdal.so

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /spenza_async_service

COPY requirements.txt /spenza_async_service/

RUN pip install -r requirements.txt

COPY . /spenza_async_service/

EXPOSE 9000

CMD ["gunicorn", "--bind", "0.0.0.0:9000", "--workers", "2", "spenza_async_service.wsgi:application"]