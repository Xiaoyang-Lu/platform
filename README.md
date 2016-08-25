# Platform

I am luxiaoyang


This is a prototype for a platform which can dynamically generate fig(chart) according to the database. The platform is designed under django framework 1.9 with python 2.7.

# 1. Set Up
a) I am using pyhton2.7 make sure you are not using python3

b) "virtualenv" is strongly recommended. (https://virtualenv.pypa.io/en/stable/)

c) download the source code, and use "$pip install requirement.txt" to install the requirement package. If not using virtualenv then probablay will have package conflict issues.

# 2. Get Prepared

a) get familiar with django framework(https://docs.djangoproject.com/en/1.9/). 

There are two tutorial vedios which are very helpful(https://www.youtube.com/watch?v=KsLHt3D_jsE&list=PLEsfXFp6DpzRcd-q4vR5qAgOZUuz8041S, https://www.youtube.com/watch?v=yfgsklK_yFo&list=PLEsfXFp6DpzQFqfCur9CJ4QnKQTVXUsRy). The first is trydjango1.8 the second is trydjango1.9, these two vedio are very useful and strongly recommended.

b) get familiar with matplotlib(http://matplotlib.org/). This is used to create matplotlib fig obj dynamically.

c) get familiar with mpld3(http://mpld3.github.io/index.html). This is used to convert matplotlib fig obj to html dom obj.

# 3. Get Started

a) start the server by "$pyhton manage.py runserver" go to "http://127.0.0.1:8000/admin" login with "username:yhu82 password:1234567890pass" to check the database.

b) go to "http://127.0.0.1:8000/mat2web" to check the application

c) make modifications on the source code in src/demo/mat2web  
