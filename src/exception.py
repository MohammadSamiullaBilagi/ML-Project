import sys
from src.logger import logging

# This custom Exception is raised whenved there is an error on any line number, filename

def error_message_details(error,error_detail:sys): #this function will give custom exception message whenever exception is raised
    _,_,exc_tb=error_detail.exc_info() #here i will get all info about exceptions line number, filename, etc
    filename=exc_tb.tb_frame.f_code.co_filename
    error_message="Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        filename,exc_tb.tb_lineno,str(error))
    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message=error_message_details(error_message,error_detail=error_detail)
    
    def __str__(self):
        return self.error_message

#Test the logging of exception
# if __name__=="__main__":
#     try:
#         a=1/0
#     except Exception as e:
#         logging.info("Divide by zero")
#         raise CustomException(e,sys)

        