# TalentManagement
**An HR consulting company website.**
<br>
<br>
<br>
> ## The challenge:
This project was conceived as a full working website for TalentManagement. The goal was to make clear and impactful messages in a modern way, explaining to potential customers who they are, what they do, and why they are the right choice.
<br><br>
The website should have a clean landing hero section, with other brief sections for the _About Us_ and _Why Us_, with links for a separate page with further explanation about those topics, and also a _Review_ section with a JavaScript carousel effect. The _Contact_ section would have a form in which users could write a message for the company, and their message would be stored on the database as the client also should receive an email with the message he just wrote (and not just a static email, confirming the database storage and email logic works as intended). Lastly, it should have an _Articles_ section displaying the two most recent articles added to the database, and users can both read the articles and access a different page for all the other articles.
<br><br>
> ## What I've done:
## Database setup
The first step of the development process was to design the database. To do so, I first made a diagram of the backend logic, which consisted of two unrelated tables, one for storing the articles (images, text, and all related components), and another for storing the contact form data (user email and message send, also with datetime). After that, I created a Django project inside a local virtual environment and started creating the database models and migrating them to the SQLite database for now.
<br><br>
## HTML, CSS and JavaScript
I then started writing the HTML for the homepage, one section at a time, and when I had most of the structure done, I began styling it. For that purpose, I chose the Bootstrap 5 CSS framework to speed up the development and imported it with their CDN. Eventually, I felt the need to change some of the CSS variables with Sass and some custom CSS in a style sheet. I also imported the Bootstrap JavaScript CDN and also wrote custom JavaScript for dynamic content loading (detecting which section of the website the user is at, and then loading it while the pre and post-sections remain hidden). This was possible due to CSS transform and transitions. I also had to ensure that the website remained responsive both in multiple window resolutions and on multiple phone screen sizes with CSS media queries.
<br><br>
## Django backends
As most of the homepage was structured and styled, I then started building other pages, sticking to Django's DRY (Don't Repeat Yourself) concept, which means that all URLs were named and the navigation was made with Django dynamic URL tags, rather than hard-coded static URLs, making it possible to create new pages, update or even change the whole backend logic without breaking the page href links. New pages also had little time to create due to Django's template inheritance and including elements from other HTML files (such as the navbar, for example).
<br><br>
Most of the logic was written in the Views file, having function-based views that queried the database for the latest articles written and showed the two last items in it (and querying all the articles for the _Articles_ page). The homepage also has a form that users can fill with their email and a message. Those data are stored in the database and an email is generated with Django's SMTP backends.
```
    if request.method == 'POST':
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Saving to the Database
        ContactForm.objects.create(
            email=email,
            message=message,
            date_sent=datetime.today()
        )
        
        # Sending the email
        send_mail('Hello from David Buckley',
                  f'Hey there, {email}, it worked! You are receiving this email to confirm the following message has reached us: \n"{message}". \nThanks for using my website!\n\nBest regards, \nDavid Buckley.',
                  'settings.EMAIL_HOST_USER',
                  [email],
                  fail_silently=False)
        messages.success(request, 'Email sent!')
        return redirect('home')
```
## PostgreSQL and AWS S3 static files storage
At a production level, static files such as CSS and JavaScript files, images, videos, and future image uploads, none of those should be stored inside a project because of latency and security risks. Also, Django's default SQLite database is not suitable for real-life data storage when in production. For that reason, I created a PostgreSQL database in the cloud with AWS's RDS (Relational Database Services). For static files storage, I created an AWS S3 bucket, and also a User for IAM (Identity and Access Management) to connect to the bucket. The AWS connection was made with the ```django-storages``` python library.
<br><br>
## Setup for production
Django applications require some changes and a lot of carefulness when setting up for production because several critical sensitive data are stored in many parts of the project, so I created a ```.env``` file to store all sensitive data (such as email passwords, project secret key, allowed hosts, AWS secret key, aws access key, and so on). I also made a ```.gitignore``` file and added the ```.env``` file to it, and also the virtual environment and the ```__pyinit__``` folder for safe git commits and pushes. All sensitive data is safe because of the ```python-decouple``` library.
```
# Access environment variables
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool, default=False)
ALLOWED_HOSTS = list(config('ALLOWED_HOSTS'))
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_DEFAULT_ACL = config('AWS_DEFAULT_ACL')
AWS_S3_CUSTOM_DOMAIN = config('AWS_S3_CUSTOM_DOMAIN')
```
Lastly, because of maintenance costs, I eventually had to revert to the SQLite database and local static files storage, but to change it, it is only needed to create another S3 bucket, another PostgreSQL database, run the migrations, add the path to the bucket's ```staticfiles```, change ```DEBUG``` to ```True``` and deploy it to the host of choice.
<br><br>
## How to run locally
1. **Clone this repository** <br>
Open your terminal and create a folder to hold the project with ```mkdir folder_name```. use ```cd folder_name``` and type ```git init```. Copy ```git clone https://github.com/davidbuckley96/talentmanagement.git``` and paste it on your terminal. Then, ```cd talentmanagement```.
2. **Inside the project folder, use ```pip install virtualenv```** <br>
3. **Type ```virtualenv myenv```, then ```myenv\scripts\activate```, and ```pip install -r requirements.txt```** <br>
4. **Open your python interpreter and open its terminal, then type again ```myenv\scripts\activate```**<br>
5. **Create a ```.env``` file on the root directory** <br>
6. **Copy the code below and paste it all inside ```.env```:** <br>
```
SECRET_KEY=random-secret-key-value
EMAIL_HOST_USER=your-address@email.com
EMAIL_HOST_PASSWORD=email-password
AWS_ACCESS_KEY_ID=NOT-NEEDED-IN-DEVELOPMENT
AWS_SECRET_ACCESS_KEY=NOT-NEEDED-IN-DEVELOPMENT
AWS_STORAGE_BUCKET_NAME=NOT-NEEDED-IN DEVELOPMENT
AWS_DEFAULT_ACL=None
AWS_S3_CUSTOM_DOMAIN=aws.amazon.com
ALLOWED_HOSTS=*
```
8. **Start the server in localhost with ```python manage.py runserver``` in your terminal** <br>
9. **Please note that due to security reasons the cloned repository's ```EMAIL_HOST_USER``` and ```EMAIL_HOST_PASSWORD``` variables are different from the production-ready project. For that reason, you can see a replica of the email which was supposed to be sent on the interpreter terminal; alternatively, you can set those variables to real email address and a SMTP provider app connection password (visit [Sign in with app passwords](https://support.google.com/mail/answer/185833?hl=en) if you don't know how to do so).**
<br><br><br><br>
Feel free to use this project as a study source, but not for commercial purposes.
<br><br>
David Buckley
<br>
January/2024




