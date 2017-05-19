from flask import Flask, render_template, url_for, request, redirect, \
        session, make_response, g, flash, abort, Markup

from flask.ext.sqlalchemy import SQLAlchemy

from flask.ext.security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user

from datetime import datetime, timedelta, date

import requests, time, dateutil.parser, pytz, os, sqlite3

from flask.ext.mail import Message, Mail

from flask_wtf import Form, RecaptchaField
from werkzeug.utils import secure_filename
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask.ext.wtf import Form
from wtforms import TextField, IntegerField, DecimalField, StringField, SelectField, TextAreaField, SubmitField, BooleanField, validators
from wtforms.validators import Required, DataRequired, ValidationError
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField, EmailField
from flask.ext.admin.form import widgets

#from flask_celery import make_celery


#import pdfkit

#from flask_debugtoolbar import DebugToolbarExtension
import os, random, string


from flask_security.utils import encrypt_password
import flask_admin
from flask_admin.contrib import sqla
from flask_admin import helpers as admin_helpers

###########################################################################
################ invoke-rc.d rabbitmq-server start ########################
################ celery -A app.celery worker --loglevel=info ##############
###########################################################################
###########################################################################
################ settings
###########################################################################
###########################################################################

########################################################################
##    ###     ###       ###       ###     ### ##### ####    #####    ###
# ####### ########## ######### ######## ##### # ### ### ######## #######
##  #####   ######## ######### ######## ##### ## ## ### #    ####  #####
####  ### ########## ######### ######## ##### ### # ### ### #######  ###
#    ####     ###### ######### ######     ### ####  ####    ####    ####
########################################################################



# Create app
app = Flask(__name__)
# Import more settings in config.py
#app.config.from_pyfile('config.py')
# Make sure debug = False in production
db = SQLAlchemy(app)
#celery = make_celery(app)
#mail=Mail(app)
# Setup Flask-Mail

app.config.update(
	#Remember to change
    DEBUG = True,

    # Make sure the SECRET_KEY is bigger and r,andom and keep it somewhere safe,
    SECRET_KEY = 'XNQZXULEOLHWPJTHSISSFVZH',

    # Flask-Security config,
    SECURITY_URL_PREFIX = "/admin",
    SECURITY_PASSWORD_HASH = "pbkdf2_sha512",
    SECURITY_PASSWORD_SALT = "ATGUOHAELKiubahiughaerGOJAEGj",

    # Flask-Security features
    SECURITY_REGISTERABLE = True,
    SECURITY_SEND_REGISTER_EMAIL = True,
    SECURITY_RECOVERABLE = True,
    SECURITY_TRACKABLE = True,
    SECURITY_CONFIRMABLE = True,

    # Create in-memory database
    #dialect+driver://username:password@host:port/database,
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./prowler.db',
    SQLALCHEMY_POOL_RECYCLE = 299,
    SQLALCHEMY_ECHO = True,

    # Celery settings
    #CELERY_BROKER_URL = 'amqp://localhost//',
    #dialect+driver://username:password@host:port/database,
    #CELERY_BACKEND = 'sqlite:///' + DATABASE_FILE,
    CELERY_BROKER_URL = 'amqp://localhost//',
    #dialect+driver://username:password@host:port/database,
    CELERY_BACKEND = 'sqlite:///./prowler.db',

    # Flask-Security URLs, overridden because they don't put a / at the end,
    SECURITY_LOGIN_URL = "/login/",
    SECURITY_LOGOUT_URL = "/logout/",
    SECURITY_REGISTER_URL = "/register/",
    SECURITY_POST_LOGIN_VIEW = "/",
    SECURITY_POST_LOGOUT_VIEW = "/",
    SECURITY_POST_REGISTER_VIEW = "/",


    #EMAIL SETTINGS for google
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'reportprowlers@gmail.com',
    MAIL_PASSWORD = '123password123',
    MAIL_FAIL_SILENTLY = 'False',

    RECAPTCHA_PUBLIC_KEY ='6LcEzgoUAAAAAPz13uGi1Lo2ktDrmW-S-LrWYtGf',
    RECAPTCHA_PRIVATE_KEY ='6LcEzgoUAAAAAEWjonNP4y83h6vVgcPt0l63WX03',
    )

mail=Mail(app)

######################################################
# ##### #####   #####   ######     ### ########    ###
#  ###  #### ### #### ### #### ####### ####### #######
# # # # ### ##### ### #### ###   ##### ########  #####
# ## ## #### ### #### ### #### ####### ##########  ###
# ##### #####   #####   ######     ###     ###    ####
######################################################



# Creates a many to many relationship for roles and users
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


# User models
class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    last_login_at = db.Column(db.DateTime(), default=datetime.now())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(24))
    current_login_ip = db.Column(db.String(24))
    login_count = db.Column(db.Integer())

    def __str__(self):
        return self.email


# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.DateTime())
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    province = db.Column(db.String(55), default=None)
    areas = db.Column(db.String(255))
    company = db.Column(db.String(255))
    number_of_areas = db.Column(db.Integer)
    paid = db.Column(db.Boolean(), default=False)
    ref = db.Column(db.String(255))

    def __init__(self, date=date, name=name, email=email, province=province, areas=areas, company=company, number_of_areas=number_of_areas, paid=paid, ref=ref):
        self.date = date
        self.name = name
        self.email = email
        self.province = province
        self.areas = areas
        self.company = company
        self.number_of_areas = number_of_areas
        self.paid = paid
        self.ref= ref



class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    time = db.Column(db.DateTime(), default=datetime.now())
    reporter_email = db.Column(db.String(255))
    province = db.Column(db.String(55), default=None)
    area = db.Column(db.String(55), default=None)
    street = db.Column(db.String(55), default=None)
    tone = db.Column(db.String(55), default=None)
    age = db.Column(db.String(55), default=None)
    build = db.Column(db.String(55), default=None)
    height = db.Column(db.String(55), default=None)
    shirt = db.Column(db.String(55), default=None)
    pants = db.Column(db.String(55), default=None)
    shoes = db.Column(db.String(55), default=None)
    remarks = db.Column(db.String(255), default=None)

    def __init__(self, time=time, reporter_email=reporter_email, province=province, area=area, street=street, tone=tone, age=age, build=build, height=height,
        shirt=shirt, pants=pants, shoes=shoes, remarks=remarks):
        self.time = datetime.now()
        self.reporter_email = reporter_email
        self.province = province
        self.area = area
        self.street = street
        self.tone = tone
        self.age = age
        self.build = build
        self.height = height
        self.shirt = shirt
        self.pants = pants
        self.shoes = shoes
        self.remarks = remarks



class Vehicle(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    time = db.Column(db.DateTime(), default=datetime.now())
    reporter_email = db.Column(db.String(255))
    province = db.Column(db.String(55), default=None)
    area = db.Column(db.String(55), default=None)
    street = db.Column(db.String(55), default=None)
    colour = db.Column(db.String(55), default=None)
    registration = db.Column(db.String(55), default=None)
    occupants = db.Column(db.Integer(), default=None)
    make = db.Column(db.String(55), default=None)
    model = db.Column(db.String(55), default=None)
    remarks = db.Column(db.String(255), default=None)

    def __init__(self, time=time, reporter_email=reporter_email, province=province, area=area, street=street, colour=colour, registration=registration, occupants=occupants,
        make=make, model=model, remarks=remarks):
        self.time = datetime.now()
        self.reporter_email = reporter_email
        self.province = province
        self.area = area
        self.street = street
        self.colour = colour
        self.registration = registration
        self.occupants = occupants
        self.make = make
        self.model = model
        self.remarks = remarks


class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    time = db.Column(db.DateTime(), default=datetime.now())
    reporter_email = db.Column(db.String(255))
    province = db.Column(db.String(55), default=None)
    area = db.Column(db.String(55), default=None)
    street = db.Column(db.String(55), default=None)
    number_of_people = db.Column(db.Integer(), default=None)
    remarks =  db.Column(db.String(255), default=None)

    def __init__(self, time=time, reporter_email=reporter_email, province=province, area=area, street=street, number_of_people=number_of_people, remarks=remarks):
        self.time = datetime.now()
        self.reporter_email = reporter_email
        self.province = province
        self.area = area
        self.street = street
        self.number_of_people = number_of_people
        self.remarks = remarks

class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    time = db.Column(db.DateTime(), default=datetime.now())
    reporter_email = db.Column(db.String(255))
    province = db.Column(db.String(55), default=None)
    area = db.Column(db.String(55), default=None)
    street = db.Column(db.String(55), default=None)
    filename = db.Column(db.String(55), default=None)
    remarks =  db.Column(db.String(255), default=None)

    def __init__(self, time=time, reporter_email=reporter_email, province=province, area=area, street=street,filename=filename, remarks=remarks):
        self.time = datetime.now()
        self.reporter_email = reporter_email
        self.province = province
        self.area = area
        self.street = street
        self.filename = filename
        self.remarks = remarks




############################################################################################
# ##### #####   #####   ######     ### ####### ##### ###     ###     ### ####### ####    ###
#  ###  #### ### #### ### #### ####### ####### ##### ##### ##### ####### ####### ### #######
# # # # ### ##### ### #### ###   ##### ######## ### ###### #####   ##### ### ### ####  #####
# ## ## #### ### #### ### #### ####### ######### # ####### ##### ######## ## ## #######  ###
# ##### #####   #####   ######     ###     ###### ######     ###     ##### ### #####    ####
############################################################################################


# Create customized model view class
class AdminView(sqla.ModelView):
    column_exclude_list = ['password', ]
    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('superuser'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))

# Create admin
admin = flask_admin.Admin(
    app,
    'Report Prowlers',
    base_template='my_master.html',
    template_mode='bootstrap3',
)

# Add model views
admin.add_view(AdminView(Subscriber, db.session))
admin.add_view(AdminView(Role, db.session))
admin.add_view(AdminView(User, db.session))
admin.add_view(AdminView(Person, db.session))
admin.add_view(AdminView(Vehicle, db.session))
admin.add_view(AdminView(Group, db.session))
admin.add_view(AdminView(Image, db.session))

# define a context processor for merging flask-admin's template context into the
# flask-security views.
@security.context_processor
def security_context_processor():
    return dict(
        admin_base_template=admin.base_template,
        admin_view=admin.index_view,
        h=admin_helpers,
        get_url=url_for
    )

#############################################
#     #####   #####    #### ##### ####    ###
# ######## ### #### ### ###  ###  ### #######
#   ##### ##### ###    #### # # # ####  #####
# ######## ### #### ### ### ## ## ######  ###
# #########   ##### ### ### ##### ###    ####
#############################################

#class ContactForm(Form):
#    firstName = TextField('First Name', [validators.DataRequired("Enter your first name")])
#    lastName = TextField('Last Name', [validators.DataRequired("Enter your last name")])
#    email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
#    subject = TextField('Subject', [validators.DataRequired("What's the nature of your message?")])
#    message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
#    submit = SubmitField('Send')


# Contact Form
class ContactForm(Form):
    email = TextField('E-mail', [validators.DataRequired("Enter a valid email address"), validators.Email("Enter a valid email address")])
    message = TextAreaField('Message', [validators.DataRequired("Didn't you want to say something?")])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

# Prowler report form
class ReportPerson(Form):
    province = SelectField(u'Province', [validators.DataRequired("This Field is required")], choices=[('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Gauteng', 'Gauteng'), ('Western Cape', 'Western Cape'), ('Free State', 'Free State'), ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'), ('North west', 'North west'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ])
    area = TextField('Message', [validators.DataRequired("This field is required")])
    street = TextField('Street name')
    build = SelectField(u'Build', choices=[(' ', 'Build size (Optional)'),('slim', 'Slim'), ('medium', 'Medium'), ('large', 'Large')])
    height = SelectField(u'Height', choices=[(' ', 'Height (Optional)'),('short', 'Short'), ('medium', 'Medium'), ('tall', 'Tall')])
    tone = SelectField(u'Skin tone', choices=[(' ', 'Skin tone (Optional)'),('light', 'Light skin tone'), ('medium', 'Medium skin tone'), ('dark', 'Dark skin tone')])
    age = SelectField(u'Age', choices=[(' ', 'Approx age? (Optional)'),('teens', 'Teenager'), ('20-40', 'Twenty to Fourty'), ('40+', 'Forty +')])
    shirt = TextField('Shirt colour')
    pants = TextField('Pants colour')
    shoes = TextField('Shoes colour')
    remarks = TextAreaField('Any other details')
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

class ReportVehicle(Form):
    province = SelectField(u'Province', [validators.DataRequired("This Field is required")], choices=[('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Gauteng', 'Gauteng'), ('Western Cape', 'Western Cape'), ('Free State', 'Free State'), ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'), ('North west', 'North west'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ])
    area = TextField('Message', [validators.DataRequired("This field is required")])
    street = TextField('Street name')
    colour = TextField('Vehicle colour')
    registration = TextField('Registration number')
    occupants = TextField('Number of people in vehicle')
    make = TextField('Vehicle make')
    model = TextField('Vehicle model')
    remarks = TextAreaField('Any other details')
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

class ReportGroup(Form):
    province = SelectField(u'Province', [validators.DataRequired("This Field is required")], choices=[('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Gauteng', 'Gauteng'), ('Western Cape', 'Western Cape'), ('Free State', 'Free State'), ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'), ('North west', 'North west'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ])
    area = TextField('Message', [validators.DataRequired("This field is required")])
    street = TextField('Street name')
    number_of_people = TextField('How many people')
    remarks = TextAreaField('Any other details')
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')


class ReportImage(Form):
    province = SelectField(u'Province', [validators.DataRequired("This Field is required")], choices=[('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Gauteng', 'Gauteng'), ('Western Cape', 'Western Cape'), ('Free State', 'Free State'), ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'), ('North west', 'North west'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ])
    area = TextField('Message', [validators.DataRequired("This field is required")])
    street = TextField('Street name')
    photo = FileField('Your photo')
    # photo = FileField('image', validators=[FileRequired(),FileAllowed(['jpg', 'png'], 'Images only!')])
    remarks = TextAreaField('Any other details')
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

class SubsciberForm(Form):
    name = TextField('Full name', [validators.DataRequired("Enter a valid email address")])
    email = TextField('E-mail address', [validators.DataRequired("Enter a valid email address")])
    company = TextField('Company or organization name')
    province = SelectField(u'Province', [validators.DataRequired("This Field is required")], choices=[('KwaZulu-Natal', 'KwaZulu-Natal'),
        ('Gauteng', 'Gauteng'), ('Western Cape', 'Western Cape'), ('Free State', 'Free State'), ('Eastern Cape', 'Eastern Cape'),
        ('Northern Cape', 'Northern Cape'), ('North west', 'North west'), ('Limpopo', 'Limpopo'), ('Mpumalanga', 'Mpumalanga'), ])
    remarks = TextAreaField('Any other details')
    area1 = TextField('Area 1')
    area2 = TextField('Area 2')
    area3 = TextField('Area 3')
    area4 = TextField('Area 4')
    area5 = TextField('Area 5')
    area6 = TextField('Area 6')
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')

class ExampleForm(Form):
    email = TextField('E-mail address', [validators.DataRequired("Enter a valid email address")])
    submit = SubmitField('Send')

####################################################################################
#       ###     ####    ###       #### ##### ###     ###     ### ####### ####    ###
#### ###### ####### ########## ####### ##### ##### ##### ####### ####### ### #######
#### ######   ######  ######## ######## ### ###### #####   ##### ### ### ####  #####
#### ###### ##########  ###### ######### # ####### ##### ######## ## ## #######  ###
#### ######     ###    ####### ########## ######     ###     ##### ### #####    ####
####################################################################################



@app.route('/cu')
def cu():
    return render_template('cu.html', current_user=current_user)


@app.route('/googlef5ce05674f2c2ab6.html')
def googleverify():
    return render_template('googlef5ce05674f2c2ab6.html')

###############################################
# ##### ###     ###     ### ####### ####    ###
# ##### ##### ##### ####### ####### ### #######
## ### ###### #####   ##### ### ### ####  #####
### # ####### ##### ######## ## ## #######  ###
#### ######     ###     ##### ### #####    ####
###############################################



@app.route('/subscribe', methods=('GET', 'POST'))
def subscribe():

    form = SubsciberForm()
    eform = ExampleForm(request.form, prefix="eform")
    if request.method == 'POST':

        if form.validate() == False:
            flash('Please enter information into all of the required fields')
            return render_template('subscriber.html', form = form, eform=eform)
        else:
            # Generate a random customer reference
            def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
                return ''.join(random.choice(chars) for _ in range(size))
            ref = id_generator()
            paid = False
            date= datetime.now()
            name = form.name.data.lower()
            email = form.email.data
            province=form.province.data.lower()
            company = form.company.data.lower()
            areas = []
            number_of_areas = 0
            if form.area1.data != '':
                number_of_areas += 1
                areas.append(form.area1.data.lower())
            if form.area2.data != '':
                number_of_areas += 1
                areas.append(form.area2.data.lower())
            if form.area3.data != '':
                number_of_areas += 1
                areas.append(form.area3.data.lower())
            if form.area4.data != '':
                number_of_areas += 1
                areas.append(form.area4.data.lower())
            if form.area5.data != '':
                number_of_areas += 1
                areas.append(form.area5.data.lower())
            if form.area6.data != '':
                number_of_areas += 1
                areas.append(form.area6.data.lower())

            total_due = ('R'+str(number_of_areas * 150)+'.00')

            for area in areas:
                subscriber = Subscriber(date=date, name=name,
                                        email=email, province=province,
                                        areas=area, company=company,
                                        number_of_areas=number_of_areas,
                                        paid=paid, ref=ref)
                db.session.add(subscriber)
                db.session.commit()



            msg = Message(subject="Subscription to Report Prowlers", sender='reportprowlers@gmail.com', recipients=[form.email.data])
            msg.body = """
            Hi %s

            Thank you for your subscription, we have entered the details below into our database.

            Please take a moment to check the details below are correct:


            Email = %s
            Company or Organization = %s
            Province = %s
            Remarks = %s
            Areas =  %s, %s, %s, %s, %s, %s


            OPTION 1

            Complete the Debit Order Mandate attached
            Email the completed form to reportprowlers@gmail.co.za


            OPTION 2

            Set up a debit order for %s per calender month

            Name:           Report Prowlers
            Bank:           Capitec
            Branch Code:    470010
            Acc Number:     1474674478
            Payment Reference: %s


            Terms and conditions can be read at any time at www.reportprowlers.co.za/terms

            For cancellations or adjustments to order email reportprowlers@gmail.com
            before the first working day of each month

            Please do not hesitate to contact us should you have any questions


            Sincerely Yours,

            Hannah Swan
            Sales Manager
            Report Prowlers
            Phone: 039 319 1088
            Mobile: 078 738 3038
            Email: reportprowlers@gmail.com


            """ % (form.name.data, form.email.data, form.company.data, form.province.data, form.remarks.data,
                form.area1.data, form.area2.data, form.area3.data, form.area4.data, form.area5.data, form.area6.data, total_due, ref)
            msg.add_recipient('reportprowlers@gmail.com')
            with app.open_resource("MANDATE.pdf") as fp:
                msg.attach("MANDATE.pdf", "file/pdf", fp.read())
            mail.send(msg)
            flash('Your subscription form has been sent')
            flash('Please check your emails')
            return render_template('subscriber.html',
                                title = 'Subscribe to Report Prowlers',
                                form = form, eform=eform)
    elif request.method == 'GET':
        return render_template('subscriber.html',
                                title = 'Subscribe to Report Prowlers',
                                form = form, eform=eform)







@app.route('/example', methods=('GET', 'POST'))
def example():
    form = SubsciberForm()
    eform = ExampleForm()
    if request.method == 'POST':
        if eform.validate() == False:

            flash('Please enter information into all of the required fields')
            return render_template('subscriber.html',
                                    title = 'Subscribe to Report Prowlers',
                                    form = form, eform=eform)

        else:
            msg = Message(subject="PROWLER CODE GREEN", sender='reportprowlers@gmail.com', recipients=[eform.email.data])
            msg.body = """
            ##### EXAMPLE PROWLER CODE GREEN  ######

            PERSON REPORT
            time= %s

            province = KwaZulu-Natal
            area = Margate
            street = North Drive
            tone = Light skinned
            age = 20-40
            build = large
            height = short
            shirt = red
            pants = yellow shorts
            shoes = white
            remarks = Carrying a suitcase

            SUGGESTED ACTION: Mobilize response, ready reserve

            CODE GREEN:
            First report in the last 3 hours
            No similar reports in the last 48 hours
            (Similar = where 3 or more fields are the same)

            """ % (datetime.now().strftime("%d %B, %Y %H:%M"))

            mail.send(msg)

            flash("Example email has been sent")
            return render_template('subscriber.html',
                                    title = 'Subscribe to Report Prowlers',
                                    form = form, eform=eform)

    return render_template('subscriber.html',
                                    title = 'Subscribe to Report Prowlers',
                                    form = form, eform=eform)







@app.route('/register')
def register():
    # If user is logged in, show useful information here, otherwise show login and register
    return render_template('subscriber.html', form=SubsciberForm(), eform=ExampleForm())





@app.route('/terms')
def terms():
    return render_template('terms.html')








# landing page, no login required
@app.route('/', methods=('GET', 'POST'))
def index():
    # Test to identify users role
    if current_user.has_role('user') and current_user.has_role('superuser'):
        print('###############################################################')
        print('###############I am USER and SUPERUSER #########################')
        print('ID = ' + str(current_user.id))
        print(current_user.email)
        print('###############################################################')
    elif current_user.has_role('user'):
        print('###############################################################')
        print('###############I am USER #########################')
        print('ID = ' + str(current_user.id))
        print(current_user.email)
        print('###############################################################')
    elif current_user.has_role('superuser'):
        print('###############################################################')
        print('############### I AM SUPER  #########################')
        print('ID = ' + str(current_user.id))
        print(current_user.email)
        print('###############################################################')
    else:
        print('###############################################################')
        print('############### I am a GUEST #########################')
        print('###############################################################')


    form = ContactForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('You must enter something into all of the fields')
            return render_template('index.html', form = form)
        else:
            msg = Message(subject="Prowler Contact", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
            msg.body = """
            Hi %s

            Thank you for your message:

            "%s"

            Best wishes

            Vaughn de Villiers
            Report Prowlers


            """ % (form.email.data, form.message.data)
            # Without Celery
            msg.add_recipient(form.email.data)
            mail.send(msg)
            # With Celery
            #send_async_email.delay(msg)
            flash('Your message has been sent')
            return render_template(
                'index.html',
                title='Report Prowlers',
                year=datetime.now().year,
                message='Index and contact page.',
                form=form)


    elif request.method == 'GET':
            return render_template(
                'index.html',
                title='Report Prowlers',
                year=datetime.now().year,
                message='Index and contact page.',
                form=form)


######################################################################
#### ######    ####     ###### ######    ####     #####  ######    ###
### # ##### ### ### ######### # ##### ### ##### ###### ### ### #######
## ### ####    ####   ###### ### ####    ###### ##### #########  #####
#       ### ### ### #######       ### ######### ###### ### ######  ###
# ##### ### ### ###     ### ##### ### #######     #####   ####    ####
######################################################################

@app.route('/areapics')
@login_required
def areapics():
    filenames = []
    for filename in os.listdir('/home/VaughnDV/mysite/prowler/static/uploads'):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            filenames.append(os.path.join('static/uploads', filename))
        else:
            pass
    flash('Images are in numeral and alphabetical order')
    flash('Please contact us should you wish us to remove a picture')
    return render_template(
                    'areapics.html',
                    title='Report Prowlers',
                    year=datetime.now().year,
                    nessage='Pictures sent to us in the last day for your area',
                    filenames=filenames
                    )




#####################################################
#    ####     ###    #####    #####   ##### ##### ###
# ### ### ####### ### ### ######## ### #### # ### ###
#    ####   #####    #####  ##### ##### ### ## ## ###
# ####### ####### ### ######  #### ### #### ### # ###
# #######     ### ### ###    ######   ##### ####  ###
#####################################################



@app.route('/person', methods=('GET', 'POST'))
@login_required  # required for Flask-Security
def person():
    form = ReportPerson()
    fields = []
    print("Request")
    if request.method == 'POST':
        print("Method is POST")
        if form.validate() == False:
            flash('Please enter all the REQUIRED fields')
            return render_template('person.html', form=form)
        else:
            area = form.area.data.lower()
            province=form.province.data.lower()
            street=form.street.data.lower()
            report = Person(province=province, reporter_email=current_user.email, area=area, street=street, tone=form.tone.data, age=form.age.data, build=form.build.data, height=form.height.data,
        shirt=form.shirt.data.lower(), pants=form.pants.data.lower(), shoes=form.shoes.data.lower(), remarks=form.remarks.data)
            ## With Celery
            #send_async_email.delay(report)
            db.session.add(report)
            db.session.commit()

            # Query to get subscribers for the reported area
            recipients = Subscriber.query.filter(Subscriber.province == province).filter(Subscriber.areas == area).filter(Subscriber.paid == True).all()

            # Change to real time in production
            three_hours_ago = datetime.now() - timedelta(hours=3)
            #one_min_ago = datetime.now() - timedelta(minutes=1)

            # Query all the entries for the reported area in the last 3 hours
            last_three_hours = Person.query.filter(Person.time > three_hours_ago).filter(Person.province == province).filter(Person.area == area).all()

            # Query all the entries for the reported area in the last 2days
            #last_two_days = Person.query.filter(Person.time > two_days_ago).filter(Person.province == form.province.data).filter(Person.area == form.area.data).all()

            counter = 0
            for item in last_three_hours:
                counter += 1


            print('#################################')
            print('TEST')
            #print(last_three_hours[0].area)
            #print(last_three_hours[0].province)
            print(counter)
            print('#################################')

            if counter == 1:

                msg = Message(subject="PROWLER CODE GREEN", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE GREEN

                PERSON REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                tone = %s
                age = %s
                build = %s
                height = %s
                shirt = %s
                pants = %s
                shoes = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize response, ready reserves

                CODE GREEN:
                First report in the last 3 hours
                No similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.tone.data, form.age.data,
                    form.build.data, form.height.data, form.shirt.data, form.pants.data,
                    form.shoes.data, form.remarks.data )
                ## Without Celery
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)
            #elif counter == 2 or similar >= 3:
            elif counter == 2:
                msg = Message(subject="PROWLER CODE YELLOW", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE YELLOW

                PERSON REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                tone = %s
                age = %s
                build = %s
                height = %s
                shirt = %s
                pants = %s
                shoes = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize reserves, ready notify Alpha

                CODE YELLOW:
                Second report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.tone.data, form.age.data,
                    form.build.data, form.height.data, form.shirt.data, form.pants.data,
                    form.shoes.data, form.remarks.data, )
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter >= 3:
                msg = Message(subject="PROWLER CODE RED", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE RED

                PERSON REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                tone = %s
                age = %s
                build = %s
                height = %s
                shirt = %s
                pants = %s
                shoes = %s
                remarks = %s

                CODE RED:
                Third report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                SUGGESTED ACTION: Mobilize Alpha, notify police
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.tone.data, form.age.data,
                    form.build.data, form.height.data, form.shirt.data, form.pants.data,
                    form.shoes.data, form.remarks.data, )
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            else:
                msg = Message(subject="PROWLER ERROR", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER SYSTEM ERROR"

                PERSON REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                tone = %s
                age = %s
                build = %s
                height = %s
                shirt = %s
                pants = %s
                shoes = %s
                remarks = %s

                DEBUG
                COUNTER = %s

                SUGGESTED ACTION: Send vehicle to investigate, ready backup, notify developer
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.tone.data, form.age.data,
                    form.build.data, form.height.data, form.shirt.data, form.pants.data,
                    form.shoes.data, form.remarks.data, counter )
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            flash('Thank you for your report has been sent, we are investigating')
            flash('Please encourage your local security services to support us in improving this free service')
            flash('All the information is used to improve our service and build intelligence in crime prevention')
            return redirect(url_for('index'))

    else:
        print("Method is GET")
        return render_template('person.html', title='Report Prowlers', form=form)





############################################################
# ##### ###     ### ### ###     #####  ##### #######     ###
# ##### ### ####### ### ##### ###### ### ### ####### #######
## ### ####   #####     ##### ##### ######## #######   #####
### # ##### ####### ### ##### ###### ### ### ####### #######
#### ######     ### ### ###     #####   ####     ###     ###
############################################################


@app.route('/vehicle', methods=('GET', 'POST'))
@login_required  # required for Flask-Security
def vehicle():
    form = ReportVehicle()
    fields = []
    print("Request")
    if request.method == 'POST':
        print("Method is POST")
        if form.validate() == False:
            flash('Please enter all the REQUIRED fields')
            return render_template('vehicle.html', form=form)
        else:
            area = form.area.data.lower()
            province=form.province.data.lower()
            street=form.street.data.lower()
            report = Vehicle(province=province, reporter_email=current_user.email, area=area, street=street, colour=form.colour.data.lower(), registration=form.registration.data.upper(),
        occupants=form.occupants.data.lower(), make=form.make.data.lower(), model=form.model.data.lower(), remarks=form.remarks.data)
            db.session.add(report)
            db.session.commit()
            recipients = Subscriber.query.filter(Subscriber.province == province).filter(Subscriber.areas == area).filter(Subscriber.paid == True).all()
            # Change to real time in production
            three_hours_ago = datetime.now() - timedelta(hours=3)
            one_min_ago = datetime.now() - timedelta(minutes=1)

            last_three_hours = Vehicle.query.filter(Vehicle.time > three_hours_ago).filter(Vehicle.province == province).filter(Vehicle.area == area).all()

            counter = 0
            for item in last_three_hours:
                counter += 1
            print('#################################')
            #print(last_three_hours[0].area)
            #print(last_three_hours[0].province)
            print(counter)
            print('#################################')

            if counter == 1:
                msg = Message(subject="PROWLER CODE GREEN", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE GREEN

                VEHICLE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                vehicle colour = %s
                registration = %s
                number of occupants = %s
                vehicle make = %s
                vehicle model = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize response, ready reserves

                CODE GREEN:
                First report in the last 3 hours
                No similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.colour.data, form.registration.data,
                    form.occupants.data, form.make.data, form.model.data, form.remarks.data)
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter == 2:
                msg = Message(subject="PROWLER CODE YELLOW", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE YELLOW

                VEHICLE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                vehicle colour = %s
                registration = %s
                number of occupants = %s
                vehicle make = %s
                vehicle model = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize reserves, ready notify Alpha


                CODE YELLOW:
                Second report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.colour.data, form.registration.data,
                    form.occupants.data, form.make.data, form.model.data, form.remarks.data)
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter >= 3:
                msg = Message(subject="PROWLER CODE RED", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE RED

                VEHICLE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                vehicle colour = %s
                registration = %s
                number of occupants = %s
                vehicle make = %s
                vehicle model = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize Alpha, notify police

                CODE RED:
                Third report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.colour.data, form.registration.data,
                    form.occupants.data, form.make.data, form.model.data, form.remarks.data)
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)
            else:
                msg = Message(subject="PROWLER ERROR", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER SYSTEM ERROR"

                VEHICLE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                vehicle colour = %s
                registration = %s
                number of occupants = %s
                vehicle make = %s
                vehicle model = %s
                remarks = %s

                SUGGESTED ACTION: Send vehicle to investigate, ready backup, notify developer

                DEBUG
                COUNTER = %s
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.colour.data, form.registration.data,
                    form.occupants.data, form.make.data, form.model.data, form.remarks.data, counter)
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            counter = 0
            flash('Thank you for your report has been sent, we are investigating')
            flash('Please encourage your local security services to support us in improving this free service')
            flash('All the information is used to improve our service and build intelligence in crime prevention')
            return redirect(url_for('index'))

    else:
        print("Method is GET")
        return render_template('vehicle.html', title='Report Prowlers', form=form)





##############################################
##    ####    ######   ##### ##### ###    ####
# ######## ### #### ### #### ##### ### ### ###
# #    ###    #### ##### ### ##### ###    ####
# ### #### ### #### ### ##### #### ### #######
##    #### ### #####   #######     ### #######
##############################################



@app.route('/group', methods=('GET', 'POST'))
@login_required  # required for Flask-Security
def group():
    form = ReportGroup()
    fields = []
    print("Request")
    if request.method == 'POST':
        print("Method is POST")
        if form.validate() == False:
            flash('Please enter all the REQUIRED fields')
            return render_template('group.html', form=form)
        else:
            area = form.area.data.lower()
            province=form.province.data.lower()
            street=form.street.data.lower()
            report = Group(province=province, reporter_email=current_user.email, area=area, street=street, number_of_people=form.number_of_people.data.lower(), remarks=form.remarks.data)
            db.session.add(report)
            db.session.commit()
            start = datetime.now()
            recipients = Subscriber.query.filter(Subscriber.province == province).filter(Subscriber.areas == area).filter(Subscriber.paid == True).all()
            # Change to real time in production
            three_hours_ago = datetime.now() - timedelta(hours=3)
            #one_min_ago = datetime.now() - timedelta(minutes=1)
            #two_days_ago = datetime.now() - timedelta(days=2)
            last_three_hours = Group.query.filter(Group.time > three_hours_ago).filter(Group.province == province).filter(Group.area == area).all()
            #last_two_days = Group.query.filter(Group.time > two_days_ago).filter(Group.province == province).filter(Group.area == area).all()

            counter = 0
            for item in last_three_hours:
                counter += 1

            if counter == 1:
                msg = Message(subject="PROWLER CODE GREEN", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE GREEN

                GROUP REPORT
                time = %s

                province = %s
                area = %s
                street = %s
                number of people in group = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize response, ready reserves

                CODE GREEN:
                First report in the last 3 hours
                No similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.number_of_people.data, form.remarks.data, )

                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter == 2:
                msg = Message(subject="PROWLER CODE YELLOW", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE YELLOW

                GROUP REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                number of people in group = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize reserves, ready notify Alpha


                CODE YELLOW:
                Second report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.number_of_people.data, form.remarks.data, )
                mail.send(msg)

            elif counter >= 3:
                msg = Message(subject="PROWLER CODE RED", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE RED

                GROUP REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                number of people in group = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize Alpha, notify police

                CODE RED:
                Third report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.number_of_people.data, form.remarks.data, )
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            else:
                msg = Message(subject="PROWLER ERROR", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER SYSTEM ERROR"

                GROUP REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                number of people in group = %s
                remarks = %s

                SUGGESTED ACTION: Send vehicle to investigate, ready backup, notify developer

                DEBUG
                COUNTER = %s
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, form.number_of_people.data, form.remarks.data, counter )
                mail.send(msg)


            flash('Thank you for your report has been sent, we are investigating')
            flash('Please encourage your local security services to support us in improving this free service')
            flash('All the information is used to improve our service and build intelligence in crime prevention')
            return redirect(url_for('index'))

    else:
        print("Method is GET")
        return render_template('group.html', title='Report Prowlers', form=form)




##############################################
#     ### ##### ###### #######    ####     ###
### #####  ###  ##### # ##### ######## #######
### ##### # # # #### ### #### #    ###   #####
### ##### ## ## ###       ### ### #### #######
#     ### ##### ### ##### ####    ####     ###
##############################################





@app.route('/image', methods=('GET', 'POST'))
@login_required  # required for Flask-Security
def image():

    form = ReportImage()
    if request.method == 'POST':
        print("Method is POST")
        if form.validate_on_submit():
            filename = secure_filename(form.photo.data.filename)
            form.photo.data.save('/home/VaughnDV/mysite/prowler/static/uploads/' + filename)
            #form.photo.data.save('uploads/' + newname )
            area = form.area.data.lower()
            province=form.province.data.lower()
            street=form.street.data.lower()
            report = Image(time=datetime.now(),
                            reporter_email=current_user.email,
                            province=province,
                            area=area,
                            street=street,
                            filename=filename,
                            remarks=form.remarks.data)
            db.session.add(report)
            db.session.commit()
            recipients = Subscriber.query.filter(Subscriber.province == province).filter(Subscriber.areas == area).filter(Subscriber.paid == True).all()
            three_hours_ago = datetime.now() - timedelta(hours=3)
            #one_min_ago = datetime.now() - timedelta(minutes=1)
            last_three_hours = Image.query.filter(Image.time > three_hours_ago).filter(Image.province == province).filter(Image.area == area).all()
            #last_two_days = Image.query.filter(Image.time > two_days_ago).filter(Image.province == form.province.data).filter(Image.area == form.area.data).all()

            counter = 0
            for item in last_three_hours:
                counter += 1


            if counter == 1:
                msg = Message(subject="PROWLER CODE GREEN", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE GREEN

                IMAGE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                filename = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize response, ready reserves

                CODE GREEN:
                First report in the last 3 hours
                No similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, filename, form.remarks.data)
                ## Attachment
                with app.open_resource('/home/VaughnDV/mysite/prowler/static/uploads/' + filename) as fp:
                    msg.attach(filename, "image/jpg", fp.read())
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter == 2:
                msg = Message(subject="PROWLER CODE YELLOW", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE YELLOW

                IMAGE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                filename = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize reserves, ready notify Alpha


                CODE YELLOW:
                Second report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)

                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, filename, form.remarks.data)
                ## Attachement
                with app.open_resource('/home/VaughnDV/mysite/prowler/static/uploads/' + filename) as fp:
                    msg.attach(filename, "image/jpg", fp.read())
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            elif counter >= 3:
                msg = Message(subject="PROWLER CODE RED", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER CODE RED

                IMAGE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                filename = %s
                remarks = %s

                SUGGESTED ACTION: Mobilize Alpha, notify police

                CODE RED:
                Third report in the last 3 hours
                Similar reports in the last 48 hours
                (Similar = where 3 or more fields are the same)


                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, filename, form.remarks.data)

                with app.open_resource('/home/VaughnDV/mysite/prowler/static/uploads/' + filename) as fp:
                    msg.attach(filename, "image/jpg", fp.read())
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)
            else:
                msg = Message(subject="PROWLER ERROR", sender='reportprowlers@gmail.com', recipients=['reportprowlers@gmail.com'])
                msg.body = """
                PROWLER SYSTEM ERROR"

                IMAGE REPORT
                time= %s

                province = %s
                area = %s
                street = %s
                filename = %s
                remarks = %s

                SUGGESTED ACTION: Send vehicle to investigate, ready backup, notify developer

                DEBUG
                COUNTER = %s
                """ % (datetime.now().strftime("%d %B, %Y %H:%M"), province, area, street, filename, form.remarks.data, counter)

                with app.open_resource('/home/VaughnDV/mysite/prowler/static/uploads' + filename) as fp:
                    msg.attach(filename, "image/jpg", fp.read())
                for recipient in recipients:
                    msg.add_recipient(recipient.email)
                mail.send(msg)

            flash('Thank you for your report has been sent, we are investigating')
            flash('Please encourage your local security services to support us in improving this free service')
            flash('All the information is used to improve our service, and build intelligence in crime prevention')
            return redirect(url_for('index'))

        else:
            flash('You must enter the area')
            return render_template('image.html', form=form)


    return render_template('image.html',title='Report Prowlers' , form=form)



if __name__ == '__main__':
    app.run()
