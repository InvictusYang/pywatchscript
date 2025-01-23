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
    'Authorization': 'Bearer zO8OOudrrmqi5-G0oetHxJIvu7N3IVtElJmrPp5-Oi4',
    'Cookie': 'currency=CNY; cf_clearance=P5QmHxzG3z73aYLsx8h4HcvnhV2YarpWs5W4ABYhI9E-1737589960-1.2.1.1-mlP3tQclJeEn6CgOjb3XyFzY_kWXkGwRyOwtG18clVG2rPxV3HTnGXJakEMmZbsjIWJbq4ujhAxqk.Q0fjHD82ZZQLM25eA_J2Y.V2nL4K7oSPfW.u9x141rZy6yMopt74W9LX5aDf8aKaroNXtvZxSZEk7MABA6VlIVMzM479Q9fkEGcRuGhW12Q5ZrklXpaQutB5NFmeR3uxL70aqUPWpIn9AonY3ti8pfjJb8JLi.XpckmVS30Gh0RmfpHikiWgPx1Na_ThK1VvRpxhOckVvxVQrtSq0p1g9Rhd3HUMs; __cf_bm=bxNSR5xO51leIEEOlAUeDsMQFyQmJIuRx1EvRn84Boo-1737591809-1.0.1.1-7Tk6w50wV87WqntCbvNLSDaO4GvURdb8WFwGJX9qxTFhHj2ruDCitbRDHmRDKSJEIa2GGCxsBp49yYlOscbkxg',
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
