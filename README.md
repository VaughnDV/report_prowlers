"# reportprowlers" 

Report prowlers is an online service that security companies and policing services can subscribe to. 
In return they receive alerts via email of reports of suspicious activity in their subscribed areas.

USERS (The general public) can register and report suspicious activity by completing the simple forms. 
For USERS this service for free, and remain anonymous to subscribers. 
Police may call request the email address of the reporting USER should police require further help.

SUBSCRIBERS pay a monthly fee for each area they wish to monitor.

Reports are compared with other report in that area:

	Code Green = first report
	Code Yellow = Second report 
	Code Red = Multiple reports with similar 

This allows SUBSCRIBERS to escalate their response appropriately.

The onus is upon the SUBSCRIBERS to monitor their emails for incoming reports. 
SUBSCRIBERS may spread the word for USERS to use this servie in their communities. 
  

###########
#SETTING UP
###########

#Clone

	TBA

#Install requirements

	pip install -r requirements.txt

#Initiate database and create super user

	python create_user.py

#Populate with dummy data (OPTIONAL)

	python populate_db

#Run app

	python app.py

#Note Celery deacticated by default


##########
# TO DO
##########

#Clean up code
#Set up RabbitMQ and modify settings to send 
#Finish Image upload facility

