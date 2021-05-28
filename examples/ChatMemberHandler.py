
from telebot import types,TeleBot,AsyncTeleBot

bot = TeleBot(<YourBotToken>)
MyChannelID = -123456789
AdminChatID = 987654321
MyChannelMembers = []

#with this function your bot leave joined group or channels if Adder is not Admin
@bot.chat_member_handler(content_types=['bot_joins_group','bot_joins_channel'])
def LeaveSpamChats(message):
    if message.from_user.id != AdminChatID:
        bot.leave_chat(message.chat.id)

#simple function to list channel members Also you can do this with your groups
@bot.chat_member_handler(content_types=['channel_new_member','channel_member_left'])
def ChannelMember(message):
    if message.content_type == 'channel_new_member':
        if message.chat.id == MyChannelID:
            MyChannelMembers.append(message.new_chat_member.from_user.id)
    elif message.content_type == 'channel_member_left':
        if message.chat.id == MyChannelID:
            if message.new_chat_member.from_user.id in MyChannelMembers:
                MyChannelMembers.remove(message.new_chat_member.from_user.id)

#simple function for detect if our bot upgrade to admin in some groups
@bot.chat_member_handler(content_types=['bot_upgraded_to_group_admin'])
def IfBotUpgradeToGroupAdmin(message):
    bot.send_message(message.chat.id,"Now I'M Admin Here :)")

    

bot.polling(none_stop=True)
