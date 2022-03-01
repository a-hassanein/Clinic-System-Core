# Clinic-System-Core
Clinic System  Backend API Using Django Restfull Framework 

# Installtion
- pip install django==3.2.10
- pip3 install djangorestframework
- pip install django-mathfilters
- pip install psycopg2

# DataBase
- sudo -i -u postgres
- create database clinic;
- create user clinicuser with password'123';
- alter user clinicuser with superuser;
- grant all privileges on database clinic to clinicuser;
- \q
- psql -h localhost -U clinicuser clinic
