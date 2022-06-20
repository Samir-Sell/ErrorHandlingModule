import os
import sys

def error(e, kill=False):
    print(f"Error: {e}")
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(f"Error Type: {exc_type}, File Name: {fname}, Line Number: {exc_tb.tb_lineno}")
    if kill == True:
        print("Exiting Program")
        sys.exit
