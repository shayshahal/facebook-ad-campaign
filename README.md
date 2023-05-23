# facebook-ad-campaign

For this project I was tasked to make a python script that logins to a Facebook ad-account and posts a list of all it's campaign's names and their start date. This means writing code that would send a request to Facebook's API in order to fetch the relevant data.
To do this I would need to learn how to use and navigate the Facebook API in order to be able to perform the task's requirements.

First, I search for Meta developer resources that would guide me towards what I need. I then reach the Meta Developer Docs and read about the Facebook API structure:

1. Facebook API uses the term 'Edges' to describe connections between objects (a Graph API).
2. Facebook uses access tokens to allow developers access to the Facebook API (within the token scope/restrictions).
   There are 2 relevant types of tokens for this project:
   User-Access-Token: Temporary token that allow reading the user's data
   App-Access-Token: Permanent token that is able to be generated after you create an App in the Facebook for Developers site. This token allows the developer to connect and make request with the Facebook API.

Lastly I read about the [Facebook-python-business-sdk](https://github.com/facebook/facebook-python-business-sdk) and use the example that is given to similarly initialize the api and make the request for the campaigns.
