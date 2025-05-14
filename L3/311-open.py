message = open('311-message.txt', 'w')
message.write('Testing file for player configuration')
message.close()

message_test = open('311-message.txt', 'r')
print('311-message is open')

#when opening an external file we want to store that action in a variable because there are many methods we can run to read content from a file write to the file or other actions on the file. we need to open the file to do something one the file.