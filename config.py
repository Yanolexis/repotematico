import os
import ProxyCloud

BOT_TOKEN =  os.environ.get('bot_token','')
API_ID =  os.environ.get('api_id','')
API_HASH = os.environ.get('api_hash','')
SPLIT_FILE = 1024 * 1024 * int(os.environ.get('split_file','99'))
ROOT_PATH = 'root/'
ACCES_USERS = os.environ.get('tl_admin_user','')
PROXY = ProxyCloud.parse(os.environ.get('proxy_enc',''))

if PROXY:
  print(f'Proxy {PROXY.as_dict_proxy()}')
