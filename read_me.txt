This is a basic hotel website

u need to set up a local_settings file with these parameters:
SECRET_KEY
EMAIL_HOST 
EMAIL_HOST_USER
EMAIL_HOST_PASSWORD

make sure your on the hotel/hotel file path before you use any of the commands.
some usefull commmans:

to run server:
python manage.py runserver

to make an admin user:
python manage.py createsuperuser