import hashlib


class HashClass:

    @staticmethod
    def hash_password(password):
        hash_obj = hashlib.md5(password.encode())
        return hash_obj.hexdigest()