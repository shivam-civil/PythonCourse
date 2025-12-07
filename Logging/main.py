from helper import get_input,log_setup
import logging
from math import fabs
log_setup()

#A progarm to find whether a number is odd or even.
number=get_input('Enter a  number : ',data_type=float)
logging.info("Data taken as input...")
if fabs(number)%2==0:
    print(f"{number} is even...")
    logging.info("data is even.")
else:
    print(f"{number} is odd...")   
    logging.info("data is odd...") 