import random, os

def gen_random_filename(instance, filename):
    ext = os.path.splitext(filename)[-1]
    return str(random.random()) + ext