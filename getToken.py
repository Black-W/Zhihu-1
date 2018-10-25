# getToken.py
from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

TOKEN_FILE = 'token.pkl'
client = ZhihuClient()

try:
    client.login('email_or_phone', 'password')
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('email_or_phone', 'password', captcha)

client.save_token(TOKEN_FILE)
