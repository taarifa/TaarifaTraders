import telerivet

tr = telerivet.API('1PtmwpYc0OyFVS6F6wIqlQHa1Mb3c4db')
project = tr.initProjectById('PJ4f75ddf74530bf70')

sent_msg = project.sendMessage(
    content = "hello from CBT", 
    to_number = "+255782978899"
)

print("Message successfully sent!");