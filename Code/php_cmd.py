import requests
import base64
import re
find_pre = re.compile(r"<pre>((?:.|\n)*?)</pre>")
url = "http://localhost/cmd.php?cmd="
def post():
    cmd = input(u"请输入命令:")
    bash = base64.b64encode(bytes(cmd,encoding='utf-8'))
    print(bash)
    temp = url + str(bash,encoding="utf-8")
    resp = requests.get(temp)
    text = re.findall(find_pre,resp.text)[0]
    text = base64.b64decode(text)
    print(text.decode("gbk"))

while True:
    post()

