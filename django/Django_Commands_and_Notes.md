# Django Useful Commands and Notes

## Installing Django

To create a Python environment that can handle Django, enter the command:

**Mac/Linux:**
> python3 -m venv environment_name

**Windows:**
> python -m venv environment_name

and navigate to the folder in CMD. Then run:

> pip install Django==2.2.4

***

## Starting Django

To create a Django project, start with the Django environment enabled and type in the console

>django-admin startproject project_name

Django projects come pre-installed with certain Python files that will be needed in the future

Django projects need apps, navigate inside the new project file and write in the CMD

> python manage.py startapp app_name

There should be a new folder with the app's name and several other files within that folder. It is missing certain key files for building a website, which will be added later.
Also, an app's name cannot be the projects name, since Django automatically creates a folder with the project's name that contains key files.

Finally, in the urls.py of the project name folder add **include** to the list of imports and add the app inside the urlpatterns list by writing

```python
    from django.urls import path, include

    path('', include('app_name.urls'))
```
And add the app to the list of INSTALLED_APPS in settings.py

Our app does not have have urls.py inside of it by default so that will need to be added. This file should be set up like so:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
]
```

The import here tells urls to look for functions in views, their names shown after the dot after views, when a specific url path is called. Here, the url path of '', or '/' (both mean the same thing but in the url it will be '/') will call upon the function *home* in views.py when visited. The file also needs to import views so it can see these functions.

The views.py file comes pre-installed, but is blank except for a single import line for *render*. It should be set up like so:

```python
from django.shortcuts import render, redirect, HttpRequest, JsonResponse

def home(request):
    return HttpRequest(request, "Hello")
```

Though not with those exact imports. All methods must take in **request** as an argument.

All four of those imported commands can be used after a return statement go give something for the client to view after making a **request** to the server. Only **redirect** does not have to also return **request** in its first argument. For what each does:

- render
    - Displays an HTML webpage
    - request and the HTML file must be passed in as arguments. Any variables passed into the HTML may be declared as arguments at the end.
- redirect
    - redirects to a specified route that should be in urls.py
    - **MUST** include the intitial forward slash ('/') that begins each url, unlike path declarations
- HttpRequest
    - Returns a string to be displayed on a webpage. Won't see much use.
- JsonRequest
    - Returns a JSON object. Useful for APIs and other methods of sending data.

Remember to only import what you will use, not everything.

In order to display html, html files must be placed in a folder called *templates* inside the app folder, which is not automatically created. For CSS and JavaScript files, they must be stored in another separate folder from *templates*, called *static*. To access them in the html, in the header, you need to write:

```HTML
    {% load static %}
    <link rel="stylesheet" href="{% static 'styles.css' %}">
    <script type = "text/javascript" src="{% static 'script.js' %}">
```

Note that if CSS or JavaScript files are contains in directories inside the static folder, they must be specified in the single quotes before the name of the file being called upon.

In order to start your server write in console:

 > python manage.py runserver

As long as no errors occur, head to localhost//:8000/ to see what views.home will display. Press CTRL+C to close the server.

If you make changes to urls or views, the server will automatically refresh to apply those updates. This will not always be the case for every file type, however.

If you have functionalities in other paths, say:

```python
    path('other_path', views.display),
```

Then you need to head to localhost//:8000/other_path to check on the functionality of that page.

***

## Forms and POST requests

If you want the user to be able to provide inputs to a webpage and bring interactivity to a page, you are going to need to use a form and be able to process and store any data it shares.

Forms must be set up like so:

```HTML
<form action = '/process_route' method = 'post'>
    <input type = 'text' name = 'field'>
    <button type = 'submit'>Submit</button>
</form>
```

- action
    - Which route processes the data. When the submit button is pressed, the page will redirect to that processing site
- method
    - Needs to be set to *post* otherwise it will be a *get* request, which can't post data to the server.
- Input elements
    - Needed for retriving data. Are referenced by their *name* fields.
- A *type submit* button or input
    - Will submit the data to the specificed route.

There is a issue in the processing route in that, if the user is stuck in the route processing the data and hits refresh, they will resubmit the form again. This can do anything from creating two nearly identical users to charging someone's credit card twice. To get around this, the route must return a redirect after it is done processing the data, that way a refresh will not cause the form to be resubmitted.

However, a redirect cannot return extra variables after it's initial argument, unlike render. This creates a problem where only the processing function will be aware that the data exists, while the other functions will be unable to see the data and use it in their own functionalities. To solve this, we need to use sessions.

***

## Sessions

In order to gain access to sessions, go back to the CMD, while the environment is active and you are inside the project folder and type:

> python manage.py migrate

The console should migrate a session variable for you to use.

A session is technically a Python dictionary, and so must be accessed within the Python code like it is a dictionary.

- request.session['key']
    - gets value assigned to said key
- request.session['key'] == value
    -  assigns that key that value or creates that key with that value if it currently does not exist.
- del request.session['key']
    - deletes the key, unless it doesn't exist. Then it throws a KeyError. Use with *try* and *except* so you don't crash and control what happens when the key doesn't exist.

When accessing keys inside the HTML file using Django's template language (You're likely using {{}}), use dot notation only to separate the different parts and remove the brackets and quotes.

If a session key holds a list that is being modified, use

```python
    request.session.save()
```

To ensure the list changes get properly updated.

To assign post request values inside the Python code, do

```python
    request.session['key'] == request.POST['name']
```

The POST here is case sensitive.

Additionally, different forms that both give post request must be distinguished by a

```HTML
    <input type = 'hidden' name = "which_form" value = 'x'>
```

Which can be read and stored by the session and be used in an if statement to determine different handlings of each form. Just note that hidden inputs are visible on the source page and their name and values can be edited, which can lead to some unintended or malicious consequences.

***

## Django ORM

An ORM is an Object Relational Manager, which is used to translate database rows into instances of Python classes. Each class will contain variables as fields and built-in methods that preform SQL Queries in the background. Also addresses security concerns by sanitizing user input and preventing SQL injection attacks.

The user input sanitation is not a part of all frameworks, so check to make sure. Sanitation is required to prevent script injection.

ORM relies on models, which are made in the models.py file automatically set up by Django. The class essentially allows you to access different rows of a table. Each model should start like so:

```python
    from django.db import models
    
    class className(models.Model):
```

These classes do not need an __init__ method.

Each entity (essentially our table column for our row) has its own variable and it's assignment line with a field specified.

- CharField(max_length=num); max_length sets how many characters the field can hold
- TextField(); like CharField but with no max_length requirement
- IntegerField(); holds an integer value
- DecimalField(max_digits=int1, decimal_places=int2); Hold a decimal number, but with a set number of total digits and set number of decimal places to the right. max_digits must be greater than decimal_places.
- BooleanField(); hold a boolean value
- DateTimeField(); saves the date and time as a datetime object. Also has two useful optional parameters:
    - auto_now_add = True: Saves Date+Time when object was created
    - auto_now = True: Saves Date+time when object is modified

Models do not need a field for their ID since it is automatically assigned by Django ORM and saved into its SQLite database.

Every time a change is made to the model or a model is created, in the Python Django environment input:

>python manage.py makemigrations

If makemigrations completes without errors, run the migrate commmand.

makemigrations ensures Django can understand the code within the model while migrate sets the changes in stone. Correct any errors identified by makemigrations before migrating!

NEVER delete migration files and always do 'makemigrations' and 'migrate' in that order when models.py is changed (except for a certain change discussed later)

If a model class is changed after it has already been updated with a new field, Python will throw an error because now that field in the older entries will be null. Django will give you two options to resolve this in the command prompt (Type 1 or 2 to select one)
- Option 1
    - Provide a default value to Django, which it will automatically assign to all previous entries before the change.
- Option 2
    - Provide a default value through models.py by passing (default=) into the arguments or allow it to be nullable (null=True)

There is a third secret option that requires manually deleting db.sqlite3, app_name/migrations and app_name/__pycache and then doing your makemigrations app_name and migrate commands again, but this is the nuclear option and should only be done if the database becomes corrupted or you're SoL.

Django comes prepackages with SQLite, but it should be switched to SQL when deployed.

Regardless, Django ORM queries and models will be the same not matter which database is being accessed.

To directly access and test models, use the Django shell:

>python manage.py shell

This will change the command line to >>>

Here, do:

> from app_name.models import *

Note that * imports everything, which is discoraged for everything other than testing because:
- Namespace collisions can occur
- Import may be inefficient because of how many things must be imported
- Doesn't explicitly state what is being imported, so you don't know what methods are exactly available to you

You can also use DB Browser to look at the db.sqlite3 file and edit it.

***

## Django ORM CRUD Commands

Useful commands to use within views.py to edit and access databases. Stands for Creating Reading Updating Deleting.

- Creating
    - class_name.objects.create(field1 = "value of field1", field2 = "value of field2", etc.)
- Reading (All these methods return an object, and so must be instanced with a variable assignment to access/edit)
    - class_name.objects.first(): Gets first record.
    - class_name.objects.last(): Gets last record.
    - class_name.objects.get(id = #): Gets object with id of # (Works with other entities defined in the model!)
    - class_name.objects.all(): Gets a list of all the objects that currently exist in the database
    - class_name.objects.filter(field1 = 'value'): Gets a list of all records with a field matching that value (or an empty list if there are none)
    - class_name.objects.exclude(field1 = 'value'): Gets a list of all records with a field that does not match that value (or an empty list if there are none)
- Updating
    ```python
        c = class_name.objects.get(id=num)
        c.fieldname = "new value for fieldname"
        c.save()
    ```
- Deleting
    ```python
        c = class_name.objects.get(id=num)
        c.delete()
    ```

Other useful commands:

- Displaying records:
    ```python
        class_name.objects.get(id=num)__dict__
    ```
    - Shows all values recorded as a dictionary
    ```python
        class_name.objects.get(id=num).values()
    ```
    - Shows all values of a QuerySet

- Ordering records
    ```python
        class_name.objects.all().order_by("field_name")
    ```
    - Orders by field provided, ascending
    ```python
        class_name.objects.all().order_by("-field_name")
    ```
    - Orders by field provided, descending

If you wish to change how models display, you have to override the default __str__ method

```python
    def __str__ (self):
        return f"<class object: {self.entity}...>"
```

To ensure our controller (views.py) knows about our model, do:

```python
    from .models import class_name
```

If you want to use data from the model in an HTML file, you need to pass in either the individual object you want accessed OR the entire list of objects in a dictionary.

```python
    context = {
        "all_users" : User.objects.all()
    }
    return render(request, 'index.html', context)
```

***

## One to Many Relationship

A model can hold many of another model through a One to Many relationship.

This is done by giving the model that will contain the "many" other models with a ForeignKey() field

For example, if you wanted a Book that could hold many Author models, you'd put, in the Book model:

```python
    author = models.ForeignKey(Author, related_name = "books", on_delete=models.CASCADE)
```

To assign this relationship, in the code or in the shell, we would need to do:

```python
    this_author = Author.objects.get(id=2)
    my_book = Book.objects.create(author = this_author)
```

Reading 'author' will return a query of author instances, which you can for loop through to access their data.

You can also filter this query so you only get specific authors assigned to this book.

The related_name field is used for reverse look-up. Much like how a book can access its authors, an author can access its books through the related_name. The author essentially has a ForiegnKey which is accessed via the related_name declared in Book.

***

## Many to Many Relationship

This relationship occurs when many records of one table can hold many records of another table. In SQL, this would be done using three tables, with one table being an intermediary having a one to many relationship with the two other tabels and designating which pairs of record ids go together. Django does not require a third relating model, and instead does this automatically using a ManyToManyField, which can go in either model.

```python
    fieldname = models.ManyToManyField(class_name, related_name="")
```

To assign relationships between models we use

```python
    first_model.fieldname.add(second_model)
```

To remove relationships between models we use

```python
    first_model.fieldname.remove(second_model)
```

These can be reversed so the second_model adds/removes first_model, but second_model will need to use related_name in place of fieldname.

.all() can also be used to see all related models.

## Validations

If we want to ensure data submitted by a form adheres to certain conditions before it is saved to a database, it needs to be validated.

Models have a hidden property

```python
    objects = models.Manager()
```

Which, if we want to implement validations, must be overwritten with a new model Manager containing our validation functions. These validation functions in the model Manager must pass 'self' as an argument as well as another argument for any POST data (We will pass in request.POST if we're validating forms). 

Note that models.Manager() makes all those CRUD commands available to the model, so the new Manager must inherit from models.Manager() to maintain the functionality of any old CRUD commands you have lying around. 

So, a Manager for Users would look like this:

```python
    class UserManager(models.Manager):
        def basic_validator(self, postData):
            errors = {}
            if condition:
                #...
                errors['error_name'] = "error here"
            return errors
```

Then within the code we override the original manager like so:

```python
    class User(models.Model):
        objects = UserManager()
```

When we want to validate some form data and display errors when they fail, we use a special django import called 'messages' and use this code:

```python
    from django.contrib import messages

    def register(request):
        errors = User.objects.basic_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            #code to run if we pass
```

To display in the HTML using Django template language we use:

```HTML
    {% if messages %}
        <ul class="messages">    
            {% for message in messages %}    
                <li>{{ message }}</li>    
            {% endfor %}
        </ul>
    {% endif %}
```

Regex functions can be used to check if an input matches a certain pattern. This fnctionality must be imported and used like so:

```python
    import re

    def basic_validator(self, postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']): 
            errors['email'] = "Invalid registered email address!"
```

Since we haven't learned about regex expressions (yet), you likely should look up some regex expressions on the internet or how it works.

For storing passwords inside databases, we want the password to be hashed, with a unique salt concatenated onto it for each user so the passwords are secure against any brute force attacks. 

Bcrypt, as of writing, is a  Python package that can do this though some simple methods, and is fast enough so that the user experience won't be slow but complex enough that a brute force attack will take many, many years to be successful.

To get Bcyrpt all you need to do is have pip version 20+ and in console type:

>pip install bcrypt

It can then be imported into your views

```python
    import bcrypt
```

Registration methods look something like this:

```python
    def register(request)
        pword = request.POST['pword']
        pw_hash = bcrypt.hashpw(pword.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            username = request.POST['username'],
            password=pw_hash)
        request.session['user_id'] = User.objects.last().id
        return redirect('/success')
```

and login methods look something like:

```python
    def login(request):
        login_attempt = User.objects.filter(username = request.POST['login_username'])
        if login_attempt:
            logged_user = login_attempt[0]
            if bcrypt.checkpw(request.POST['login_pword'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
```
-

```python
    bcrypt.checkpw(request.POST['login_pword'].encode(), logged_user.password.encode()):
```

This code snipet checks to see if the left side, when encoded by our hash function, matches our already hashed second argument.

Technically, when encoding, Bcrypt translates a Python unicode string into a byte string, and decode does this in reverse. This is because cryptographic functions only work on byte strings.