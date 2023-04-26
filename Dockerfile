#Use an official python runtime
FROM python:3.7-alpine

#Set the working directory
WORKDIR /project
COPY . /project

#Copy the code base in the current directory to the container /app
COPY requirements.txt requirements.txt

#Upgrade pip
RUN pip install --upgrade pip

#install needed packages
RUN pip install -r requirements.txt

#Set the default command to run when starting the container
CMD ["python", "wsgi.py"]

