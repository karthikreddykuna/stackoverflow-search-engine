# Stack overflow Search Engine

## Goal
Our main objective is to fine tune the search result and return most relevant results to the user from stack overflow.

## Documents to look for:

1. app.py (run this file using "python app.py" command from the command prompt or anaconda prompt to run the stack overflow serach engine web application in the web browser)
2. Data file.ipynb (Dataset - running this is not required)
3. Stackoverflowsearchengine Documentation (Documentation Paper)

##Dataset:
   Dataset is taken is from kaggle.
     https://www.kaggle.com/stackoverflow/stackoverflow

## How to run the project:
1. Connect to drexel VPN 
2. Unzip the INFO624-Stackoverflowsearchengine.zip 
3. Install supporting packages using the commands below in anaconda command prompt
	  pip install -r requirements.txt
4.Install the mandatory packages by running the below commands in anaconda command prompt
      pip install flask 
	  pip install elasticsearch	  
5. Enter into unziped folder through anaconda prompt by using the command
     cd ..\INFO624-Stackoverflowsearchengine\
6. run the python file by using following command 
    >>python app.py
7.The server should be up and running on http://127.0.0.1:5000/
8.Copy the address and open it web browser.
