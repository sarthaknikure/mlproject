import sys
'''
The sys module in python provides various functions and variables that are used to manipulate different parts of python runtime environment.
So any exception that is getting controlled the sys library will automatically have this information
'''
import logging

def error_message_detail(error, error_detail:sys):
    # This will be my error massage detail, whenever an exception get raised I want to push my own custom massage
    # This error detail will be present inside the sys
    
    _,_,exc_tb=error_detail.exc_info()
    # This variable exc_info will give you all the information like on which file exception has occured, on which line number exception has occured
    
    file_name=exc_tb.tb_frame.f_code.co_filename
    # custome exception handling documentation
    
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    return error_message
    

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_detail(error_message,error_detail=error_detail)
        '''
        These are the parameters I am giving, in my custom exception, so whenever I raise this custome exception
        First up all it is inheriting the parent Exception, whatever error msg comming from this perticular function, that error msg will come over here,
        and we will initialise to the class variable(custom exception variable) i.e. error msg
        '''
    
    def __str__(self):
        return self.error_message
    '''
    So whenever I try to print it I will be getting all the error msg here
    '''
# Below code is for checking purpose
'''
if __name__=="__main__":

    try:
        a=1/0
    except Exception as e:
        logging.info("Devide By Zero Error")
        raise CustomException(e,sys)
'''