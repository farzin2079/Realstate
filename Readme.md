# Realstate

- [Realstate](#realstate)
  - [Discraptions](#discraptions)
  - [Installation](#installation)
  - [Distinctiveness and Complexit](#distinctiveness-and-complexit)
    - [Usage](#usage)
    - [coding](#coding)
    - [account](#account)
    - [propert](#propert)

## Discraptions

Realstate is a web application that allows users to search for real estate properties based on their preferences. Users can search for properties by price range, property type, and other criteria. The application also allows users to save their in watchlist properties.

## Installation

To install Realstate, follow these steps:

Install the required dependencies by running
pip install -r requirements.txt

Set up the database by running `python manage.py makemigrations` and `python manage.py migrate`
Start the development server by running `python manage.py runserver`

## Distinctiveness and Complexit

### Usage

To use Real State, follow these steps:

Open your web browser and navigate to <http://localhost:8000>
this URL guide you to login page if you don't have account then down of form is a link __(I don't have account)__ send you to register page.
register page have 4 field for username, E-mail, password and confirmation. there is an eye if user click on this password show and if user click again password transfer to dots. after user regiter with uniq username and same password and confirmation change direct to they account.
in account they can chabge they informations and profile details and saved. in right of card is four tab by click each of theme card change and show that info category. in watchlist tab they can see they watchlist. in peroperty tab they can see property they submited.
in home navtab can see every peoperty click on theme and see details. in add new property can add new property by fill the fields.
and in category dropdown users can filter the propertys.

### coding

this project have 2 app fist let's look at settings.py in project folder or realstate folder

- realstate/setting.py:
  - add my apps in instaled app in line 22, 23
  - change template Dirs to `BASE_DIR/templates`
  - insert new setting for static in line 110 to 114 and do `python manage.py collectstatic`
  - add media folder root and url in line 122, 123
  - import massega from django and cutomize setting in line 129 to end

project apps is __account__ and __property__

### account

- account/models.py:
        i import `User` base model from django then create `Profile` model.
        Profile model have an user field that is a ForeignKey field.
        email and username field when user created, signals.py automate fill those field with what ever user add in register page.
        other fields is obvious.
- account/forms.py
        create a custom form for some Profile model field
- account/signals.py
        every time new User create signals fire and create a profile and connect Profile.user, Profile.username and Profile.email field to new user details.
        for firing signals i add code below to apps.py in account folder.

        ```python

        def ready(self):
            import account.signals
        ```

- account/views.py
        functions:
          1. index:
            if request method is get return user profile and cutomized Profile model form and if method equal to post then update user profile with modelform.
          2. login_view, logout_view, register:
            all this function i copy from Previous project like commerce, mail and etc.
          3. profile:
            get user id and  get user model find user Profile and user propertys and return all those

### propert

- property/models.py:
        import User model from django and Profile from account app. create Property model and category model
        category have only two field. first name of category. secend propertys of that category.
        Property's field is obvious only vpm mean value per Square meters.

- property/forms.py
        create a custom form for some Property model field and give a special class to each of theme.

- property/views.py
        1. index:
            return all properys in pagination
        2. datails:
            take a property id and get and retuned that pecific property.
        3. category:
            return all property is related to selected category
        4. addprop:
            if method equal to post add new prop using modelform and add new property to category and user profile else return property custom form
        5. watchlist:
            by using javascript in front-end send request to watchlist function if method equal to post add or remove propery and profile to or from watchlist fields else return just a json to show is user have property in user watchlist.
        6. delete:
            take id in Post request and delete selected property
