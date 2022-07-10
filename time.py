from datetime import datetime
from time import gmtime, strftime


print(datetime.now())


time = datetime.now()

print(time)


print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))

print(datetime.now().strftime('%Y%m%d%H%M%S%f'))
