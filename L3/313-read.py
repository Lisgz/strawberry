message = open('313-message.txt', 'w')
message.write('Testing file for player configuration')
message.write('Testing file for player score')
message.close()

message_test = open('313-message.txt', 'r') 
                    #file opening      status
content = message_test.read()
print(content)
message_test.close()

# r stands for read
#r+ = write and read

#for a file to be read it needs to be open in a kind of read mode the contents need to be stored in a variable and then the content can be read through a print statement