message = open('312-message.txt', 'w')
message.write('Testing file for player configuration')
message.write('Testing file for player score')
message.close()

message_test = open('312-message.txt', 'r')

message_test.close()

#files needs to be closed after alterations so that it's not accidentally atler it.