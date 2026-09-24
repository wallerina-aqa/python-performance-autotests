from locust import User, between

class LocustBaseUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    abstract = True
