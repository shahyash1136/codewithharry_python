# Append to and existing  file called John Doe.txt It should contain data about John Doe's Hometown

f = open("John Doe.txt", "a")

string = '''
John Doe initially live in Phoenix, Arizona. He is a very nice guy
'''
f.write(string)

f.close()
