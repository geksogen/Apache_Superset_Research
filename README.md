# Apache_Superset_Research
* Ubuntu v22.04 (2CPU, 40GB HDD, 8Gb RAM)

#### Pre config VM
```Bash
sudo apt update
sudo apt upgrade
sudo apt -y install python3-pip

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
```

#### Install Apache Superset Docker-Compose
```Bash
git clone https://github.com/apache/superset.git
cd superset
docker compose up -d
docker-compose down -v
docker compose up -d
```
#### Install Apache Superset Docker
```Bash
docker network create app_net
docker run -d --rm --net=app_net -p 80:8080 --name superset apache/superset
docker exec -it superset superset fab create-admin --username admin --firstname Superset --lastname Admin --email test@mail.ru --password hfy67*fjtyh
docker exec -it superset superset db upgrade
docker exec -it superset superset init
```
### Install mysql
```Bash
mkdir /tmp/mysql-data
docker run --name basic-mysql -d --rm -v /tmp/mysql-data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=ANSKk08aPEDbFjDO -e MYSQL_DATABASE=testing -p 3306:3306 -it mysql:8.0
docker exec -it basic-mysql /bin/bash
mysql -uroot -p
show databases;
use website_traffic;
select * from traffic;
```
### Add data source and gen traffic
```Bash
pip install mysql-connector-python
python3 data_source_setup.py
python3 gen_traffic.py
  
```
### Apache Airflow Setup
```Bash
sudo apt-get install build-essential libssl-dev libffi-dev python3-dev python3-pip libsasl2-dev libldap2-dev default-libmysqlclient-dev
pip3 install requests==2.26.0
pip3 install apache-airflow[cncf.kubernetes]
#
export AIRFLOW_HOME=~/airflow
mkdir /root/airflow/dags
pip3 install "apache-airflow==2.6.1" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.6.1/constraints-3.10.txt"
airflow db init
#airflow db reset
#airflow db init
airflow users create --username admin --password admin --firstname admin --lastname admin --role Admin --email test@mail.ru
airflow users list
#
airflow standalone
mv dag.py /root/airflow/dags
```