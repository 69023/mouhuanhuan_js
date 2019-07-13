import requests
import execjs
import json

conn = requests.post(
    url="https://www.huanhuanhuishou.com/Index/getGoodsInfo",
    headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
    }
)

code = conn.headers.get('Content-Text')
res = conn.text

with open('000.js', 'r') as file:
    js = file.read()

ctx = execjs.compile(js)
result = ctx.call('get_json_str', res, code)

result = json.loads(result)

print(json.dumps(result, ensure_ascii=False))
