# -*- coding: utf-8 -*-
import itchatmp

from .abstract import WechatService
from ...settings import *


class WechatMP(WechatService):

    def _start(self):
        itchatmp.update_config(itchatmp.WechatConfig(
                token=WECHAT_TOKEN,
                appId=WECHAT_APP_ID,
                appSecret=WECHAT_APP_SECRET),
            filterRequest=True)
        itchatmp.run()

    def _stop(self):
        pass

    @itchatmp.msg_register(itchatmp.content.TEXT)
    def handle_text(self, msg):
        self._handle_text(msg)

    @itchatmp.msg_register(itchatmp.content.VOICE)
    def handle_voice(self, msg):
        self._handle_voice(msg)

    @itchatmp.msg_register(itchatmp.content.IMAGE)
    def handle_image(self, msg):
        self._handle_image(msg)

    @itchatmp.msg_register(itchatmp.content.VIDEO)
    def handle_video(self, msg):
        self._handle_video(msg)