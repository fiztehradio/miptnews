#!/usr/bin/env python3
#-*- coding: UTF 8 -*-

from objs.bot import ExportBot, bot_job, echo
from telegram.ext import Updater, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
bot = ExportBot()
updater = Updater(bot=bot)
dispatcher = updater.dispatcher
echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
j = updater.job_queue
j.run_repeating(bot_job, interval=1800, first=0)
updater.start_polling()
