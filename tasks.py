import requests
import logging

from celery import Celery
from celery.schedules import crontab

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Celery('tasks', broker='redis://localhost:6379/0')


BOT_ID = "7692621050:AAGSFehqYAJTz3TTrrkGczKqdK1wqhcLVdk"
NOTIF_URL = f"https://api.telegram.org/bot{BOT_ID}/sendMessage"

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN;q=0.9',
    'Authorization': 'Bearer CGG4tuYfBacuIhnZ_ZBdH7UiwrTqQcqMSdD8ZTDoBso',
    'Cookie': 'crisp-client%2Fsession%2Fe3482bfe-6283-41af-a0ce-2b5322ec465e=session_a780a6a9-4bfe-460a-a487-f3db99dab941; currency=CNY; cf_clearance=0pOJ96A0bOcSuYjTYzlI17lFLoBEOU6.3FRPp6CyJ9g-1735948956-1.2.1.1-m.XjsxGN7UcN3BigMWkP7Gd1f0j82ESWFz11j3Un9RWpbGlFago1kSpsGG7IZyhMWGhleA8a_ETiPmJx.BEXFx80nNdIq5OJzPW3GabYU.DXK43TaH9bWFOIPayOpwJnGLxMdXuvGUsitJe2DysJvgWP0nMsmNHlk.jLq2G_8QXDFM55Fzqxhxr6DBKws8xkNoPl0W73EgFVM7p6MgqBgwwJ3co4i3cSQlQRxE6vL3D2XweepnyQG36kZzQJTQGzN9IbqpDqLaJMHGI_jeniq8CIlkoQX0wmvdJu0cXkIpCH.Gv3R1.nFe44nnVTLQn.pp1cpCPN77OMnHK7al7PhPWZlu0vuUK_8oEN55TNQXFDmkmPBzM2zuKdA_E8BJD6Bb85bvC.SKD0fVO72FxiIA; __cf_bm=jK4Qx1lWENexZwUGMKyJINiZm9Lhl38NtnIwFNLf4Xo-1735970015-1.0.1.1-2yN_NEZ7Q7uCvR4dJbg6ftHEb1nJkatmd2lVD2_PtCMc9csz2fzLHkjFWP_AmI3YhgObiZeVqq4CKY_FndVtWw',
    'Origin': 'https://d1t9c65g8vg9.basicex.com',
    'Priority': 'u=1, i',
    'Referer': 'https://d1t9c65g8vg9.basicex.com/',
    'Sec-Ch-Ua': '"Microsoft Edge";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
}


@app.task
def send_notification():
    # 构造请求 URL
    url = f"https://api.basicex.com/backstage/manage/overview/todo"
    response = requests.get(url, headers=headers).json()
    params = response['data']

    for param in params:
        if param['code'] == 'MultipleAignatureApproval' and param['num'] > 0:
            requests.post(
                url=NOTIF_URL,
                data={'chat_id': "-4568198158", 'text': f"有新的多签审批，请及时处理！"}
            )
