# facebook-ad-campaign

## First task

For this project I was tasked to make a python script that logins to a Facebook ad-account and posts a list of all it's campaign's names and their start date. This means writing code that would send a request to Facebook's API in order to fetch the relevant data.
To do this I would need to learn how to use and navigate the Facebook API in order to be able to perform the task's requirements.

First, I search for Meta developer resources that would guide me towards what I need. I then reach the Meta Developer Docs and read about the Facebook API structure:

1. Facebook API uses the term 'Edges' to describe connections between objects (a Graph API).
2. Facebook uses access tokens to allow developers access to the Facebook API (within the token scope/restrictions).
   There are 2 relevant types of tokens for this project:
   User-Access-Token: Temporary token that allow reading the user's data
   App-Access-Token: Permanent token that is able to be generated after you create an App in the Facebook for Developers site. This token allows the developer to connect and make request with the Facebook API.

Lastly I read about the [Facebook-python-business-sdk](https://github.com/facebook/facebook-python-business-sdk) and use the example that is given to similarly initialize the api and make the request for the campaigns.

## Second task

This time I was asked to use Flask in order to create an endpoint localhost:3000/campaigns which will be used to output the
campaigns list. I was also tasked with creating environment variables and files that will allow users to be able to install and use the code on their own machine.

For this I will have to read about Flask, dotenv and virtual environments in order to understand how to achieve the requirements.

I go straight to the Flask documentation and there I find most of the answers. I read the [flask Installation page](https://flask.palletsprojects.com/en/2.3.x/installation/) which right away leads me to:

1. python-dotenv docs (Environment variables were not a foreign subject to me so a skim is all I need)
2. Python's venv docs which explains most of what I need to do in relation to virtual environment setup.

After I read a bit more of the Flask docs I'm able to write the code.

## Usage

In the your powershell, write the following to create a virtual environment:

```
> py -3 -m venv .venv
```

Activate it with the following:

```
> .venv\Scripts\activate
```

Then install the dependencies:

```
python3 -m pip install -r requirements.txt
```

In order to set your own environment variables, create a .env file in the root directory of the project.

```
|--facebook-ad-campaign
|-- main.py
|-- .env <----
```

For more information, go to the [python-dotenv documentation](https://github.com/theskumar/python-dotenv#readme).

Lastly, run the script with the following command:

```
python3 main.py
```
