from faker import Faker
from models import *

fake = Faker()
for _ in range(2):
    User.seed(fake)

