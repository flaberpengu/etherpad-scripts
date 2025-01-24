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
    pad = ""
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

    ##Handle args
    try:
        opts, args = getopt.getopt(argv, "hp:t:", ["help", "pad=", "token="])
    except getopt.GetoptError:
        print_help(True)
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help(False)
            sys.exit(0)
        elif opt in ("-p", "--pad"):
            pad = arg
        elif opt in ("-t", "--token"):
            token = arg
    
    if pad == "":
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
    url_string = url + "/api/" + api_ver + "/deletePad"
    payload = {
        "apikey": token,
        "padID": pad,
    }
    response = requests.post(url_string, params=payload)

    ##Handle response
    try:
        response_dict = json.loads(response.text)
        if response_dict["code"] == 0:
            print(f"{bcolors.OKGREEN} ✔ {bcolors.ENDC}Successfully deleted {pad}")
        else:
            print(f"{bcolors.FAIL} ⨯ {bcolors.ENDC}Unsuccessful - {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Failed: {response.text}")

def print_help(shortHelp):
    if shortHelp:
        print(f"{bcolors.OKBLUE}Usage: {bcolors.ENDC}delete-pad.py -p <pad> [OPTIONAL: -t <api_token>]")
        print(f"Run with {bcolors.OKBLUE}-h{bcolors.ENDC} or {bcolors.OKBLUE}--help{bcolors.ENDC} for more information")
    else:
        print('delete-pad.py -p <pad> [OPTIONAL: -t <api_token>]')
        print(f"{bcolors.OKBLUE}-p, --pad : {bcolors.ENDC}The name of the pad to delete")
        print(f"{bcolors.OKCYAN}[OPTIONAL]: {bcolors.ENDC}{bcolors.OKBLUE}-t, --token : {bcolors.ENDC}The Etherpad API token")
        print(f"If token is not passed as a parameter, it must be set in the .env file as {bcolors.UNDERLINE}TOKEN{bcolors.ENDC}. If it is both set in .env and passed as a parameter, the parameter takes priority")
        print(f"{bcolors.BOLD}The .env file must be set up with {bcolors.UNDERLINE}URL{bcolors.ENDC}{bcolors.BOLD} and {bcolors.UNDERLINE}API_VER{bcolors.ENDC}")
        print(f"{bcolors.BOLD}If you wish to use spaces, hyphens, or other special characters in a pad name, surround it in \"quotation marks\"{bcolors.ENDC}")
        print(f"{bcolors.WARNING}WARNING: THIS ACTION CANNOT BE UNDONE{bcolors.ENDC}")

def print_dotenv():
    print(f"Please {bcolors.FAIL}configure .env{bcolors.ENDC}")
    print(f"Run with {bcolors.OKBLUE}-h{bcolors.ENDC} or {bcolors.OKBLUE}--help{bcolors.ENDC} for more information")

if __name__ == "__main__":
    main(sys.argv[1:])