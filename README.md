# Etherpad-scripts
A collection of simple scripts that wrap the Etherpad API (developed for Etherpad v1.9.2, full docs developed against [here](https://etherpad.org/doc/v1.9.2)).

## Set up
- Clone the repo
- Navigate inside the root folder (hereafter called `etherpad-scripts`)
- (Optional) Create a venv (virtual environment)
    - (Assumes use of Linux, find external guide for Windows or other OS as necessary)
    - `python3 -m venv ./etherpad-venv`
    - `source ./etherpad-venv/bin/activate`
- Install requirements using `pip install -r requirements.txt`
- Configure `.env` file
    - \[Required\] URL - The URL of the etherpad instance (e.g. https://etherpad.example.com) -- **MUST INCLUDE** `https://` where releavnt
    - \[Required\] API_VER - The API version of the etherpad instance (e.g. 1.3.0) -- **Note** that this is not the same as the Etherpad version and can probably be found at `URL/api/` under `currentVersion`
    - \[Optional\] TOKEN - The Etherpad API token, found in the root folder of the Etherpad instance in `APIKEY.txt` 
- Run scripts using `python3 <script_name> <parameters>`
- Running `python3 <script_name> -h` provides a better listing of help information for a specific script