FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

MAINTAINER Iván Kuzel

# create root directory for our project in the container
RUN mkdir /code

# Set the working directory to /code
WORKDIR /code

COPY requirements.txt /code/

# Copy the current directory contents into the container at /code
ADD . /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
