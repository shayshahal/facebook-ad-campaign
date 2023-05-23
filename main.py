from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi


access_token = 'EAANhwOe7TpABAAoaBm8yHgqqZANAIUBDWW4xcgvyDeTlFwZBz4IaRMc97v7bvNQZCwfQmYpGZAKVbqNgS3lc27TOdWA3zZBuERff1BGmOiapAzZAi6uAAsQ7dgD5TcOsMuR9SCkLdhRrTjNzYXFCxlxk2DZAEQFm777HmcgJZBa48ug9BjSqdHQOtnhjPUz9gSsZD'
app_secret = '08befff363aea705da35d1633c3bd701'
app_id = '951906079559312'
id = '739297514555981'


def main():
    FacebookAdsApi.init(app_id, app_secret, access_token)


if __name__ == '__main__':
    main()