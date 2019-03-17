import requests


def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://123.56.4.230:80/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=458193034,
                                                                                    re_url=redirect_url)
    print(auth_url)


def get_access_token(code="10edefe6652fa4177e1828952d3bc57b"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    re_dict = requests.post(access_token_url, data={
        "client_id": "458193034",
        "client_secret": "77cdd24c7f129c475f89823cf7496e96",
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://123.56.4.230:80/complete/weibo/"
    })

    print(re_dict.json())

# {'access_token': '2.009Ii8iG0OwWAV382897e77fHmGXxD',
# 'remind_in': '157679999', 'expires_in': 157679999,
# 'uid': '6153560292', 'isRealName': 'true'}

# todo
def get_user_info(access="2.009Ii8iG0OwWAV382897e77fHmGXxD"):
    pass


if __name__ == '__main__':
    get_auth_url()
    get_access_token()

