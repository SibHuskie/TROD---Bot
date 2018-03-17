import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import random
import pickle
import os
import requests
import json
import time
from gtts import gTTS
from boto.s3.connection import S3Connection

''''''

Client = discord.Client()
bot_prefix= "}"
client = commands.Bot(command_prefix=bot_prefix)
server = discord.Server(id='414089074870321153')
footer_text = "Tʜᴇ Rᴇᴀʟᴍ Oғ Dᴀʀᴋɴᴇss"
s3 = S3Connection(os.environ['BOT_TOKEN'])

attacks = ["Punches the opponent :punch: ", "Kicks the opponent :boot: ", "Throws the opponent :raised_hands: ", "Stabs the opponent :dagger: ", "Shoots the opponent :gun: ",
           "Sets the opponent on fire :fire: ", "Poisons the opponent :syringe: ", "Throws a bomb at the opponent :bomb: ", "Uses a shield to deal damage with the same attack as the opponent's :shield: ", "Chokes the opponent using chains :chains: ",
           "Cuts the opponent :knife: ", "Hits the opponent's head with a hammer :hammer: ", "Uses dark magic to attack the opponent :skull_crossbones: ", "Casts a spell on the opponent :sparkles: ", "Pukes at the opponent :nauseated_face: ",
           "Scares the opponent :ghost: ", "Summons a demon to attack the opponent :smiling_imp: ", "Transforms into a robot to attack the opponent :robot: ", "Farts at the opponent :dash: ", "Summons a tornado near the opponent :cloud_tornado: ",
           "Summons a meteor and hits the opponent with it :comet: ", "Hits the opponent with lightning :zap: ", "Freezes the opponent :snowflake: ", "Cripples the opponent :boom: ", "Shoots the opponent using a bow and arrow :bow_and_arrow: ",
           "Drives over the opponent :red_car: ", "Chops off the opponent's leg :crossed_swords: ", "Drains some of the opponent's life :broken_heart: ", "Steals the opponent's soul :black_heart: ", "Stuns the opponent :octagonal_sign: ",
           "Uses nuclear energy to attack the opponent :radioactive: ", "Blinds the opponent :eye: ", "Deafens the opponent :ear: ", "Uses mind control on the opponent :alien: ", "Summons minions to attack the opponent :busts_in_silhouette: ",
           "Traps the opponent :spider_web: "]

choices = ["rock", "paper", "scissors"]

suicidemsgs = ["was mentally ill and couldn't keep living with it so they decided to commit suicide!",
               "had anxiety for way too long so they took their own life away!",
               "had a bipolar disorder which made them commit suicide!",
               "was depressed for a few years, not having any hope left, they killed themselves!",
               "had schizophrenia, living with that made them kill themselves!",
               "was physically abused and that experience made them commit suicide!",
               "was sexually abused, later that day they took their own life by jumping off a plane!",
               "lived in war and terror for far too long, today is the day they had enough and commited suicide!",
               "was bullied everyday, in school, outside and on the internet. Not having any friends, they decided to kill themselves, thinking the world would be a better place without them!",
               "had some sort of a personality disorder, which made them commit suicide!",
               "was addicted to drugs. One day they took a few more pills than they were supposed to, later that day they were found dead in their bathroom!",
               "had an eating disorder, thinking that they are not meant to be in this world, they took their own life!",
               "was lonely their whole life, not having anyone to talk to, they decided to leave this world!",
               "had relationship problems, their partner leaving them and telling them to kill themselves made them commit suicide!",
               "felt lonely after their whole family was killed, they decided to join them in the after life by killing themselves!",
               "didn't have any motivation or hope left, so they took their own life away by overdosing!",
               "commited suicide! Too bad there is no one to leave a flower on their grave...",
               "died! Ok, that's it they just died! They totally didn't commit suicide!!",
               "put a rope around their neck and died!",
               "overdosed and died!",
               "tried to commit suicide, but failed! Better luck next time, I guess.",
               "was forced to commit suicide by the dark lord!",
               "killed themselves after losing their diamonds in minecraft!",
               "had no internet connection for over 5 seconds, later that day, they commited suicide!",
               "didn't have a life! They killed themselves!",
               "watched boku no pico, few seconds later they decided to kill themselves!",
               "lost all of their hentai, after not being able to find it, they commited suicide!",
               "saw Zero's face reveal, they commited suicide after that!",
               "got all of their memes stolen, not having any memes left, they decided to kill themselves!",
               "killed themselves!",
               "realised how shitty this server actually is, later that day they commited suicide!"]

killmsgs = ["beating them with a baseball bat covered with barbed wire!",
            "breaking all their bones with chains!",
            "shooting them with a shotgun!",
            "drowning them in a glass of water!",
            "throwing them into a pool with sharks!",
            "roasting the shit out of them!",
            "throwing them out of a plane!",
            "pushing them off a mountain!",
            "farting at their face!",
            "pushing them into a volcano!",
            "spamming their DMs!",
            "stealing their memes!",
            "stealing their chocolate!",
            "stealing their diamonds on their minecraft server!",
            "throwing a bomb at them!",
            "nuking them!",
            "breaking their toilet!",
            "hacking their toaster!",
            "trapping them in a cage with hungry lions!",
            "hacking their car while they were driving!",
            "hitting their private spot!",
            "poisoning their food!",
            "playing earrape too loud!",
            "putting them in the hunger games!",
            "putting them in the maze!",
            "making them watch furry porn!",
            "making them use internet explorer!",
            "driving over them with a tank!",
            "shooting them with a tank!",
            "trapping them in their mind!",
            "sending them to the realm of darkness!",
            "cutting them to death!",
            "torturing them til they died!",
            "sending them to hell!",
            "selling their soul to the devil!",
            "leaking their browsing history!",
            "setting them on fire!"]

eightballmsgs = ["Yes!",
                 "No!",
                 "Probably!",
                 "Most likely!",
                 "Probably not!",
                 "Definitely!",
                 "Definitely not!",
                 "Of course!",
                 "Of course not!",
                 "WTF no!",
                 "Hell yeah!"]

roasts = ["I saw a piece of shit today. It reminded me of you.",
          "your face is a physical weapon.",
          "I know you from somewhere. Oh yea, I see you in the trashcan."
          "don't worry, you're not adopted... yet. We still haven't found anyone who wants you.",
          "unless your name is 'Google', stop acting like you know everything.",
          "if I wanted to kill myself I would climb up your ego and jump in your IQ",
          "you are so stupid that you got hit by a parked car.",
          "you're so fat that when god created light, you were asked to move out of the way.",
          "I heard you were taken to a dog show and you won.",
          "you suck so much, I can use you as a vacumcleaner.",
          "maybe you should stop making fun of others just to get attention, cause the world doesn't rotate around your crap looking ass.",
          "try not to spit when you talk, we don't need a public shower here.",
          "you remind me of Zero, eew.",
          "I can't breathe when I see you... cause I'm suffocating of your bullshit.",
          "your mom is twice the man you will ever be.",
          "you have the right to remain silent, cause what ever you say will be stupid anyways.",
          "the only thing you are good at is being a cunt.",
          "it's hard for you isn't it? Not to be a dick.",
          "it's hard to ignore you, mostly cause you smell like shit.",
          "you must've fallen from Mars, cause you clearly can't understand anything happening around you.",
          "did you fall from Heaven? Cause so did Satan.",
          "you're so ugly, you went to an ugly competition and they said 'No professionals allowed!'.",
          "you really shouldn't try cooking, cause the last time you did, it ended with 3 houses being on fire.",
          "did Satan send you to kill people? Cause your smell is killing me.",
          "I'd give you a nasty look but you've already got one.",
          "if laughter is the best medicine, your face must be curing the world.",
          "the only way you'll ever get laid is if you crawl up a chicken's ass and wait.",
          "scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.",
          "your family tree must be a cactus because everyone on it is a prick.",
          "someday you'll go far... and I hope you stay there.",
          "save your breath, you'll need it to blow your date.",
          "the zoo called. They're wondering how you got out of your cage?",
          "you have something on your chin... no, the 3rd one down.",
          "thought of you today. It reminded me to take the garbage out.",
          "you're so ugly when you look in the mirror, your reflection looks away.",
          "it's better to let someone think you're stupid than open your mouth and prove it.",
          "were you born this stupid or did you take lessons?",
          "calling you an idiot would be an insult to all stupid people.",
          "I just stepped in something that was smarter than you... and smelled better too."]

huglinks = ["https://i.imgur.com/yE2RnXK.gif",
            "https://i.imgur.com/R9sYxk8.gif",
            "https://i.imgur.com/iLBEoKv.gif",
            "https://i.imgur.com/cc554e8.gif",
            "https://i.imgur.com/1dqkjHe.gif",
            "https://i.imgur.com/Ph8GTqg.gif",
            "https://i.imgur.com/G6EnOxd.gif",
            "https://i.imgur.com/ZxwHn5Y.gif",
            "https://i.imgur.com/movPIsP.gif",
            "https://i.imgur.com/tKlfSgo.gif",
            "https://i.imgur.com/ICg9nCr.gif",
            "https://i.imgur.com/yC95DC2.gif",
            "https://i.imgur.com/hRYXNKX.gif",
            "https://i.imgur.com/br3bGQc.gif",
            "https://i.imgur.com/IcNGAQD.gif"]

patlinks = ["https://i.imgur.com/8eApUKG.gif",
            "https://i.imgur.com/qVcP9Pt.gif",
            "https://i.imgur.com/X9hKO2p.gif",
            "https://i.imgur.com/v8cRPH9.gif",
            "https://i.imgur.com/N6C7C30.gif",
            "https://i.imgur.com/M9QPcY6.gif",
            "https://i.imgur.com/oUSdjX6.gif",
            "https://i.imgur.com/mFFr4e0.gif",
            "https://i.imgur.com/3F7kmCd.gif",
            "https://i.imgur.com/7yFvJ6m.gif",
            "https://i.imgur.com/y3La9yP.gif"]

kisslinks = ["https://i.imgur.com/0Ri9sfq.gif",
             "https://i.imgur.com/EMdpmXW.gif",
             "https://i.imgur.com/Y9iLoiv.gif",
             "https://i.imgur.com/ZlqZy8S.gif",
             "https://i.imgur.com/ySav1IQ.gif",
             "https://i.imgur.com/ZGfrn2d.gif",
             "https://i.imgur.com/glwWeUl.gif",
             "https://i.imgur.com/j5hDl7V.gif",
             "https://i.imgur.com/w7mVYty.gif",
             "https://i.imgur.com/FJ5bckO.gif",
             "https://i.imgur.com/KqVmVU7.gif",
             "https://i.imgur.com/EM1C9a6.gif",
             "https://i.imgur.com/TACVpH9.gif",
             "https://i.imgur.com/opiHLtc.gif",
             "https://i.imgur.com/LylJAea.gif"]

nomlinks = ["https://i.imgur.com/E1eQPfu.gif",
            "https://i.imgur.com/UUZY3Rb.gif",
            "https://i.imgur.com/Zd6fIpA.gif",
            "https://i.imgur.com/i2NaBS7.gif",
            "https://i.imgur.com/Up5J6Nn.gif",
            "https://i.imgur.com/J5MLku7.gif",
            "https://i.imgur.com/7yYgZXE.gif"]

throwlinks = ["https://i.imgur.com/o9j2oNi.gif",
              "https://i.imgur.com/wSb8aux.gif",
              "https://i.imgur.com/QO8TrkK.gif",
              "https://i.imgur.com/Ts3Cc52.gif",
              "https://i.imgur.com/D3ggzfW.gif",
              "https://i.imgur.com/eD5mE7R.gif",
              "https://i.imgur.com/JCUipZJ.gif",
              "https://i.imgur.com/VSg0YLw.gif",
              "https://i.imgur.com/8mUufrm.gif"]

bitelinks = ["https://i.imgur.com/E0jIIa9.gif",
             "https://i.imgur.com/Nvkw6hN.gif",
             "https://i.imgur.com/wr7l06j.gif",
             "https://i.imgur.com/uce91VI.gif"]

bloodsucklinks = ["https://i.imgur.com/UbaeYIq.gif",
                  "https://i.imgur.com/qi83Eft.gif",
                  "https://i.imgur.com/CtwmzpG.gif",
                  "https://i.imgur.com/DAuEJ2F.gif",
                  "https://i.imgur.com/By6IGzq.gif"]

cuddlelinks = ["https://i.imgur.com/GWNWcLH.gif",
               "https://i.imgur.com/i3Eqqgz.gif",
               "https://i.imgur.com/GpFk6fE.gif",
               "https://i.imgur.com/mc3Z7wf.gif",
               "https://i.imgur.com/N5JYB5r.gif",
               "https://i.imgur.com/PGp8JYq.gif"]

highfivelinks = ["https://i.imgur.com/hjoQeOt.gif",
                 "https://i.imgur.com/9nhheqT.gif",
                 "https://i.imgur.com/yw3xMOu.gif",
                 "https://i.imgur.com/Y4g5fsT.gif",
                 "https://i.imgur.com/p6Hvx5r.gif",
                 "https://i.imgur.com/33nuO9D.gif",
                 "https://i.imgur.com/uFQnmYa.gif",
                 "https://i.imgur.com/9KG3k2n.gif",
                 "https://i.imgur.com/nHCC1ps.gif",
                 "https://i.imgur.com/aKvaNba.gif",
                 "http://i.imgur.com/hnHR29x.gif"]

pokelinks = ["https://i.imgur.com/HAAktbl.gif",
             "https://i.imgur.com/Fmd0Rsu.gif",
             "https://i.imgur.com/1rObSM3.gif",
             "https://i.imgur.com/Wo2fc94.gif",
             "https://i.imgur.com/rtTucBW.gif",
             "https://i.imgur.com/4c2mC5d.gif",
             "https://i.imgur.com/1DVD84G.gif"]

slaplinks = ["https://i.imgur.com/EAF42MG.gif",
             "https://i.imgur.com/tLTT9Q4.gif",
             "https://i.imgur.com/tEWjg7v.gif",
             "https://i.imgur.com/MlkLTjv.gif",
             "https://i.imgur.com/hoTYJZP.gif",
             "https://i.imgur.com/Pthhs3Y.gif"]


punchlinks = ["https://i.imgur.com/T2HdIv8.gif",
              "https://i.imgur.com/LZz65rg.gif",
              "https://i.imgur.com/FqPBIf3.gif",
              "https://i.imgur.com/KmqPDQG.gif",
              "https://i.imgur.com/yEx4aKu.gif"]

starelinks = ["https://i.imgur.com/f8rFNH0.gif",
              "https://i.imgur.com/ACCQDj4.gif",
              "https://i.imgur.com/1Co1i9t.gif",
              "https://i.imgur.com/uPZHQxV.gif",
              "https://i.imgur.com/wXQLAb3.gif",
              "https://i.imgur.com/hY7ZngK.gif"]

facepalmlinks = ["http://media.giphy.com/media/8BYLSNmnJYQxy/giphy.gif",
                 "https://uploads.disquscdn.com/images/84e9a7cef36a59ae605fad98c7ac567841be388820bf3fb936fd21b646a1d605.gif",
                 "https://media1.tenor.com/images/74199573d51d1bd9b61029b611ee7617/tenor.gif?itemid=5695432",
                 "http://i0.kym-cdn.com/photos/images/original/000/173/877/Facepalm.gif",
                 "http://i.imgur.com/gXOcRsW.gif",
                 "https://media.giphy.com/media/8cPpgUhTMjhF6/giphy.gif",
                 "https://media1.tenor.com/images/a0282083ab6b592ab419659e4fb08624/tenor.gif?itemid=4745847"]

crylinks = ["https://media1.giphy.com/media/ROF8OQvDmxytW/giphy-downsized.gif",
            "https://media1.tenor.com/images/06ae6bbe852471939cf61a81e5a9eb23/tenor.gif?itemid=5370823",
            "https://78.media.tumblr.com/e9fb46144efc579746e57bcaebd3350a/tumblr_olrmy4djBG1tydz8to1_500.gif",
            "http://i.imgur.com/k5B1CBd.jpg",
            "https://media.giphy.com/media/hyU0RHvlS3iQU/giphy.gif",
            "https://media1.tenor.com/images/5912cbe4bc0dec511b5e0996a2ad9b6f/tenor.gif?itemid=8620704",
            "https://s9.favim.com/orig/131225/an-anime-anime-gif-anime-guy-Favim.com-1182388.gif"]

leavelinks = ["https://media.giphy.com/media/lAtxSyUHnoIco/giphy.gif",
              "https://ci.memecdn.com/5650164.gif",
              "https://pa1.narvii.com/6080/c46db4cd0979e64c08698175e936bca4626acadd_hq.gif",
              "https://media1.tenor.com/images/5d4a1f882108251c15d7725060704226/tenor.gif?itemid=4674589",
              "https://myanimelist.cdn-dena.com/s/common/uploaded_files/1460140429-d60a2b5a534becb71153db8eaaaf4e14.gif",
              "https://myanimelist.cdn-dena.com/s/common/uploaded_files/1460139914-f1109b66f45c29d770e26da53e875508.gif",
              "http://i0.kym-cdn.com/photos/images/original/001/081/817/909.gif",
              "https://myanimelist.cdn-dena.com/s/common/uploaded_files/1460140490-8b365d32a26712058adf10436dce0389.gif",
              "https://media1.tenor.com/images/151a5c1d0f8434a1d42fbcecfed3e332/tenor.gif?itemid=9362305"]

hacklinks = ["https://i.imgur.com/9eoPhC0.gif",
             "https://i.imgur.com/43cI6Fe.gif",
             "https://vignette.wikia.nocookie.net/vsbattles/images/5/58/Hacking.gif/revision/latest?cb=20150210152035",
             "https://i.imgur.com/uG8Kwlv.gif",
             "https://media2.giphy.com/media/ohONS2y8GTDoI/giphy.gif"]

suicidelinks = ["https://i.imgur.com/wgOudvL.gif",
                "https://i.imgur.com/rYVvGjd.gif",
                "https://i.imgur.com/rxKk3Mw.gif",
                "https://i.imgur.com/CyuEKD9.gif",
                "https://i.imgur.com/f7xjGP6.gif",
                "https://i.imgur.com/y6wW8zc.gif",
                "https://i.imgur.com/EwzhaIu.gif"]

languages = ["af", "sq", "ar", "hy", "bn", "ca", "zh", "zh-cn",
             "zh-tw", "zh-yue", "hr", "cs", "da", "nl", "en", "en-au",
             "en-us", "en-uk", "eo", "fi", "fr", "de", "el", "hi",
             "hu", "is", "id", "it", "ja", "km", "ko", "la",
             "lv", "mk", "no", "pl", "pt", "ro", "ru", "sr",
             "si", "sk", "es", "es-es", "es-us", "sw", "sv", "ta",
             "th", "tr", "uk", "vi", "cy"]

dis_roles = ["Demons (Administrators)",
             "Nightmares (Managers)",
             "Dark Lords (Owners)",
             "DARKNESS",
             "BOTS",
             "Corrupted Souls (BOTs)",
             "Zero's Property",
             "Bunny's Property"]

panlinks = ["https://i.imgur.com/DPBafqb.gif",
            "https://i.imgur.com/iXryDZy.gif",
            "https://i.imgur.com/49h6CKN.gif",
            "https://i.imgur.com/EQ4G9Ig.gif",
            "https://i.imgur.com/t8FGb8R.gif",
            "https://i.imgur.com/T8rUe4N.gif",
            "https://i.imgur.com/ABpc6pn.gif",
            "https://i.imgur.com/f9XLuyn.gif"]

games = ["with the other me...", "with monsters in the dark...", "with monsters like me...",
         "with lies and liars...", "chess with the devil...", "with your soul...",
         "with your dreams...", "with your worst nightmares...", "with your fears...",
         "with your thoughts...", "with someone special...", "chess with death...",
         "with the lost ones...", "with the ones that left...", "with the missing one...",
         "in hell...", "with my blood...", "with my mind...",
         "with your mind...", "with my thoughts...", "with my feelings...",
         "with your feelings...", "with your emotions...", "with my emotions...",
         "with blood and chains...", "with chains...", "with my cuts...",
         "with the forgotten ones...", "with the forgotten one...", "with razors...",
         "with lost souls...", "with space and time...", "with fake friends...",
         "with shadows...", "with your masks...", "with my mask...",
         "}help"]

hackergame_types = ["ddos", "virus", "claim", "nuke", "raid"]

# EVENT - TELLS YOU WHEN THE BOT TURNS ON
@client.event
async def on_ready():
    t1 = time.perf_counter()
    print("============================================================")
    print("D A R K N E S S has arrived!")
    print("============================================================")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    print("============================================================")
    await client.change_presence(game=discord.Game(name='}help'))
    await client.wait_until_ready()
    t2 = time.perf_counter()
    print("Ping: {}".format(round((t2-t1)*1000)))
    print("============================================================")

# AUTO CHANGING GAME STATUS
async def gamechanger():
    await client.wait_until_ready()
    while not client.is_closed:
        game = random.choice(games)
        await client.change_presence(game=discord.Game(name=game))
        await asyncio.sleep(60)
    
client.loop.create_task(gamechanger())

# EVENT - JOIN / LEAVE
@client.async_event
async def on_member_join(userName: discord.User):
    joins = ["`{}` joined the game!".format(userName),
             "`{}`, we've been expecting you...".format(userName),
             "`{}`, hey! We hope you brought pizza!".format(userName),
             "`{}`, welcome!".format(userName),
             "`{}` is here! Everyone, look busy!".format(userName),
             "It's dangerous to go alone, take `{}` with you!".format(userName),
             "Shut up! `{}` is here!".format(userName),
             "A wild `{}` has appeared!".format(userName),
             "`{}` has been summoned!".format(userName),
             "Everyone, gather around. `{}` came to visit us!".format(userName),
             "`{}` has joined your party!".format(userName),
             "`{}` has spawned!".format(userName),
             "Holy shit! `{}` is here!".format(userName),
             "Roses are red, violets are blue, `{}` joined the server, you should invite your friends too!".format(userName),
             "`{}` just slid into the server!".format(userName),
             "`{}` is ready and waiting!".format(userName),
             "Achievement earned: Find `{}`.".format(userName),
             "`{}` joined your team! Can I get a heal?".format(userName),
             "`{}` is here! Leave your weapons by the door.".format(userName),
             "Brace yourselves, here comes `{}`!".format(userName),
             "`{}` joined the server! Seems OP - please nerf.".format(userName),
             "Hey, `{}`! About time you joined.".format(userName),
             "Welcome `{}`. Make yourself at home.".format(userName),
             "`{}` joined! Please no hacks!".format(userName),
             "`{}` joined the server! Seems legit.".format(userName)]
    await client.send_message(client.get_channel("414092782408433684"), "{}".format(random.choice(joins)))
    print("============================================================")
    print("JOIN EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

@client.async_event
async def on_member_remove(userName: discord.User):
    leaves = ["`{}` left! Please insert a coin to continue.".format(userName),
              "We lost `{}`! Do not give up yet!".format(userName),
              "`{}` died!".format(userName),
              "`{}` left the server! Everyone, get back to work.".format(userName),
              "We will miss you, `{}`!".format(userName),
              "Achievement get: Loose `{}`!".format(userName),
              "Good luck, `{}`, you'll need it on your journey!".format(userName),
              "`{}` left the server!".format(userName),
              "Wait, where did `{}` go?".format(userName),
              "Our `{}` has been killed!".format(userName),
              "Your `{}` was destroyed!".format(userName),
              "And so `{}` went on their journey to become the wizard king!".format(userName),
              "No, `{}`! We lost them...".format(userName),
              "`{}` left the game!".format(userName),
              "`{}` left your party!".format(userName),
              "`{}` left the server! Shut up and listen.".format(userName),
              "`{}`, you will be remembered.".format(userName),
              "`{}`, wait! What about our deal?!".format(userName),
              "Damn! Not `{}` too!".format(userName),
              "`{}` left the server! Did I do something wrong?".format(userName),
              "Swoooosh, `{}` just flew away.".format(userName),
              "Hey, `{}`! Where do you- too late...".format(userName),
              "You'll be back, `{}`! I'll be waiting!".format(userName),
              "Error 404: `{}` not found!".format(userName),
              "No one really liked you anyway, `{}`... except me...".format(userName)]
    await client.send_message(client.get_channel("414092782408433684"), "{}".format(random.choice(leaves)))
    print("============================================================")
    print("LEAVE EVENT")
    print("{} ### {}".format(userName, userName.id))
    print("============================================================")

'''COMMANDS FOR EVERYONE'''
# }help
client.remove_command('help')
@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author
    embed1 = discord.Embed(colour=0x4ec0ca, description= "")
    embed2 = discord.Embed(colour=0x2100ff, description= "")
    embed3 = discord.Embed(colour=0x32325e, description= "")
    embed4 = discord.Embed(colour=0x0fb400, description= "")
    embed5 = discord.Embed(colour=0x2d77df, description= "")
    embed6 = discord.Embed(colour=0xff0000, description= "")
    embed7 = discord.Embed(colour=0x4d009e, description= "")
    embed8 = discord.Embed(colour=0x000000, description= "")

    embed1.title = "COMMANDS FOR EVERYONE"
    embed2.title = "VIP COMMANDS"
    embed3.title = "LEGEND COMMANDS"
    embed4.title = "HELPER COMMANDS"
    embed5.title = "MODERATOR COMMANDS"
    embed6.title = "ADMINISTRATOR COMMANDS"
    embed7.title = "MANAGER COMMANDS"
    embed8.title = "OWNER COMMANDS"

    embed1.set_footer(text=footer_text)
    embed2.set_footer(text=footer_text)
    embed3.set_footer(text=footer_text)
    embed4.set_footer(text=footer_text)
    embed5.set_footer(text=footer_text)
    embed6.set_footer(text=footer_text)
    embed7.set_footer(text=footer_text)
    embed8.set_footer(text=footer_text)

    embed1.add_field(name="}ping", value="`Shows your and the bot's ping! Use this to check if you or the bot is lagging!`", inline=True)
    embed1.add_field(name="}help", value="`Gives you a list of commands (this list)!`", inline=True)
    embed1.add_field(name="}calculator <math problem>", value="`Solves simple math problems!`", inline=True)
    embed1.add_field(name="}battle <user>", value="`Use this to fight the mentioned user!`", inline=True)
    embed1.add_field(name="}ship <user1> <user2>", value="`Ships the mentioned users!`", inline=True)
    embed1.add_field(name="}rps <rock/paper/scissors>", value="`Play rock, paper, scissors with the bot!`", inline=True)
    embed1.add_field(name="}nothing", value="`Does nothing! Very essential for bots!`", inline=True)
    embed1.add_field(name="}serverinfo", value="`Gives you information about the server!`", inline=True)
    embed1.add_field(name="}kill <user>", value="`Kills the mentioned user!`", inline=True)
    embed1.add_field(name="}report <user> <reason>", value="`Reports the mentioned user to the staff! Report people that are breaking the rules only!`", inline=True)
    embed1.add_field(name="}eightball <yes or no question>", value="`Asks the magic eight ball a yes or no question! This always tells the truth!`", inline=True)
    embed1.add_field(name="}roast <user>", value="`Use this to roast someone so hard that they'll start to melt!`", inline=True)
    embed1.add_field(name="}hug <user>", value="`Use this to hug the mentioned user!`", inline=True)
    embed1.add_field(name="}kiss <user>", value="`Use this to kiss the mentioned user!`", inline=True)
    embed1.add_field(name="}cuddle <user>", value="`Use this to cuddle with the mentioned user!`", inline=True)
    embed1.add_field(name="}pat <user>", value="`Use this to pat the mentioned user!`", inline=True)
    embed1.add_field(name="}nom <user>", value="`Use this to nom the mentioned user!`", inline=True)
    embed1.add_field(name="}punch <user>", value="`Punches the mentioned user!`", inline=True)
    embed1.add_field(name="}bloodsuck <user>", value="`Sucks the mentioned user's blood!`", inline=True)
    embed1.add_field(name="}bite <user>", value="`Bites the mentioned user!`", inline=True)
    embed1.add_field(name="}throw <user>", value="`Throws the mentioned user!`", inline=True)
    embed1.add_field(name="}poke <user>", value="`Use this to poke the mentioned user!`", inline=True)
    embed1.add_field(name="}highfive <user>", value="`Use this to highfive the mentioned user!`", inline=True)
    embed1.add_field(name="}stare <user>", value="`Stares at the mentioned user!`", inline=True)
    embed1.add_field(name="}slap <user>", value="`Slaps the mentioned user!`", inline=True)
    embed1.add_field(name="}facepalm", value="`Use this to facepalm!`", inline=True)
    embed1.add_field(name="}suicide", value="`Use this to kill yourself!`", inline=True)
    embed1.add_field(name="}cry", value="`Cries!`", inline=True)
    embed1.add_field(name="}hack <user>", value="`Hacks the mentioned user!`", inline=True)
    embed1.add_field(name="}leave", value="`Leaves!`", inline=True)
    embed1.add_field(name="}rate <text>", value="`Rates the specified thing!`", inline=True)
    embed1.add_field(name="}dicklength", value="`Tells how big your dick is, even if you don't have one!`", inline=True)
    embed1.add_field(name="}hackergame <number> [type]", value="`Tries to hack into the specified amount of companies. You can also add a type of hack to destroy the companies!`", inline=True)

    embed2.add_field(name="}say <text>", value="`Forces the bot to say whatever you want!`", inline=True)
    embed2.add_field(name="}tts <language> <text>", value="`Forces the bot to say something in a voice chat with the specified language!`", inline=True)
    embed2.add_field(name="}disconnect", value="`Forces the bot the leave a voice chat!`", inline=True)
    embed2.add_field(name="}fart", value="`Farts in a voice chat!`", inline=True)
    embed2.add_field(name="}earrape", value="`Plays earrape in a voice chat!`", inline=True)

    embed3.add_field(name="?", value="`No commands yet!`", inline=True)

    embed4.add_field(name="}userinfo <user>", value="`Gives you information about the mentioned user!`", inline=True)
    embed4.add_field(name="}punish <user> [reason]", value="`Punishes the mentioned user! Punished people can only see messages in channels, but can't talk!`", inline=True)
    embed4.add_field(name="}pardon <user>", value="`Revomes the punishment from the mentioned user!`", inline=True)
    embed4.add_field(name="}purge <number>", value="`Deletes the specified amount of messages in a channel!`", inline=True)
    embed4.add_field(name="}nick <user> [nickname]", value="`Changes the mentioned user's nickname to whatever you specify!`", inline=True)
    embed4.add_field(name="}warn <user> <reason>", value="`Warns the mentioned user!`", inline=True)

    embed5.add_field(name="}ban <user> [reason]", value="`Bans the mentioned user!`", inline=True)
    embed5.add_field(name="}unban <user id>", value="`Unbans the user with the specified ID!`", inline=True)
    embed5.add_field(name="}kick <user> [reason]", value="`Kicks the mentioned user!`", inline=True)

    embed6.add_field(name="}embed <title> <description> <field name> <field value> <footer>", value="`Forces the bot to create custom embeds!`", inline=True)
    embed6.add_field(name="}takerole <user> <role name>", value="`Removes a specified role from the mentioned user!`", inline=True)
    embed6.add_field(name="}giverole <user> <role name>", value="`Gives a specified role to the mentioned user!`", inline=True)
    embed6.add_field(name="}masspardon", value="`Removes punishments from all punished members on the server!`", inline=True)

    embed7.add_field(name="}rawsay <text>", value="`Forces the bot to say something, this supports formats!`", inline=True)
    embed7.add_field(name="}idban <user id>", value="`Bans a user with the matching ID as the one specified! This can ban users outside of the server!`", inline=True)

    embed8.add_field(name="}pan <user> [text]", value="`Uses the mighty pan to destroy the mentioned user!`", inline=True)

    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.add_field(name=":incoming_envelope: ", value="`A list of commands has been sent to your DMs!`")
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    await client.send_message(author, embed=embed8)
    await client.send_message(author, embed=embed7)
    await client.send_message(author, embed=embed6)
    await client.send_message(author, embed=embed5)
    await client.send_message(author, embed=embed4)
    await client.send_message(author, embed=embed3)
    await client.send_message(author, embed=embed2)
    await client.send_message(author, embed=embed1)
    print("============================================================")
    print("}help")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }ping
@client.command(pass_context=True)
async def ping(ctx):
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await client.send_typing(channel)
    t2 = time.perf_counter()
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.add_field(name=":satellite: ", value="`Yes, I am here. No need to ping me.`\n`Ping: {}ms`".format(round((t2-t1)*1000)))
    msg.set_footer(text=footer_text)
    await client.say(embed=msg)
    print("============================================================")
    print("}ping")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }calculator <math problem>
@client.command(pass_context=True)
async def calculator(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}calculator <math problem>`")
    else:
        answer = str(eval(args))
        msg.add_field(name=":fax: Calculator", value= "`Problem: {}`\n \n`Answer: {}`".format(args, answer), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}calculator <math problem>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }battle <user>
@client.command(pass_context=True)
async def battle(ctx, userName: discord.Member = None):
    attacker = random.randint(0, 301)
    attacked = random.randint(0, 301)
    attackerhealth = 300 - attacked
    attackedhealth = 300 - attacker
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}battle <user>`")
    else:
        msg.add_field(name= ":red_circle: B A T T LE :red_circle: ", value= "**~~=================================~~**\n`{}` :vs: `{}`\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n \n:arrow_forward: {}\n \n:fast_forward: {} DMG\n**~~=================================~~**\n:small_orange_diamond: `{}`\n:hearts: {} HP\n \n:small_orange_diamond: `{}`\n:hearts: {} HP\n**~~=================================~~**".format(author.display_name, userName.display_name, author.display_name, random.choice(attacks), attacker, userName.display_name, random.choice(attacks), attacked, author.display_name, attackerhealth, userName.display_name, attackedhealth), inline=True)
        if attacker == attacked:
            msg.add_field(name= ":diamonds: N O  W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n`{}`\n**~~=================================~~**".format(author.display_name, userName), inline=True)
        elif attacker > attacked:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        else:
            msg.add_field(name= ":diamonds: W I N N E R :diamonds:", value= "**~~=================================~~**\n`{}`\n**~~=================================~~**".format(userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}battle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }ship <user1> <user2>
@client.command(pass_context=True)
async def ship(ctx, userName1: discord.Member = None, userName2: discord.Member = None):
    percent = random.randint(0, 101)
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName1 == None or userName2 == None:
        msg.add_field(name=":octagonal_sign: ",value="`}ship <user1> <user2>`")
    else:
        if percent >= 1 and percent <= 10:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Shit\n```\n:sob: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 11 and percent <= 20:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Awful\n```\n:cry: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 21 and percent <= 30:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Really Bad\n```\n:frowning2: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 31 and percent <= 40:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Bad\n```\n:slight_frown: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 41 and percent <= 50:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Okay\n```\n:neutral_face: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 51 and percent <= 60:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Good\n```\n:slight_smile: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 61 and percent <= 70:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Very Good\n```\n:smiley: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 71 and percent <= 80:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Fantastic\n```\n:blush: ".format(userName1.display_name, userName2.display_name, percent))
        elif percent >= 81 and percent <= 90:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Amazing\n```\n:heart_eyes: ".format(userName1.display_name, userName2.display_name, percent))
        else:
            msg.add_field(name=":heartpulse: S H I P  M A C H I N E :heartpulse: ", value=":small_red_triangle_down: **{}**\n:small_red_triangle: **{}**\n```fix\n{} Perfect\n```\n:revolving_hearts: ".format(userName1.display_name, userName2.display_name, percent))
    await client.say(embed=msg)
    print("============================================================")
    print("}ship <user1> <user2>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
        
# }rps <rock/paper/scissors>
@client.command(pass_context=True)
async def rps(ctx, args=None):
    choice = random.choice(choices)
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}rps <rock/paper/scissors>`")
    elif args == "rock" or args == "paper" or args == "scissors":
        msg.add_field(name=":fist: :raised_hand: :v: ROCK PAPER SCISSORS :v: :raised_hand: :fist: ", value="**~~=================================~~**\n:arrow_forward: `{}`: {}\n:arrow_forward: `BOT`: {}\n**~~=================================~~**".format(author.display_name, args, choice), inline=True)
        if args == "rock" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "paper" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "scissors" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`{}`\n**~~=================================~~**".format(author.display_name), inline=True)
        elif args == "rock" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "scissors":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "scissors" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="`BOT`\n**~~=================================~~**", inline=True)
        elif args == "rock" and choice == "rock":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        elif args == "paper" and choice == "paper":
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
        else:
            msg.add_field(name=":diamonds: W I N N E R :diamonds: ", value="It's a tie!\n**~~=================================~~**", inline=True)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`}rps <rock/paper/scissors>`")
    await client.say(embed=msg)
    print("============================================================")
    print("}rps <rock/paper/scissors>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }serverinfo
@client.command(pass_context=True)
async def serverinfo(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ":page_with_curl: SERVER INFORMATION"
    msg.set_footer(text=footer_text)
    msg.add_field(name="MEMBERS", value=(len(ctx.message.server.members)), inline=True)
    msg.add_field(name="CHANNELS", value=(len(ctx.message.server.channels)), inline=True)
    msg.add_field(name="EMOJIS", value=(len(ctx.message.server.emojis)), inline=True)
    msg.add_field(name="ID", value=(ctx.message.server.id), inline=True)
    msg.add_field(name="REGION", value=(ctx.message.server.region), inline=True)
    msg.add_field(name="ROLES", value=(len(ctx.message.server.roles)), inline=True)
    msg.add_field(name="OWNER", value=(ctx.message.server.owner), inline=True)
    msg.add_field(name="CREATED AT", value=(ctx.message.server.created_at), inline=True)
    msg.add_field(name="RELEASE DATE:", value="9th of March 2018", inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}serverinfo")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }kill <user>
@client.command(pass_context=True)
async def kill(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}kill <user>`")
    else:
        msg.add_field(name=":newspaper: NEWS", value="`{} killed {} by {}`".format(author.display_name, userName.display_name, random.choice(killmsgs)))
    await client.say(embed=msg)
    print("============================================================")
    print("}kill <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }nothing
@client.command(pass_context=True)
async def nothing(ctx):
    author = ctx.message.author
    await client.say("` `")
    print("============================================================")
    print("}nothing")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }report <user> <reason>
@client.command(pass_context=True)
async def report(ctx, userName: discord.Member = None, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg2 = discord.Embed(colour=0x210150, description= "")
    msg2.title = ""
    msg2.set_footer(text=footer_text)
    if userName == None or args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}report <user> <reason>`")
    else:
        msg.add_field(name=":clipboard: REPORT", value="`{} has reported {}!`".format(author.display_name, userName.display_name))
        msg2.add_field(name=":clipboard: REPORT", value="`Reporter:`\n`{} ### {}`\n`Reported:`\n`{} ### {}`\n`Reason:`\n`{}`".format(author, author.id, userName, userName.id, args))
        channel = client.get_channel('414094893946765313')
        await client.send_message(channel, embed=msg2)
    await client.say(embed=msg)
    print("============================================================")
    print("}report <user> <reason>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
        
# }eightball <yes or no question>
@client.command(pass_context=True)
async def eightball(ctx, *, args=None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}eightball <yes or no question>`")
    else:
        msg.add_field(name="Magic Eight Ball", value=":grey_question: **Question:**\n`{}`\n \n:8ball: **Answer:**\n`{}`".format(args, random.choice(eightballmsgs)))
    await client.say(embed=msg)
    print("============================================================")
    print("}eightball <yes or no question>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }roast <user>
@client.command(pass_context=True)
async def roast(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}roast <user>`")
    else:
        msg.add_field(name=":fire: Roast Machine", value="`{}, {}`".format(userName.display_name, random.choice(roasts)))
    await client.say(embed=msg)
    print("============================================================")
    print("}roast <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
        
# }hug <user>
@client.command(pass_context=True)
async def hug(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}hug <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(huglinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got a hug from {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hug <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }kiss <user>
@client.command(pass_context=True)
async def kiss(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}kiss <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(kisslinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got kissed by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}kiss <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }cuddle <user>
@client.command(pass_context=True)
async def cuddle(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}cuddle <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(cuddlelinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got a cuddle from {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cuddle <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }pat <user>
@client.command(pass_context=True)
async def pat(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}pat <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(patlinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got a pat from {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}pat <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }punch <user>
@client.command(pass_context=True)
async def punch(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}punch <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(punchlinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got punched by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}punched <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }nom <user>
@client.command(pass_context=True)
async def nom(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}nom <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(nomlinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, {} nommed you! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}nom <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }bite <user>
@client.command(pass_context=True)
async def bite(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}bite <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(bitelinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got bitten by{}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}bite <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }bloodsuck <user>
@client.command(pass_context=True)
async def bloodsuck(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}bloodsuck <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(bloodsucklinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, {} is sucking your blood! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}bloodsuck <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }highfive <user>
@client.command(pass_context=True)
async def highfive(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}highfive <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(highfivelinks)))
        msg.add_field(name=":handshake: Interactions", value="`{} highfived {}! :3`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}highfive <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }poke <user>
@client.command(pass_context=True)
async def poke(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}poke <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(pokelinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got poked by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}poke <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }slap <user>
@client.command(pass_context=True)
async def slap(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}slap <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(slaplinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got slapped by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}slap <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }stare <user>
@client.command(pass_context=True)
async def stare(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}stare <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(starelinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, {} is staring at you! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}stare <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }hack <user>
@client.command(pass_context=True)
async def hack(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}hack <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(hacklinks)))
        msg.add_field(name=":handshake: Interactions", value="`{}, you got hacked by {}! :3`".format(userName.display_name, author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}hack <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }throw <user>
@client.command(pass_context=True)
async def throw(ctx, userName: discord.Member = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if userName == None:
        msg.add_field(name=":octagonal_sign: ", value="`}throw <user>`")
    else:
        msg.set_image(url="{}".format(random.choice(throwlinks)))
        msg.add_field(name=":handshake: Interactions", value="`{} threw {}!`".format(author.display_name, userName.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}throw <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }cry
@client.command(pass_context=True)
async def cry(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(crylinks)))
    msg.add_field(name=":handshake: Interactions", value="`{} is crying! 3:`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}cry")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }leave
@client.command(pass_context=True)
async def leave(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(leavelinks)))
    msg.add_field(name=":handshake: Interactions", value="`{} left the chat! 3:`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}leave")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }facepalm
@client.command(pass_context=True)
async def facepalm(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(facepalmlinks)))
    msg.add_field(name=":handshake: Interactions", value="`{} facepalmed!`".format(author.display_name), inline=True)
    await client.say(embed=msg)
    print("============================================================")
    print("}facepalm")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }suicide
@client.command(pass_context=True)
async def suicide(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    msg.set_image(url="{}".format(random.choice(suicidelinks)))
    msg.add_field(name=":newspaper: NEWS", value="`{} {}`".format(author.display_name, random.choice(suicidemsgs)))
    await client.say(embed=msg)
    print("============================================================")
    print("}suicide")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }rate <text>
@client.command(pass_context=True)
async def rate(ctx, *, args = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}rate <text>`")
    else:
        msg.add_field(name=":scales:", value="`I'd rate {} a {}/10`".format(args, random.randint(0, 11)))
    await client.say(embed=msg)
    print("============================================================")
    print("}rate <text>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }dicklength
@client.command(pass_context=True)
async def dicklength(ctx):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    choice = random.randint(0, 10)
    if choice == 0 or choice == 1:
        msg.add_field(name=":straight_ruler: ", value="`I'm sorry, {}, you currently do not have a dick.`".format(author.display_name))
    elif choice == 9 or choice == 10:
        msg.add_field(name=":straight_ruler: ", value="`Error! Currently {}'s dick is too big for me to take the length of it.`".format(author.display_name))
    else:
        msg.add_field(name=":straight_ruler: ", value="`Currently, {}'s dick is {}cm long.`".format(author.display_name, random.randint(1, 101)))
    await client.say(embed=msg)
    print("============================================================")
    print("}dicklength")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
           
# }hackergame <number> [type]
@client.command(pass_context=True)
async def hackergame(ctx, args: int = None, args2 = None):
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    chance = random.randint(0, 100)
    if args == None:
        msg.add_field(name=":octagonal_sign: ", value="`}hackergame <number> [type]`")
    else:
        earned = random.randint(1, 10000)
        hacked = random.randint(1, args)
        destroyed = random.randint(1, hacked)
        if args > 10000 and args >= 1:
            msg.add_field(name=":octagonal_sign: ", value="`Please enter a number between 1 and 10000!`")
        elif args2 == None:
            if chance <= 60:
                msg.add_field(name=":computer: ", value="```diff\n--- {} tried hacking into {} companies.\n \n- They have been cought!\n \n+ Failed to hack: {}\n \n! Money lost: {}$\n```".format(author.display_name, args, hacked, earned))
            else:
                msg.add_field(name=":computer: ", value="```diff\n--- {} tried hacking into {} companies.\n \n+ Successfully hacked: {}\n \n! Money earned: {}$\n```".format(author.display_name, args, hacked, earned))
        elif args2 not in hackergame_types:
            msg.add_field(name=":octagonal_sign: ", value="`Types of hacks you can use:`\n`{}`".format(hackergame_types))
        else:
            if chance <= 60:
                msg.add_field(name=":computer: ", value="```diff\n--- {} tried hacking into {} companies using {}.\n \n- They have been cought!\n \n+ Failed to hack: {}\n \n! Money lost: {}$\n \n \n-Companies destroyed: {}\n```".format(author.display_name, args, args2, hacked, earned, destroyed))
            else:
                msg.add_field(name=":computer: ", value="```diff\n--- {} tried hacking into {} companies using {}.\n \n+ Successfully hacked: {}\n \n! Money earned: {}$\n \n \n-Companies destroyed: {}\n```".format(author.display_name, args, args2, hacked, earned, destroyed))
    await client.say(embed=msg)
    print("============================================================")
    print("}hackergame <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

'''VIP COMMANDS'''
# }say <text>
@client.command(pass_context=True)
async def say(ctx, *, args=None):
    vip_role = discord.utils.get(ctx.message.server.roles, name='Night Crawlers (VIPs)')
    legend_role = discord.utils.get(ctx.message.server.roles, name='Eclipsors (Legends)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip_role in author.roles or legend_role in author.roles:
        if args == None:
            msg.add_field(name=":octagonal_sign: ", value="`}say <text>`")
            await client.say(embed=msg)
        else:
            await client.say("`{}`".format(args))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by VIPs and Legends!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}say <text>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }tts <language> <text>
@client.command(pass_context=True)
async def tts(ctx, lc=None, *, args=None):
    vip_role = discord.utils.get(ctx.message.server.roles, name='Night Crawlers (VIPs)')
    legend_role = discord.utils.get(ctx.message.server.roles, name='Eclipsors (Legends)')
    author = ctx.message.author
    voice_channel = author.voice_channel
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip_role in author.roles or legend_role in author.roles:
        if lc == None or args == None:
            msg.add_field(name= ":octagonal_sign: ", value= "`}tts <languages> <text>`")
            await client.say(embed=msg)
            print("============================================================")
            print("}tts <language> <text>")
            print("{} ### {}".format(author, author.id))
            print("============================================================")
        elif author.voice_channel == None:
            msg.add_field(name= ":octagonal_sign: ", value= "`You have to be in a voice channel to use this command!`")
            await client.say(embed=msg)
            print("============================================================")
            print("}tts <language> <text>")
            print("{} ### {}".format(author, author.id))
            print("============================================================")
        elif lc not in languages:
            msg.add_field(name= ":octagonal_sign: ", value= "`Language not found!`\n`Languages:`\n`{}`".format(languages))
            await client.say(embed=msg)
            print("============================================================")
            print("}tts <language> <text>")
            print("{} ### {}".format(author, author.id))
            print("============================================================")
        else:
            if client.is_voice_connected(ctx.message.server) == True:
                msg.add_field(name= ":octagonal_sign: ", value= "`You have to wait for me to leave the voice channel to use this again!`")
                await client.say(embed=msg)
                print("============================================================")
                print("}tts <language> <text>")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
            else:
                voice = await client.join_voice_channel(voice_channel)
                tts = gTTS(text=args, lang=lc)
                tts.save("tts.mp3")

                player = voice.create_ffmpeg_player('tts.mp3')
                player.start()
                msg.add_field(name= ":loudspeaker: TTS", value= "`{}: {}`\n`by {}`".format(lc, args, author.display_name))
                await client.say(embed=msg)
                print("============================================================")
                print("}tts <language> <text>")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
                letters = len(args)
                time = letters / 3
                await asyncio.sleep(float(time))
                for x in client.voice_clients:
                    if(x.server == ctx.message.server):
                        return await x.disconnect()
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by VIPs and Legends!`")
        await client.say(embed=msg)
        print("============================================================")
        print("}tts <language> <text>")
        print("{} ### {}".format(author, author.id))
        print("============================================================")
        
# }disconnect
@client.command(pass_context=True)
async def disconnect(ctx):
    vip_role = discord.utils.get(ctx.message.server.roles, name='Night Crawlers (VIPs)')
    legend_role = discord.utils.get(ctx.message.server.roles, name='Eclipsors (Legends)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip_role in author.roles or legend_role in author.roles:
        if client.is_voice_connected(ctx.message.server) == True:
            msg.add_field(name=":mute: ", value="`Leaving the voice channel...`")
            await client.say(embed=msg)
            for x in client.voice_clients:
                if(x.server == ctx.message.server):
                    return await x.disconnect()
        else:
            msg.add_field(name=":octagonal_sign: ", value="`I'm not in a voice channel! What are you on about?`")
            await client.say(embed=msg)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by VIPs and Legends!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}disconnect")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }fart
@client.command(pass_context=True)
async def fart(ctx):
    vip_role = discord.utils.get(ctx.message.server.roles, name='Night Crawlers (VIPs)')
    legend_role = discord.utils.get(ctx.message.server.roles, name='Eclipsors (Legends)')
    author = ctx.message.author
    voice_channel = author.voice_channel
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip_role in author.roles or legend_role in author.roles:
        if author.voice_channel == None:
            msg.add_field(name=":octagonal_sign: ", value="`You have to be in a voice channel to use this command!`")
            await client.say(embed=msg)
            print("============================================================")
            print("}fart")
            print("{} ### {}".format(author, author.id))
            print("============================================================")
        else:
            if client.is_voice_connected(ctx.message.server) == True:
                msg.add_field(name= ":octagonal_sign: ", value= "`You have to wait for me to leave the voice channel to use this again!`")
                await client.say(embed=msg)
                print("============================================================")
                print("}fart")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
            else:
                voice = await client.join_voice_channel(voice_channel)
                player = voice.create_ffmpeg_player('fart.mp3')
                player.start()
                msg.add_field(name= ":poop: ", value= "`Woops ¯\_(ツ)_/¯`")
                await client.say(embed=msg)
                print("============================================================")
                print("}fart")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
                await asyncio.sleep(float(2))
                for x in client.voice_clients:
                    if(x.server == ctx.message.server):
                        return await x.disconnect()
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by VIPs and Legends!`")
        await client.say(embed=msg)
        print("============================================================")
        print("}fart")
        print("{} ### {}".format(author, author.id))
        print("============================================================")
        
# }earrape
@client.command(pass_context=True)
async def earrape(ctx):
    vip_role = discord.utils.get(ctx.message.server.roles, name='Night Crawlers (VIPs)')
    legend_role = discord.utils.get(ctx.message.server.roles, name='Eclipsors (Legends)')
    author = ctx.message.author
    voice_channel = author.voice_channel
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if vip_role in author.roles or legend_role in author.roles:
        if author.voice_channel == None:
            msg.add_field(name=":octagonal_sign: ", value="`You have to be in a voice channel to use this command!`")
            await client.say(embed=msg)
            print("============================================================")
            print("}earrape")
            print("{} ### {}".format(author, author.id))
            print("============================================================")
        else:
            if client.is_voice_connected(ctx.message.server) == True:
                msg.add_field(name= ":octagonal_sign: ", value= "`You have to wait for me to leave the voice channel to use this again!`")
                await client.say(embed=msg)
                print("============================================================")
                print("}earrape")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
            else:
                voice = await client.join_voice_channel(voice_channel)
                player = voice.create_ffmpeg_player('earrape.mp3')
                player.start()
                msg.add_field(name= ":mega: ", value= "`ᕕ(ツ)ᕗ`")
                await client.say(embed=msg)
                print("============================================================")
                print("}earrape")
                print("{} ### {}".format(author, author.id))
                print("============================================================")
                await asyncio.sleep(float(60))
                for x in client.voice_clients:
                    if(x.server == ctx.message.server):
                        return await x.disconnect()
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by VIPs and Legends!`")
        await client.say(embed=msg)
        print("============================================================")
        print("}earrape")
        print("{} ### {}".format(author, author.id))
        print("============================================================")

'''LEGEND COMMANDS'''
#

'''HELPER COMMANDS'''
# }warn <user> <reason>
@client.command(pass_context=True)
async def warn(ctx, userName: discord.Member = None, *, args = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Shadows (Punished)')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":octagonal_sign: ", value="`}warn <user> <reason>`")
            await client.say(embed=msg)
        else:
            if helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
                msg.add_field(name=":octagonal_sign: ", value="`You cannot warn other staff!`")
                await client.say(embed=msg)
            else:
                await client.add_roles(userName, punished_role)
                msg.add_field(name=":pencil: ", value="`{} warned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
                await client.say(embed=msg)
                await asyncio.sleep(float(7))
                await client.remove_roles(userName, punished_role)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}warn <user> <reason>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
           
# }punish <user> [reason]
@client.command(pass_context=True)
async def punish(ctx, userName: discord.Member = None, *, args = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Shadows (Punished)')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}punish <user> [reason]`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":octagonal_sign: ", value="`You can't punish other staff!`")
        elif args == None:
            await client.add_roles(userName, punished_role)
            msg.add_field(name=":no_entry_sign: ", value="`{} has been punished by {}!`\n`Reason: ?`".format(userName.display_name, author.display_name))
        else:
            await client.add_roles(userName, punished_role)
            msg.add_field(name=":no_entry_sign: ", value="`{} has been punished by {}!`\n`Reason: {}`".format(userName.display_name, author.display_name, args))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}punish <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }pardon <user>
@client.command(pass_context=True)
async def pardon(ctx, userName: discord.Member = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Shadows (Punished)')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}pardon <user>`")
        elif punished_role in userName.roles:
            await client.remove_roles(userName, punished_role)
            msg.add_field(name=":o: ", value="`{} removed the punishment from {}!`".format(author.display_name, userName.display_name))
        else:
            msg.add_field(name=":octagonal_sign: ", value="`{} is not punished!`".format(userName.display_name))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}pardon <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }purge <number>
@client.command(pass_context=True)
async def purge(ctx, number: int = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if number == None:
            msg.add_field(name=":octagonal_sign: ", value="`}purge <number>`")
        else:
            deleted = await client.purge_from(ctx.message.channel, limit=number)
            if len(deleted) < number:
                msg.add_field(name=":wastebasket: ", value="`{} tried to delete {} messages!`\n`Deleted {} message(s)!`".format(author.display_name, number, len(deleted)))
            else:
                msg.add_field(name=":wastebasket: ", value="`{} deleted {} message(s)!`".format(author.display_name, len(deleted)))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}purge <number>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }userinfo <user>
@client.command(pass_context=True)
async def userinfo(ctx, userName: discord.Member = None):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Shadows (Punished)')
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.title = ""
            msg.add_field(name=":octagonal_sign: ", value="}userinfo <user>")
        else:
            imageurl = userName.avatar_url
            msg.title = ":page_with_curl: USER INFORMATION"
            msg.set_thumbnail(url=imageurl)
            msg.add_field(name="NAME:", value=(userName), inline=True)
            msg.add_field(name="ID:", value=(userName.id), inline=True)
            msg.add_field(name="CREATED AT:", value=(userName.created_at), inline=True)
            msg.add_field(name="JOINED AT:", value=(userName.joined_at), inline=True)
            msg.add_field(name="STATUS:", value=(userName.status), inline=True)
            msg.add_field(name="IS BOT:", value=(userName.bot), inline=True)
            msg.add_field(name="GAME:", value="Playing {}".format(userName.game), inline=True)
            msg.add_field(name="NICKNAME:", value=(userName.nick), inline=True)
            msg.add_field(name="TOP ROLE:", value=(userName.top_role), inline=True)
            msg.add_field(name="VOICE CHANNEL:", value=(userName.voice_channel), inline=True)
            if punished_role in userName.roles:
                msg.add_field(name="PUNISHED:", value="True", inline=True)
            else:
                msg.add_field(name="PUNISHED:", value="False", inline=True)
    else:
        msg.title = ""
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}userinfo <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }nick <user> [nickname]
@client.command(pass_context=True)
async def nick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if helper_role in author.roles or mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}nick <user> [nickname]`")
        elif args == None:
            nickname = args
            await client.change_nickname(userName, nickname)
            msg.add_field(name=":label: ", value="`{} removed {}'s nickname`".format(author.display_name, userName.display_name))
        else:
            nickname = args
            msg.add_field(name=":label: ", value="`{} changed {}'s nickname to {}!`".format(author.display_name, userName.display_name, args))
            await client.change_nickname(userName, nickname)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by staff!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}nick <user> <nickname>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

'''MOD COMMANDS'''
# }ban <user> [reason]
@client.command(pass_context=True)
async def ban(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}ban <user> [reason]`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":octagonal_sign: ", value="`You can't ban other staff!`")
        elif args == None:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.ban(userName)
        else:
            msg.add_field(name=":hammer: Ban Hammer", value="`{} banned {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.ban(userName)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Moderators, Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}ban <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }kick <user> [reason]
@client.command(pass_context=True)
async def kick(ctx, userName: discord.Member = None, *, args = None):
    helper_role = discord.utils.get(ctx.message.server.roles, name='Fallen Angels (Helpers)')
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}kick <user> [reason]`")
        elif helper_role in userName.roles or mod_role in userName.roles or admin_role in userName.roles or manager_role in userName.roles or owner_role in userName.roles:
            msg.add_field(name=":octagonal_sign: ", value="`You can't kick other staff!`")
        elif args == None:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: ?`".format(author.display_name, userName.display_name))
            await client.kick(userName)
        else:
            msg.add_field(name=":boot: Kicker", value="`{} kicked {}!`\n`Reason: {}`".format(author.display_name, userName.display_name, args))
            await client.kick(userName)
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Moderators, Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}kick <user> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }unban <user id>
@client.command(pass_context=True)
async def unban(ctx, userID = None):
    mod_role = discord.utils.get(ctx.message.server.roles, name='Shades (Moderators)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if mod_role in author.roles or admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":octagonal_sign: ", value="`}unban <user id>`")
        else:
            banned_users = await client.get_bans(ctx.message.server)
            user = discord.utils.get(banned_users,id=userID)
            if user is not None:
                await client.unban(ctx.message.server, user)
                msg.add_field(name=":tools: ", value="`{} unbanned the user with the following ID: {}!`".format(author.display_name, userID))
            else:
                msg.add_field(name=":octagonal_sign: ", value="`The ID you specified is not banned! ID: {}`".format(userID))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Moderators, Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}unban <user>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

'''ADMIN COMMANDS'''
# }masspardon
@client.command(pass_context=True)
async def masspardon(ctx):
    punished_role = discord.utils.get(ctx.message.server.roles, name='Shadows (Punished)')
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        for member in ctx.message.server.members:
            if punished_role in member.roles:
                await client.remove_roles(member, punished_role)
            else:
                print(".")
        msg.add_field(name=":cloud_tornado: ", value="`I have pardoned all punished users on the server!`")
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}masspardon")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
           
# }embed <title> <description> <field name> <field value> <footer>
@client.command(pass_context=True)
async def embed(ctx, title = None, desc = None, name = None, value = None, footer = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if title == None or desc == None or name == None or value == None or footer == None:
            msg = discord.Embed(colour=0x210150, description= "")
            msg.title = ""
            msg.set_footer(text=footer_text)
            msg.add_field(name=":octagonal_sign: ", value="`}embed <title> <description> <field name> <field value> <footer>`")
        else:
            msg = discord.Embed(colour=0x210150, description= "{}".format(desc))
            msg.title = "{}".format(title)
            msg.set_footer(text="{}".format(footer))
            msg.add_field(name="{}".format(name), value="{}".format(value))
    else:
        msg = discord.Embed(colour=0x210150, description= "")
        msg.title = ""
        msg.set_footer(text=footer_text)
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}embed <title> <description> <field name> <field value> <footer>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }takerole <user> <role name>
@client.command(pass_context=True)
async def takerole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":octagonal_sign: ", value="`}takerole <user> <role name>`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":octagonal_sign: ", value="`The specified role has not been found!`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":octagonal_sign: ", value="`You cannot remove a role that is the same or higher than your top role!`")
            else:
                await client.remove_roles(userName, rolename2)
                msg.add_field(name=":outbox_tray: ", value="`{} removed {} from {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}takerole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }giverole <user> <role name>
@client.command(pass_context=True)
async def giverole(ctx, userName: discord.Member = None, *, args = None):
    admin_role = discord.utils.get(ctx.message.server.roles, name='Demons (Administrators)')
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    serverroles = [ctx.message.server.roles]
    if admin_role in author.roles or manager_role in author.roles or owner_role in author.roles:
        if userName == None or args == None:
            msg.add_field(name=":octagonal_sign: ", value="`}giverole <user> <role name>`")
        else:
            rolename2 = discord.utils.get(ctx.message.server.roles, name='{}'.format(args))
            if rolename2 == None:
                msg.add_field(name=":octagonal_sign: ", value="`The specified role has not been found!`")
            elif author.top_role == rolename2 or author.top_role < rolename2:
                msg.add_field(name=":octagonal_sign: ", value="`You cannot give a role that is the same or higher than your top role!`")
            else:
                await client.add_roles(userName, rolename2)
                msg.add_field(name=":inbox_tray: ", value="`{} gave {} to {}!`".format(author.display_name, args, userName.display_name))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Administrators, Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}giverole <user> <role name>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

'''MANAGER COMMANDS'''
# }rawsay <text>
@client.command(pass_context=True)
async def rawsay(ctx, *, args = None):
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if manager_role in author.roles or owner_role in author.roles:
        if args == None:
            msg.add_field(name=":octagonal_sign: ", value="`}rawsay <text>`")
            await client.say(embed=msg)
        else:
            await client.say("{}".format(args))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Managers and Owners!`")
        await client.say(embed=msg)
    print("============================================================")
    print("}rawsay <text>")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

# }idban <user id> [reason]
@client.command(pass_context=True)
async def idban(ctx, userID: int = None, *, args = None):
    manager_role = discord.utils.get(ctx.message.server.roles, name='Nightmares (Managers)')
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    guild = ctx.message.server
    user = guild.get_member(userID)
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if manager_role in author.roles or owner_role in author.roles:
        if userID == None:
            msg.add_field(name=":octagonal_sign: ", value="`}idban <user id> [reason]`")
        elif user == None and args is not None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: {}`".format(author.display_name, userID, args))
            await client.http.ban(userID, guild.id, 0)
        elif user == None and args == None:
            msg.add_field(name=":tools: ", value="`{} ID-Banned the following ID: {}!`\n`Reason: ?`".format(author.display_name, userID))
            await client.http.ban(userID, guild.id, 0)
        else:
            msg.add_field(name=":octagonal_sign: ", value="`Unknown error!`")
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Managers and Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}idban <user id> [reason]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")

'''OWNER COMMANDS'''
# }pan <user> [text]
@client.command(pass_context=True)
async def pan(ctx, userName: discord.Member = None, *, args = None):
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner_role in author.roles:
        if userName == None:
            msg.add_field(name=":octagonal_sign: ", value="`}pan <user> [text]`")
        elif args == None:
            msg.set_image(url="{}".format(random.choice(panlinks)))
            msg.add_field(name="P A N N E R", value="`{} got panned by {}!`".format(userName.display_name, author.display_name))
        else:
            msg.set_image(url="{}".format(random.choice(panlinks)))
            msg.add_field(name="P A N N E R", value="`{} got panned by {}!`\n`{}: {}`".format(userName.display_name, author.display_name, author.display_name, args))
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command is very dangerous, it can only be used by Owners!`")
    await client.say(embed=msg)
    print("============================================================")
    print("}pan <user> [text]")
    print("{} ### {}".format(author, author.id))
    print("============================================================")
    
# }close
@client.command(pass_context=True)
async def close(ctx):
    owner_role = discord.utils.get(ctx.message.server.roles, name='Dark Lords (Owners)')
    author = ctx.message.author
    msg = discord.Embed(colour=0x210150, description= "")
    msg.title = ""
    msg.set_footer(text=footer_text)
    if owner_role in author.roles:
        msg.add_field(name=":warning: ", value="`I will shut down in a few seconds! Closing all conections...`")
        await client.say(embed=msg)
        print("============================================================")
        print("============================================================")
        print("THE CLIENT WILL NOW CLOSE!")
        print("============================================================")
        print("============================================================")
        await asyncio.sleep(float(10))
        await client.say("`Shutting down...`")
        await client.logout()
    else:
        msg.add_field(name=":octagonal_sign: ", value="`This command can only be used by Owners!`")
        await client.say(embed=msg)
        print("============================================================")
        print("}close")
        print("{} ### {}".format(author, author.id))
        print("============================================================")

# TURNS ON THE BOT
client.run(s3)
