# -*- coding: utf-8 -*-

import sys

reload(sys)  
sys.setdefaultencoding("UTF8")
# LANGUAGE FILE

START_MSG = str("Hey! 😊 \n \nWelcome to the *ZigZagBot*! 😱🚀 \nDeveloped by @WebShark25! \n \nAll bot commands: \n💢 _/help_ - Get help message \n💢 _/echo <msg>_ - Echoes the message \n💢 _/id_ - Get your ID & Group's ID \n \n_More commands comming soon!_ \n \nI Hope you enjoy it! ").encode("utf-8")
START_BUTTONS = ("/id", "/echo", "/test", "/start", "/help", "Send feedback") # ONLY 6 BUTTONS. 2x3 LINES
TEST_MSG = "This is a test message."
SHARE_CONTACT_MSG = "Please share your contact to the bot (in a private message)."
NO_ECHO_IN_SUPERGP_MSG = "Unfortunately I wont reply to messages sent in a supergroup to prevent spamming."
ECHO_REPLY_MSG = "Please enter a text so I reply to it!"
ERROR_MSG = "Error occured."
CONTACT_RECIEVED_MSG = "New contact recieved:"
CONTACT_FORWARDED_MSG = "Contact successfully forwarded!"
# {0} = name | {1} = gp title
GP_GREETING_MSG = "Hey *{0}*! \n \nWelcome to the group *{1}* 😊 \n \n_Have fun & Enjoy!_"
GP_FAREWELL_MSG = "Oh no 😕 \n*{0} left the group ☹️"
# {0} = name | {1} = id | {2} = gp id
ID_MSG = "💢 Your name: *{0}* \n💢 Your ID: *{1}* \n "
INGP_ID_MSG = "💢 Group ID: *{2}*"
NON_ADMIN_ADDED_BOT_MSG = "Im sorry ☹️ \nIm not authorized to join groups by normal members. \nOnly *admins* can add me to groups."
BOT_JOINED_MSG = "Hey😧! I am here, At your service."
MESSANGER_JOIN_MSG = "Now sending feedback. \nPlease enter your message!"
MESSANGER_LEAVE_MSG = "Thanks for your feedback! Exiting."


