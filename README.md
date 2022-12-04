How to run the application:
```
sudo docker-compose up -d
```
Migrate all apps:
```
sudo docker-compose exec web python manage.py makemigrations reviews users
sudo docker-compose exec web python manage.py migrate
```
Create a superuser:
```
sudo docker-compose exec web python manage.py createsuperuser
```
```
sudo docker-compose exec web python manage.py collectstatic --no-input
```
