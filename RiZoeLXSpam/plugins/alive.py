from .. import Riz, SUDO_USERS, lightyagamiversion
from .. import ALIVE_PIC
from telethon import events, version
from time import time
from datetime import datetime

RIZ_PIC = ALIVE_PIC if ALIVE_PIC else ""
  

          
rizoel = "✧ 𝐿𝐼𝐺𝐻𝑇𝑌𝐴𝐺𝐴𝑀𝐼 𝑋 𝑆𝑃𝐴𝑀𝑀𝐸𝑅 𝐼𝑍 𝐴𝐿𝐼𝑉𝐸 ✧\n\n"

rizoel += f"┏━━━━━━━━━━━━━━━━━━━\n"

rizoel += f"┣➣ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `3.9.6`\n"

rizoel += f"┣➣ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ** : `{version.__version__}`\n"

rizoel += f"┣➣ ** ʟɪɢʜᴛʏᴀɢᴀᴍɪ x sᴘᴀᴍ ᴠᴇʀsɪᴏɴ**  : `{rizoelversion}`\n"
    
rizoel += f"┣➣ **sᴜᴘᴘᴏʀᴛ** : [MESSAGE](https://t.me/illusion_07)\n"

rizoel += f"┣➣ **ᴄᴏɴᴛᴀᴄᴛ** : [MESSAGE](https://t.me/illusion_07)\n"

rizoel += f"┗━━━━━━━━━━━━━━━━━━━\n\n"

rizoel += f"🖤 [TG](https://https://t.me/illusion_07) 🖤"            
                                    
@Riz.on(events.NewMessage(pattern=r"\.alive"))
async def alive(event):
    if event.sender_id in SUDO_USERS:
     await Riz.send_file(event.chat_id,
                                  RIZ_PIC,
                                  caption=rizoel)
    
