# rolebased-auth
Role Based Auth: In this, there are two types of users, one user is a superuser and other will be a simple user with only front-end authorizations.
* Installing Django and running the code: To install Django make sure pip is installed. After that step go ahead and write following in the terminal `pip install django`. 
This will download and intall the django latest version. After this step now go to the directory in which this django code is placed. Type the following command next: 
  - `python manage.py makemigrations` 
  - `python manage.py migrate` 
  - `python manage.py runserver` 
Now, after the final command the server will start running and notice that in the app directory there will be migrations files that are now created. Run any browser and go to the 127.0.0.1:8000/ or the any other port number allocated. The page will surely load.
### How it Works?
  - It contains a single model to store the users. It is a good practice to keep all the users in the same model and not scatter them around, in order to stay safe from attacks and also to keep things clean.
    It uses roles for the two users.
      - Doctor (is_doctor): The doctor is the superuser who can view all the data as well as perform CRUD on patient's data. For the doctor the permissions to view content are allowed using `has_perms()` and `has_module_perms()` in the model. 
      - Patient (is_patient): Patient is not a superuser and uses the same model.
   - The page view depends on which user has logged in. If the doctor has logged in then the page for Doctor will show up, otherwise Patient's page will show up. Both pages contains different data.
   - Alternative way could be to use different apps for different users and handle them in their own app with their own models. That method will work fine if the project is not very big and complex and no scope of scalability in future, otherwise there are potential chances that it'll break down or clutter up.
* URLs: 
  1. 127.0.0.1:8000/login : This is for the user login page 
  2. 127.0.0.1:8000/doctor/register: Sign-up for the Doctor
  3. 127.0.0.1:8000/ : This is the Home page
  4. 127.0.0.1:8000/patient/register: Sign-up for the Patient 
  5. 127.0.0.1:8000/account/patient : Post login page for Patient
  6. 127.0.0.1:8000/account/doctor : Post login page for the Doctor
  7. 127.0.0.1:8000/logout: Handles logout function

* Methods and Classes: All the methods and classes are written inside the views.py which renders the templates as well as performs basic queries on the database too. We can say it's the heart of the project. Read more here: https://docs.djangoproject.com/en/3.0/topics/http/views/

* URL's in the project: Every URL is mapped to a view method or class, like so: `path(, <method_name/class_name>, )`. For each URL path on goes to, a view method is triggered which renders the corresponding HTML page. Read more here: https://docs.djangoproject.com/en/3.0/topics/http/urls/

* How it achieves custom user authentication? It uses a custom user model(inside models.py) as opposed to the base "User" model provided by Django. The class AbstractBaseUser has been extended and changes are made into it. Originally usernames is used to signup a user but here "email" is taken for this process. Read more here: https://docs.djangoproject.com/en/3.0/ref/contrib/auth/

* Django templating: The Django template language is Django’s own template system. Until Django 1.8 it was the only built-in option available. It’s a good template library even though it’s fairly opinionated and sports a few idiosyncrasies. If you don’t have a pressing reason to choose another backend, you should use the DTL, especially if you’re writing a pluggable application and you intend to distribute templates. In a nutshell it allows to run django code inside the HTML pages. Read more here: https://docs.djangoproject.com/en/3.0/topics/templates/

* Django Database api: Django automatically gives you a database-abstraction API that lets you create, retrieve, update and delete objects. An example that has been used in the project is .objects.all(). This fetches the entire instance of the model. Read more here: https://docs.djangoproject.com/en/3.0/topics/db/queries/

> Footnote: The project uses Django version 3.0 - install pillow for including images in the models (write `pip install pillow` in the terminal). Other functionalities will be added soon.
