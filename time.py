from datetime import datetime
from time import gmtime, strftime
import json

def acb():
    print(datetime.now())


    time = datetime.now()

    print(time)


    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    print(datetime.now().strftime('%Y%m%d%H%M%S%f'))

def link_con():
    #https://youtu.be/Ab5g3Ug7ysM
    requ = "Ab5g3Ug7ysM"

    link_b = "https://youtu.be/"

    print(link_b + requ)


todos = {
    "test_key":"https://www.youtube.com/watch?v=VJZ_iOEtUak&list=TLPQMTAwNzIwMjIqVUftO4aYfw&index=10"
}

link = todos['test_key']
print(link)