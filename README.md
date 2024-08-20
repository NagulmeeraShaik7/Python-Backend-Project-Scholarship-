                  
Scholarship Project
--------------------------------------------------

* Step1: In C drive create a folder **myproject**

* Step2: On url type **cmd** commad prompt will be open 

      ```C:\myproject>```


* Step3: Create Virtual Environment ``pipenv shell`` 

        **C:\myproject>pipenv shell**

   **(myproject-venv) C:\myproject>** 

* Step4:Install ```Django``` 

     ```pipenv install django``` 

    **(myproject-venv) C:\myproject>**```pipenv install django```  

* Step5:
     **(myproject-venv) C:\myproject>**```django-admin     startproject scholarship```

* Step 6:
    **(myproject-venv) C:\myproject>**

    **(myproject-venv) C:\myproject>**```cd schlorship```


    **(myproject-venv) C:\myproject\schlorship>** 

* Step7: 

    **(myproject-venv) C:\myproject\schlorship>** ```py manage.py startapp student``` 

* Step8:

   **(myproject-venv)C:\myproject\schlorship>**

   **(myproject-venv)C:\myproject\schlorship>**```code .```

   Total project is opened with VS code 

* Step9:

   *Click schlorship folder*

   *Click* ```settings.py``` *file*

   Scroll down

 INSTALLED_APPS = [

    'django.contrib.admin',

    'django.contrib.auth',

    'django.contrib.contenttypes',

    'django.contrib.sessions',

    'django.contrib.messages',

    'django.contrib.staticfiles',

    'student',                              #update this line
]


  **Database Configuration Steps** 

* Step1:
  Open postgres software ``[ pgAdmin ]``
  create database ``schlorship`` 

* Step2:
   In VS code , click ``Settings.py``
   scroll down


 DATABASES = {

    'default': {
        
        'ENGINE': 'django.db.backends.postgresql', #update

        'NAME': 'schlorship',        #update

        'USER':'postgres',           #update

        'PASSWORD':7755,             #update

        'HOST':'localhost'           #update
    }
}


**Model Creation** 

* Step1:

   In vs code  click ```student``` folder
   click ```models.py``` file


from django.db import models

#Create your models here.



class Student(models.Model):

    fullname = models.CharField(max_length=30)
    hallticket = models.CharField(max_length=30)
    clgname = models.CharField(max_length=30)
    aadharno = models.CharField(max_length=30)
    mobile = models.CharField(max_length=30)
    amount = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.fullname},{self.hallticket},{self.clgname}"




**Register with Admin** 

* Step1 : Open command Prompt

  **(myproject-venv) C:\myproject\schlorship>** 

* Step2:  Install third-party package

   **(myproject-venv) C:\myproject\schlorship>**```pipenv install psycopg2```
* Step3:
   **(myproject-venv) C:\myproject\schlorship>**```py manage.py makemigrations```


  **(myproject-venv) D:\myproject\schlorship>**```py manage.py migrate``` 
* Step4 : 

  **(myproject-venv) C:\myproject\schlorship>**```py manage.py createsuperuser```

    give details super user is created 

* Step5:
  **(myproject-venv) C:\myproject\schlorship>**```py manage.py runserver```

  open this with browser

  http://127.0.0.1:8000/admin 

  * USER: admin 
  * PASSWORD: 7755
* Step 6:

   In VScode click ```student``` folder
   click ```admin.py```

   from django.contrib import admin

   from student import models

   #Register your models here.


   admin.site.register(models.Student)


* Step7:

    referesh url http://127.0.0.1:8000/admin

  Add some students details automatically will be stored in database and check and practice 



**Refer below video** 




  <video controls src="Bootstrap demo - Google Chrome 2024-08-20 16-49-52.mp4" title="Title"></video>









