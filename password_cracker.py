import hashlib


class crack_password():
    def __init__(self, pass_hash):
        self.pass_hash = pass_hash
        self.flag = 0
        if pass_hash:
            self.run = self.check()

    def check(self):
        file = input("File name: ")
        try:
            pass_file = open(file, "r")
        except:
            print("No file found :(")
            quit()

        for word in pass_file:
            enc_wrd = word.encode('utf-8')
            digest = hashlib.md5(enc_wrd.strip()).hexdigest()
            if digest.strip() == self.pass_hash.strip():
                print("password found")
                print("Password is " + word)
                self.flag = 1
                break

        if self.flag == 0:
            print("password not found")


if __name__ == "__main__":
    convert_hash = input("Your Password: ")
    enc_hash = convert_hash.encode('utf-8')
    pass_hash = hashlib.md5(enc_hash.strip()).hexdigest()
    crack_password(pass_hash)