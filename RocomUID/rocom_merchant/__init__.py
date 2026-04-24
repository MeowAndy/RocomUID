import re
import json
import time
import asyncio
import pytz
from gsuid_core.sv import SV
from gsuid_core.bot import Bot
from gsuid_core.models import Event
from datetime import datetime, timedelta
from ..utils.rocom_api import wegame_api
from gsuid_core.subscribe import gs_subscribe
from gsuid_core.aps import scheduler
from ..utils.error_reply import get_prefix
from ..rocom_config.rocom_config import RC_CONFIG
from .draw_info_image import draw_merchant_info

PREFIX = get_prefix()
sv_merchant = SV(f'{PREFIX}远行商人事件', priority=5)

@sv_merchant.on_command(('远行商人'))
async def get_merchant_info_list(bot: Bot, ev: Event):
    merchant_info = await wegame_api.get_merchant_info(refresh=True)
    if len(merchant_info) == 0:
        return await bot.send(
            f"远行商人商品未刷新\n可输入[{PREFIX}开启远行商人]订阅远行商人商品信息推送",
            at_sender=True,
        )
    im = await draw_merchant_info(merchant_info)
    await bot.send(im, at_sender=True)

@sv_merchant.on_command(('商人'))
async def get_merchant_info_list_cs(bot: Bot, ev: Event):
    merchant_info = await wegame_api.get_merchant_info_cs()
    await bot.send(str(merchant_info), at_sender=True)

# 每日定点执行远行商人推送
@scheduler.scheduled_job('cron', hour ='*', minute='05')
async def refresh_merchant_info():
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    this_hour = now.hour
    if this_hour not in [8, 12, 16, 20]:
        return
    jishu = 0
    merchant_info = []
    merchant_cd = int(RC_CONFIG.get_config("RC_merchant_cd").data)
    while len(merchant_info) == 0 and jishu < 20:
        await asyncio.sleep(merchant_cd)
        jishu = jishu + 1
        print(f"正在进行第{jishu}次数据获取")
        merchant_info = await wegame_api.get_merchant_info(refresh=True)
    im = await draw_merchant_info(merchant_info)
    datas = await gs_subscribe.get_subscribe('[洛克王国] 远行商人')
    for data in datas:
        await data.send(im)