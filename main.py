from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

# Variables, usually should be hidden but here it doesn't really matter
access_token = 'EAANhwOe7TpABAAoaBm8yHgqqZANAIUBDWW4xcgvyDeTlFwZBz4IaRMc97v7bvNQZCwfQmYpGZAKVbqNgS3lc27TOdWA3zZBuERff1BGmOiapAzZAi6uAAsQ7dgD5TcOsMuR9SCkLdhRrTjNzYXFCxlxk2DZAEQFm777HmcgJZBa48ug9BjSqdHQOtnhjPUz9gSsZD'
app_secret = '08befff363aea705da35d1633c3bd701'
app_id = '951906079559312'
id = '739297514555981'


def main():
    # setting up the api
    FacebookAdsApi.init(app_id, app_secret, access_token)

    # fields to be printed
    fields = [
        'name',
        'start_time'
    ]

    # api get call for all campaigns
    campaigns = AdAccount('act_'+id).get_campaigns(fields)

    # print campaigns
    for campaign in campaigns:
        print('name: ' + campaign['name'] +
              '\nstart time: ' + campaign['start_time'])


if __name__ == '__main__':
    main()
