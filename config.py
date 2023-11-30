import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "") #⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "") #⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") #⚠️ Required
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "") #⚠️ Required
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","Cluster0")     
    DB_URL  = os.environ.get("DB_URL","") #⚠️ Required
 
    # other configs
    TG_MAX_SIZE = 2040108421
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()] #⚠️ Required
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") #⚠️ Required Username without @
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "")) #⚠️ Required
    FLOOD = int(os.environ.get("FLOOD", '10'))
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))



class Txt(object):
   class Txt(object):
    # part of text configuration
    START_TXT = """<b>Hᴀɪ {} 👋,
    
I Aᴍ Fɪʟᴇ Rᴇɴᴀᴍᴇ Bᴏᴛ Wɪᴛʜ Cᴜsᴛᴏᴍ Tʜᴜᴍʙɴᴀɪʟ & Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ.
Aɴᴅ Rᴇɴᴀᴍᴇ Wɪᴛʜᴏᴜᴛ Dᴏᴡɴʟᴏᴀᴅ 💯 Fᴜʟʟʏ Wᴏʀᴋ Oɴ Tɢ

Pʟᴇᴀsᴇ Sʜᴀʀᴇ Tʜɪs Bᴏᴛ Tᴏ Yᴏᴜʀ Fʀɪᴇɴᴅs 💝.</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├🤖 ᴍy ɴᴀᴍᴇ : {}
├🖥️ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/TG_LINKS_CHANNEL>CLICK HERE</a> 
├👨‍💻 Pʀᴏɢʀᴀᴍᴇʀ : <a href=https://t.me/TG_UPDATES1>CLICK HERE</a>
├📕 Lɪʙʀᴀʀy : <a href=https://github.com/Kushalhk>CLICK HERE</a>
├✏️ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org>Pyᴛʜᴏɴ 3</a>
├💾 Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com>Mᴏɴɢᴏ DB</a>
├📊 Bᴜɪʟᴅ Vᴇʀꜱɪᴏɴ: Rᴇɴᴀᴍᴇʀ V3.0.0</a></b>     
╰───────────────⍟ """

    HELP_TXT = """
  <b><u>Hᴏᴡ Cᴀɴ I Hᴇʟᴘ Yᴏᴜ?</b></u>

ɪ ᴄᴀɴ ʀᴇɴᴀᴍᴇ ᴍᴇᴅɪᴀ ᴡɪᴛʜᴏᴜᴛ ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ ɪᴛ!
sᴘᴇᴇᴅ ᴅᴇᴘᴇɴᴅs ᴏɴ ʏᴏᴜʀ ᴍᴇᴅɪᴀ ᴅᴄ.

ɪᴜsᴛ sᴇɴᴅ ᴍᴇ ᴍᴇᴅɪᴀ ᴛᴏ ʀᴇɴᴀᴍᴇ
sᴇɴᴅ ɪᴍᴀɢᴇ ᴛᴏ sᴇᴛ ᴛʜᴜᴍʙɴᴀɪʟ 
ᴛᴏ sᴇᴇ ᴄᴜsᴛᴏᴍ ᴛʜᴜᴍʙɴᴀɪʟ ᴘʀᴇss /show_thumbnail

ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/TG_SUPPORT_GROUP>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</b></u>
» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : <a href=https://github.com/Kushalhk>𝐑𝐄𝐍𝐀𝐌𝐄 𝐁𝐎𝐓</a>
» 𝗛𝗢𝗪 𝗧𝗢 𝗗𝗘𝗣𝗟𝗢𝗬 : <a href=https://telegram.me/TG_LINKS_CHANNEL>CLICK HERE</a>
</a> """

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣⪼ 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""

    SETTINGS_TXT = """<b>
ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ꜱᴇᴛᴜᴘ ʏᴏᴜʀ ꜱᴇᴛᴛɪɴɢs: </b>"""

    CAP_TXT = """<b>
<u>📑 Hᴏᴡ Tᴏ Sᴇᴛ Cᴜꜱᴛᴏᴍ Cᴀᴩᴛɪᴏɴ</u>

ᴏᴋᴇʏ,
ꜱᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ᴄᴀᴩᴛɪᴏɴ
ɢᴏ ᴛᴏ ʜᴇʟᴩ ᴍᴇɴᴜᴇ ᴛᴏ ᴄʜᴇᴄᴋ ᴩᴀʀꜱᴇ_ᴍᴏᴅᴇ ᴇxᴀᴍᴩʟᴇꜱ

ᴇɢ:- 

<b>{file_name}</b>

File Size: <b>{file_size}</b>

Join us :- @TG_UPDATES1 </b>"""

    THUMBNAIL_TXT = """<b>
 /del_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Dᴇʟᴇᴛᴇ Yᴏᴜʀ Oʟᴅ Tʜᴜᴍʙɴɪʟᴇ.
 /view_thumb Uꜱᴇ Tʜɪꜱ Cᴏᴍᴍᴀɴᴅ Tᴏ Vɪᴇᴡ Yᴏᴜʀ Cᴜʀʀᴇɴᴛ Tʜᴜᴍʙɴɪʟᴇ
</b>"""
  
