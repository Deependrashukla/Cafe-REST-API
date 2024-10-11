# To run dockerfile {docker build -t you_image_name .},  . is showing where is your dockerfile . --> (current directory) 
# to run an image from command line {docker run -p 5005:5000 rest-api} -p(port) (port on pc):(port on docker) image_name
# FROM python:3.10  it is docker image, required before using pyodbc dependencies.
# it (3.10-slim-buster) is required to solve pyodbc dependencies.


FROM python:3.10-slim-buster
EXPOSE 5000
WORKDIR /app
COPY . .

# To install pyodbc driver
ENV ACCEPT_EULA=Y
RUN apt-get update -y && apt-get update \
  && apt-get install -y --no-install-recommends curl gcc g++ gnupg unixodbc-dev

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
  && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
  && apt-get update \
  && apt-get install -y --no-install-recommends --allow-unauthenticated msodbcsql17 mssql-tools \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile \
  && echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc


RUN pip install -r requirements.txt
CMD ["flask", "run", "--host", "0.0.0.0"]


