import sys, getopt, requests, json
from dotenv import dotenv_values

class bcolors:
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def main(argv):
    url = ""
    api_ver = ""
    source = ""
    dest = ""
    token = ""

    ##Load mandatory .env variables
    config = dotenv_values(".env")
    try:
        url = config["URL"]
        api_ver = config["API_VER"]
    except Exception as e:
        print_dotenv()
        sys.exit(2)

    #Load optional .env variable
    try:
        token = config["TOKEN"]
    except Exception as e:
        pass

    ##Handle command line args
    try:
        opts, args = getopt.getopt(argv, "hs:d:t:", ["help", "source=", "dest=", "token="])
    except getopt.GetoptError:
        print_help(True)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help(False)
            sys.exit(0)
        elif opt in ("-s", "--source"):
            source = arg
        elif opt in ("-d", "--dest"):
            dest = arg
        elif opt in ("-t", "--token"):
            token = arg
    
    ##Check if any required values are empty
    if source == "" or dest == "":
        print_help(True)
        sys.exit(2)
    elif url == "" or api_ver == "":
        print_dotenv()
        sys.exit(2)
    elif token == "":
        print(f"{bcolors.FAIL}Must specify a token{bcolors.ENDC} either using {bcolors.OKBLUE}-t, --token{bcolors.ENDC} or {bcolors.OKBLUE}in .env{bcolors.ENDC}")
        print(f"Run with {bcolors.OKBLUE}-h{bcolors.ENDC} or {bcolors.OKBLUE}--help{bcolors.ENDC} for more information")
        sys.exit(2)

    ##Craft request, send
    url_string = url + "/api/" + api_ver + "/movePad"
    payload = {
        "apikey": token,
        "sourceID": source,
        "destinationID": dest
    }
    response = requests.post(url_string, params=payload)
    
    ##Handle response
    try:
        response_dict = json.loads(response.text)
        if response_dict["code"] == 0:
            print(f"{bcolors.OKGREEN} ✔ {bcolors.ENDC}Successfully moved {source} to {dest}")
        else:
            print(f"{bcolors.FAIL} ⨯ {bcolors.ENDC}Unsuccessful - {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed: {response.text}")


            

def print_help(shortHelp):
    if shortHelp:
        print(f"{bcolors.OKBLUE}Usage: {bcolors.ENDC}move-pad.py -s <source> -d <dest> [OPTIONAL: -t <api_token>]")
        print(f"Run with {bcolors.OKBLUE}-h{bcolors.ENDC} or {bcolors.OKBLUE}--help{bcolors.ENDC} for more information")
    else:
        print('move-pad.py -s <source> -d <dest> [OPTIONAL: -t <api_token>]')
        print(f"{bcolors.OKBLUE}-s, --source : {bcolors.ENDC}The name of the pad to move")
        print(f"{bcolors.OKBLUE}-d, --dest : {bcolors.ENDC}The name the pad will be moved to")
        print(f"{bcolors.OKCYAN}[OPTIONAL]: {bcolors.ENDC}{bcolors.OKBLUE}-t, --token : {bcolors.ENDC}The Etherpad API token")
        print(f"If token is not passed as a parameter, it must be set in the .env file as {bcolors.UNDERLINE}TOKEN{bcolors.ENDC}. If it is both set in .env and passed as a parameter, the parameter takes priority")
        print(f"{bcolors.BOLD}The .env file must be set up with {bcolors.UNDERLINE}URL{bcolors.ENDC}{bcolors.BOLD} and {bcolors.UNDERLINE}API_VER{bcolors.ENDC}")
        print(f"{bcolors.BOLD}If you wish to use spaces, hyphens, or other special characters in a pad name, surround it in \"quotation marks\"{bcolors.ENDC}")
        print(f"{bcolors.WARNING}WARNING: IF A PAD ALREADY EXISTS WITH NAME MATCHING <DEST>, THIS PAD WILL BE OVERWRITTEN{bcolors.ENDC}")

def print_dotenv():
    print(f"Please {bcolors.FAIL}configure .env{bcolors.ENDC}")
    print(f"Run with {bcolors.OKBLUE}-h{bcolors.ENDC} or {bcolors.OKBLUE}--help{bcolors.ENDC} for more information")
    
if __name__ == "__main__":
    main(sys.argv[1:])