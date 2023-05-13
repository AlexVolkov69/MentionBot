import os, logging, asyncio

from telegraph import upload_file
 
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


#start
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("𝗛𝗲𝗹𝗹𝗼 𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐁𝐎𝐓🥀 \n\n ➪ 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗰𝗮𝗻 𝘁𝗮𝗴 𝗠𝗲𝗺𝗯𝗲𝗿𝘀 𝗶𝗻 𝗴𝗿𝗼𝘂𝗽 𝗮𝗻𝗱 𝗰𝗵𝗮𝗻𝗻𝗲𝗹🌟 \n ➪ 𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗰𝗮𝗻 𝘁𝗮𝗴 10 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝗮𝘁 𝗮 𝘁𝗶𝗺𝗲🥂 \n\n 𝗜𝗳 𝘂 𝗻𝗲𝗲𝗱 𝗵𝗲𝗹𝗽 𝗷𝘂𝘀𝘁 𝘁𝘆𝗽𝗲 /help 💫 /n/n 𝗸𝗲𝗲𝗽 𝘀𝘂𝗽𝗽𝗼𝗿𝘁𝗶𝗻𝗴 𝗹𝗼𝘃𝗲 𝘂 𝗮𝗹𝗹🌱",
                    buttons=(
                      [
                        Button.url('✚ 𝗔𝗗𝗗 𝗠𝗘 𝗣𝗜𝗥𝗢 ✚', 'https://t.me/mentionzbot?startgroup=true'),   
                      ]
                      [
                         Button.url('𝗨𝗽𝗱𝗮𝘁𝗲𝘀 🥂', 'https://t.me/AnnexBots'), 
                         Button.url('𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🥀', 'https://t.me/AnnexChat'), 
                      ], 
                      [
                         Button.url('𝗬𝗼𝘂𝗧𝘂𝗯𝗲 💤', 'https://youtube.com/@AnnexTech'), 
                         Button.url('𝗢𝘄𝗻𝗲𝗿 🌟', 'https://t.me/AboutAnnex'), 
                      ] 
                   ), 
                    link_preview=False
                   )

#help
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**𝐌𝐄𝐍𝐓𝐈𝐎𝐍 𝐁𝐎𝐓'𝐒 𝗛𝗲𝗹𝗽 𝗠𝗲𝗻𝘂 💞**\n\n 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ➪ @all , #all , /tagall , /all , /call , /tall 🌱 \n\n ➪ 𝗬𝗼𝘂 𝗰𝗮𝗻  𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗰𝗼𝗺𝗺𝗮𝗻𝗱𝘀 𝘄𝗶𝘁𝗵 𝘁𝗲𝘅𝘁 𝘁𝗵𝗮𝘁 𝗳𝗼𝗿 𝘄𝗵𝗮𝘁 𝘂 𝘄𝗮𝗻𝘁 𝘁𝗼 𝘁𝗮𝗴 𝗮𝗹𝗹 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 💤 \n\n ➪ 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :- @all 𝗽𝗼𝗸 𝗺𝗲 😂"
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('𝗨𝗽𝗱𝗮𝘁𝗲𝘀 🥂', 'https://t.me/AnnexBots'), 
                         Button.url('𝗦𝘂𝗽𝗽𝗼𝗿𝘁 🥀', 'https://t.me/AnnexChat'), 
                      ]
                   ), 
                    link_preview=False
                   )

#AnnexOp

#Dont forget to give credits i will pok ur girl friend

#tag
@client.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("𝗨𝘀𝗲 𝘁𝗵𝗶𝘀 𝗶𝗻 𝗰𝗵𝗮𝗻𝗻𝗲𝗹 𝗼𝗿 𝗴𝗿𝗼𝘂𝗽 🌱")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("𝗢𝗻𝗹𝘆 𝗮𝗱𝗺𝗶𝗻 𝗰𝗮𝗻 𝘂𝘀𝗲 𝗶𝘁 😅")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("𝗜 𝗰𝗮𝗻𝘁 𝗺𝗲𝗻𝘁𝗶𝗼𝗻 𝗺𝗲𝗺𝗯𝗲𝗿𝘀 𝗳𝗼𝗿 𝗼𝗹𝗱 𝗽𝗼𝘀𝘁 🥹")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("𝗚𝗶𝘃𝗲 𝗺𝗲 𝗮𝗻 𝗮𝗿𝗴𝘂𝗺𝗲𝗻𝘁 🥂 \n\n 𝐄𝐱𝐚𝐦𝐩𝐥𝐞 :- /tag 𝗛𝗲𝘆, 𝘄𝘁𝗳 𝗮𝗿𝗲 𝘂 𝗱𝗼𝗶𝗻𝗴😂")
  else:
    return await event.respond("𝗥𝗲𝗽𝗹𝘆 𝘁𝗼 𝘁𝗵𝗲 𝗺𝘀𝗴 𝗼𝗿 𝗴𝗶𝘃𝗲 𝘀𝗼𝗺𝗲 𝘁𝗲𝘅𝘁 𝗧𝗼 𝗺𝗲𝗻𝘁𝗶𝗼𝗻 🥀")
    
   if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
    if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


print("𝗬𝗼𝘂𝗿 𝗯𝗼𝘁 𝗵𝗮𝘀 𝘀𝘁𝗮𝗿𝘁𝗲𝗱 𝘀𝘂𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗗𝗿𝗼𝗽 𝘀𝗼𝗺𝗲 𝗻𝘂𝗱𝗲𝘀 𝗼𝗳 𝘂𝗿 𝗚𝗶𝗿𝗹 𝗳𝗿𝗶𝗲𝗻𝗱 𝗶𝗻 𝗼𝘂𝗿 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗰𝗵𝗮𝘁 🌱")
print("𝗔𝗴𝗮𝗶𝗻 𝗶 𝗮𝗺 𝘀𝗮𝘆𝗶𝗻𝗴 𝗱𝗼𝗻𝘁 𝗳𝗼𝗿𝗴𝗲𝘁 𝘁𝗼 𝗴𝗶𝘃𝗲 𝗰𝗿𝗲𝗱𝗶𝘁𝘀 𝗶𝗳 𝘂 𝗻𝗼𝘁 𝘁𝗲𝗮𝗺 𝗽𝘂𝘁𝘀 𝗮 𝗯𝗿𝗼𝗸𝗲𝗻 𝗯𝗲𝗲𝗿 𝗯𝗼𝘁𝘁𝗹𝗲 𝗶𝗻 𝘂𝗿 𝗮𝘀𝘀𝘀𝘀 🤣")
print("𝗜𝗳 𝘂 𝗻𝗲𝗲𝗱 𝗵𝗲𝗹𝗽 𝗷𝗼𝗶𝗻 𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗰𝗵𝗮𝘁 @AnnexChat 💫")
client.run_until_disconnected()
