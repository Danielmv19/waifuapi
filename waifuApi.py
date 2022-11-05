import requests
#-----------------------------------SFW---------------------------------------
a = input(
'''waifu
neko
bully
cuddle
cry
hug
kiss
lick
pat
smug
bonk
yeet
blush
smile
wave
highfive
handhold
nom
bite
glomp
slap
kill
kick
happy
wink
poke
dance
cringe'''
)
url = "https://api.waifu.pics/sfw/{}".format(a)
r = requests.get(url)
j = r.json()
print(j)

