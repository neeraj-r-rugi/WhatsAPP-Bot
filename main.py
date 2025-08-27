#Imports
import argparse
import json
from pywhatkit import whats


#Drfines and Constants
PROG_VERSION = "v1.0"
COUNTRY_CODE = "+91"

#Functions
def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="Git Auto Info Bot")
    parser.add_argument("-V", "--version",
                        action="store_true",
                        default=False,
                        help="Displays the version of the current build")
    parser.add_argument("-m", "--message",
                        default=False,
                        help="Overrides the message in whatsapp.json file.")
    
    return parser
    
def load_json(filename) -> dict:
    with open(filename, "r") as file:
        data = json.load(file)
    
    return data
    
    
    
def main() -> None:
    arg_parser = init_parser()
    user_args = arg_parser.parse_args()
    user_args = {"version":user_args.version, "message":user_args.message}
    if(user_args["version"]):
        print("The Current Version is: ", PROG_VERSION)
        return
    
    whatsApp = load_json("./whatsapp.json")
    if(user_args["message"]):
        whatsApp["message"] = user_args["message"]
        
    for number in whatsApp["numbers"]:
        whats.sendwhatmsg_instantly(COUNTRY_CODE+number, whatsApp["message"])
        
        


if __name__ == "__main__":
    main()