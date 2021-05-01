from Pyro5.api import expose, behavior, serve
import os
from tinydb import TinyDB, Query
import serpent


@expose
@behavior(instance_mode="single")
class Dropbox(object):
    def __init__(self):
        self.db = TinyDB('db.json')
        

    def check_user(self, username):
        User = Query()
        user_check = self.db.search(User.user == username)
        if len(user_check) == 0:
            #query was empty
            return False
        else:
            return True

    def create_user(self, username, password):
        #Creates user
        # Adds to db as well as makes directory
        print("Adding user", username, "to server")
        os.mkdir(username)
        user_dict = {}
        user_dict['user'] = username
        user_dict['passwd'] = password
        self.db.insert(user_dict)
        

    def check_passwd(self, username, password):
        #Checks password
        User = Query()
        user_check = self.db.search(User.user == username)
        user_check = user_check[0]
        if user_check['passwd'] == password:
            return True
        else:
            return False

    def list_files(self, username):
        #returns all files in a user directory
        files = []
        for file in os.listdir(username):
            files.append(file)

        return files

    def list_users(self):
        #Return all the users in the db
        users = []
        for user in self.db.all():
            users.append(user['user'])

        return users 

    def list_user_files(self, query_user):
        #return all files of a specific user\
        files = []
        for file in os.listdir(query_user):
            files.append(file)
        return files

    def download_file(self, username, file):
        #Downloads a file from server to user side.
        infile = os.path.join(username, file)
        with open(infile, 'rb') as f:
            file_content = f.read()
        
        return file_content

    def upload_file(self, username, file, data):
        #upload a file from client to server in user folder.
        outfile = os.path.join(username, file)
        # print(data)
        data = serpent.tobytes(data)
        # print(data)
        with open(outfile, "wb") as f:
            f.write(data)

    def iterator(self, size):
        chunksize = size//100
        print("sending %d bytes via iterator, chunks of %d bytes" % (size, chunksize))
        data = b"x" * size
        i = 0
        while i < size:
            yield data[i:i+chunksize]
            i += chunksize





serve(
    {
        Dropbox: "dropbox"
    },
    use_ns=True)