#!/usr/bin/env python3
#-*- coding: UTF 8 -*-

from objs.bot import ExportBot, bot_job
from telegram.ext import Updater, Job
import logging
# bot = ExportBot()
# bot.detect()
# bot.public_posts()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
					level=logging.INFO)
bot = ExportBot()
updater = Updater(bot=bot)
j = updater.job_queue
j.run_repeating(bot_job, interval=1800, first=0)
updater.start_polling()
