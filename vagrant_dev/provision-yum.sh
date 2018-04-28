# provision yum
adduser vagup

yum update -y

# Install EPEL
yum install epel-release -y

# Install python3.6
yum install -y https://centos7.iuscommunity.org/ius-release.rpm
yum install -y https://download.postgresql.org/pub/repos/yum/10/redhat/rhel-7-x86_64/pgdg-centos10-10-2.noarch.rpm
yum install -y \
        postgresql10 \
        postgresql10-server \
        postgresql10-devel \
        postgresql10-contrib \
        gcc-c++ \
        unixODBC-devel \
        unixODBC \
        freetds-devel \
        nginx \
        policycoreutils-python \
        redis

# init postgresql database
/usr/pgsql-10/bin/postgresql-10-setup initdb
sudo systemctl enable postgresql-10
sudo systemctl start postgresql-10

sudo systemctl enable redis
sudo systemctl start redis

# create postgresql server
su - postgres -c "createuser --createdb --no-superuser --createrole --no-password vagrant"
su - vagrant -c "createdb -O vagrant vagup"