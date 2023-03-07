
# import required module
import os
# assign directory
path_of_the_directory = '/Users/fischee/Working/java example/python/restart-first-repo'
 
# iterate over files in
# that directory
for filename in os.listdir(path_of_the_directory):
    file = os.path.join(path_of_the_directory,filename)

    # checking if file is a directory
    if os.path.isfile(file):
        with open(file) as f:
            lines = f.readlines()
            #print(lines)
            data = ''.join(lines)
            #print(data)
            print('File Name =',f.name)
            print('lines =',len(lines))
            print('Words = ',len(data.split()))
            data = ''.join(data.split())
            print('characters = ',len(data))
            print('')
                
        #data = f.read()

        #get the length of the data
        #number_of_characters = len(data)

        #print('Number of characters in text file :', number_of_characters)
        #print(f)