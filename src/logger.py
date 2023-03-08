import logging
'''
Logger is for the purpose that any execution that probably happens,
we should be able to log all those information, execution and everything in some files.
So that we will be able to track if there are some errors, even the custom exception error,
those exception we will able to log into the text file
'''
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
'''
So whatever log will get created with respect to the current working directory.
In our src logs will get created, and every file start with logs along with whatever file name is besically coming
'''
os.makedirs(logs_path,exist_ok=True)
'''
This besically says that even though there is a file or folder, keep on appending the files inside whenever we create the file
'''

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

'''
Now whenever we want to create the log we really need to set,
If you want to overwrite the functionality of the logging, we have to probably set this up in the besic config
'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# Below code is for checking that logging is started or not.
'''
if __name__=="__main__":
    logging.info("Logging has started")
'''