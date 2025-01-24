# Etherpad-scripts
A collection of simple scripts that wrap the Etherpad API (developed for Etherpad v1.9.2, full docs developed against [here](https://etherpad.org/doc/v1.9.2))

## Requirements
- Python 3 (tested with Python 3.12.8)

## Setup
- Clone the repo
- Navigate inside the root folder (`etherpad-scripts/`)
- (Optional) Create a venv (virtual environment)
    - (Assumes use of Linux, find an OS-specific guide for Windows or other OS if necessary)
    - In the root folder, run `python3 -m venv ./etherpad-venv` to create the venv
    - Now run `source ./etherpad-venv/bin/activate` to activate the venv
- Install requirements using `pip install -r requirements.txt`
- Configure `.env` file
    - **\[Required\]** URL - The URL of the etherpad instance (e.g. https://etherpad.example.com) -- **MUST INCLUDE** `https://` where relevant
    - **\[Required\]** API_VER - The API version of the etherpad instance (e.g. 1.3.0) -- **Note** that this is not the same as the Etherpad version and can probably be found at `<URL>/api/` as the value of `currentVersion`
    - **\[Optional\]** TOKEN - The Etherpad API token, found in the root folder of the Etherpad instance in `APIKEY.txt`
## Usage
- Run scripts using `python3 <script_name> <parameters>`
- Running `python3 <script_name> -h` provides a better listing of help information for a specific script

## Scripts
### move-pad.py
This script wraps the API method `movePad` (since Etherpad does not seem to natively support renaming a file with the change showing in the list of pads)

Required parameters:
- -s, --source : The name of the pad to move
- -d, --dest : The name the pad will be moved to

Optional parameters:
- -t, --token : The Etherpad API token. If this is not specified, the token in `.env` will be used. If both are set, the command line parameter takes priority

### delete-pad.py
This script wraps the API method `deletePad`

Required parameters:
- -p, --pad : The name of the pad to delete

Optional parameters:
- -t, --token : The Etherpad API token. If this is not specified, the token in `.env` will be used. If both are set, the command line parameter takes priority
