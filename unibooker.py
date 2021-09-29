import argparse

from dotenv import load_dotenv
from unimib_booker import execute_booking

import os
import sys

# Creation of the parser
arg_parser = argparse.ArgumentParser(description="Automatically books a lessons at unimib.")

# Adding the arguments
arg_parser.add_argument("-e", "--use-env", help="Use .env file for auth info", action="store_true")

arg_parser.add_argument("-n", "--now", help="execute booking immediately", action="store_true")

arg_parser.add_argument("-u", "--username", help="Email of the university account", type=str)
arg_parser.add_argument("-p", "--password", help="Passowrd of the university account", type=str)


args = arg_parser.parse_args()

if args.use_env:
    if os.path.exists(".env"):
        load_dotenv()
        print("INFO: Envars loaded")
        execute_booking(os.environ.get("username"),
                        os.environ.get("password"))
    else:
        print("ERROR: Env file not present!")
else:
    if args.username and args.password:
        print("Booking started with username and password")
        execute_booking(args.username,
                        args.password)
    else:
        print("ERROR: Username AND Password is required (-u and -p)")
