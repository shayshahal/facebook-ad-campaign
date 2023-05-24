import os
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi
from flask import Flask
from flask import render_template
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()


@app.route('/')
def index():
    return '<a href="/campaigns">go to campaigns</a>'


@app.route("/campaigns")
def campaigns():
    FacebookAdsApi.init(os.getenv('APP_ID'), os.getenv(
        'APP_SECRET'), os.getenv('ACCESS_TOKEN'))

    # fields to be printed
    fields = [
        'name',
        'start_time'
    ]

    # api get call for all campaigns
    campaigns = AdAccount('act_'+os.getenv('ID')).get_campaigns(fields)

    return render_template('campaigns.html', campaigns=campaigns)

if __name__ == '__main__':
    app.run(port=3000)