user : habusaya@gmail.com
pass : admin123456


#mysql
user : root
pass : 123456
dbname : django_journal


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_journal',
        'USER': 'root',
        'PASSWORD': '123456'
    }
}


#url
203.157.172.12:8899

nohup python3 manage.py runserver 0.0.0.0:3333 &
cat nohup.out


#How to upload github
git add --all
git commit -m "update v.11_02_2566"
git push -u origin main
# git push -u origin master


ref: https://itsourcecode.com/free-projects/python-projects/online-journal-management-system-project-in-django-with-source-code/#google_vignette


