# 1) Connect to a MongoDB document collection
# 2) Insert a document
# 3) Display all of the documents in a collection
import datetime
import urlparse
import string
import random
from pymongo import MongoClient

# @func: issue_code_generator
#     Generates 6 digit alphanumeric digit
def issue_code_generator(size=6, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

# connect to the MongoDB on MongoLab
# to learn more about MongoLab visit http://www.mongolab.com
# replace the "" in the line below with your MongoLab connection string
# you can also use a local MongoDB instance
try:
   connection = MongoClient('localhost', 27017)
   print "\n>>> Connected successfully!!!\n"
except pymongo.errors.ConnectionFailure, e:
   print "\n>>> Could not connect to MongoDB: %s" % e

# connect to the students database and the ctec121 collection
db = connection.TaarifaAPI
# Call the collection
collection = db.subscribers

###############################################################################
# 1. User Registers by sending REGISTER to SHORT CODE

# 2. System saves the User in the Subscribers Table & sends a Thank You/Welcome Message.

# 3. System sends an Explainer Message. Looks as below:
   # Report an issue by sending the number of the issue,
#    leave a space and write the message.
#    Issues Are:
#    1. CUSTOMS        6. DUTY
#    2. BUREAU         7. PASSPORT
#    3. STANDARDS      8. BORDER PASS
#    4. POLICE         9. HARRASSMENT
#    5. IMMIGRATION   10. BRIBE

#    EXAMPLE: 4 innappropriate behaviour
###############################################################################

# 4. User sends the number of the issue and the message
#    4 innappropriate behaviour
str = raw_input("Please enter your issue: ")
key,desc = str.split(' ', 1 );

# HTTP Request from Airtel Zambia
url = 'http://cbt.com/?number=255759112233&keyword='+key+'&description='+desc+'&status=1'
par = urlparse.parse_qs(urlparse.urlparse(url).query)
# print par['number'], par['keyword'], par['description']

code = issue_code_generator()

# JSON data from the URL
issues = [{
   "facility_code":"trd001",
   "issue_phone_number": par['number'],
   "issue_keyword": par['keyword'],
   "issue_status": par['description'],
   "issue_status_group": "pending",
   "issue_code": code
}]
subscribers = [{
   "facility_code":"sub001",
   "issue_phone_number": par['number'],
   "issue_keyword": par['keyword'],
   "issue_description": par['description'],
   "issue_status": par['status']
}]

resources = db.resources
try:
   res_subscribers_id = resources.insert(subscribers)
   res_issues_id = resources.insert(issues)

   # 5. System sends a Thank you message and ISSUE CODE (auto-generated)
   #    Thanks for sending us your report.
   #    To follow up on your report send 
   #    IS001 to 1040
   print "\nThanks for sending your report.\nTo follow up on your report send "+code+" to 1040\n"
except ValueError:
   print "Oops! Failed to insert record."

# for subscriber in resources.find({"facility_code":"sub001"}):
#    print subscriber
# for issue in resources.find({"facility_code":"trd001"}):
#    print issue

# 6. User sends ISSUE CODE to the SHORT CODE
print "\n*********************************\n"
acceptIssueCode = raw_input("Enter ISSUE CODE: ")
# 7. System checks ISSUE CODE and sends the status of the Issue to the User.
if acceptIssueCode == code:
   print "The report you made with the ISSUE CODE "+code+" is being worked on.\nPlease give it some time and check back by sending the ISSUE CODE to 1040.\nThank You!"
print "\n*********************************\n"

print "Subscribers: ", resources.find({"facility_code":"sub001"}).count()
print "Issues: ", resources.find({"facility_code":"trd001"}).count()

# close the connection to MongoDB
connection.close()