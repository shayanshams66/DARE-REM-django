
01/27/2015
1. Installation of dare_rem_django_site with pinax-project-account is as follows
a. django 1.7.x needs python 2.7
b. create virtualenv venv-dare-rem-django
c. needs to run the command with sudo
d. steps.
    >  sudo venv-dare-rem-django/bin/pip install Django
    >  sudo venv-dare-rem-django/bin/django-admin startproject
     --template=https://github.com/pinax/pinax-project-account/zipball/master
     dare_rem_django_site
    >  cd dare_rem_django_site/
    >  sudo ../venv-dare-rem-django/bin/pip install -r requirements.txt
    >  sudo ../venv-dare-rem-django/bin/python2.7 manage.py migrate
    >  sudo ../venv-dare-rem-django/bin/python2.7 manage.py loaddata sites
    >  sudo ../venv-dare-rem-django/bin/python2.7 manage.py createsuperuser
    >  sudo ../venv-dare-rem-django/bin/python2.7 manage.py runserver 8100

use the following command to start

sudo venv-dare-rem-django/bin/python2.7 dare_rem_django_site/manage.py
runserver 130.39.22.155:8100


2. Configure apache for running django site using the port 8100 (this is one
of ports allowed for TMZ zone systems of LSU)
 see http.conf

3. admin : dare_rem_admin
   password : dare2015


4. To start DARE-REM (devel version), copy the following and run it in the
command line.

sudo /home/cctsg/software/DARE-REM-django/venv-dare-rem-django/bin/python2.7 /home/cctsg/software/DARE-REM-django/dare_rem_django_site/manage.py runserver dare.cct.lsu.edu:8100
