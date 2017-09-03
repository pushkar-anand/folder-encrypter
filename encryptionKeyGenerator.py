import string
import random

def key_generator(size, chars=string.ascii_uppercase + string.digits + string.ascii_lowercase):
    return ''.join(random.SystemRandom().choice(chars) for _ in range(size))