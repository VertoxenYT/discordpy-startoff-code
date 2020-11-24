import discord
from discord.ext import commands

#You can change the prefix into one of your own!
client = commands.Bot(command_prefix="!")
client.remove_command("help")

#Add in your bot token in this variable!
TOKEN = ""
#You can add your bot version into here!
bot_version = "v1.0"

#Please don't touch this!
@client.event
async def on_ready():
	print("----- ----- ----- ----- ----- ----- ----- ----- -----")
	print("                                                    ")
	print("            Copyright (c) 2020       ")
	print("                Vertoxen                    ")
	print("             Github page:                 ")
	print(" https://github.com/VertoxenYT?tab=repositories               ")
	print("                                                    ")
	print("----- ----- ----- ----- ----- ----- ----- ----- -----")
	
#Ping command!
@client.command()
async def ping(ctx):
#You can edit this bit!
	em = discord.Embed(title="Ping", description=f"The bot latency is ``{round(client.latency * 1000)}``ms!", color=discord.Colour.blue())
	
	em.set_footer(icon_url=f"{ctx.author.avatar_irl}", text=f"Requested by {ctx.author} | {bot_version}")
	
	await ctx.send(embed=em)
	
@client.command()
#It's better not to touch this if you don't know what's going on!
async def avatar(self, ctx, member : discord.Member = None):
	if member is None:
		em = discord.Embed(title="Error", description="You have not used the command correctly! Usage = ``!avatar (mention member)``", color=discord.Colour.red())
		
		await ctx.send(embed=em)
		
		return
		
	else:
		emb = discord.Embed(title=f"{member}'s Avatar", description=f"Here is {member}'s avatar!", color=discord.Colour.blue())
		
		emb.set_image(url=f"{ctx.member.avatar_url}")
		emb.set_footer(icon_url=f"{ctx.author.avatar_irl}", text=f"Requested by {ctx.author} | {bot_version}")
		
		await ctx.send(embed=emb)
		
@client.group(invoke_without_command=True)
async def help(ctx):
#Custom help command!
	em = discord.Embed(title="Help Menu", description=f"This is the help menu of this bot!\n\n__**Categories**__\n\n:gun: **Fun Category**\n``{command_prefix}help fun``", color=discord.Colour.blue())
	
	em.set_footer(icon_url=f"{ctx.author.avatar_irl}", text=f"Requested by {ctx.author} | {bot_version}")
	
	await ctx.send(embed=em)
	
@help.command()
async def fun(ctx):
#The addon onto the help command
	em=discord.Embed(title="Fun Menu", description=f"This is the fun category!\n\n__**Commands**__\n\n**Ping Command**\n``{command_prefix}ping``\n\n**Avatar Command**\n``{command_prefix}avatar (mention user)``")
	
	emb.set_footer(icon_url=f"{ctx.author.avatar_irl}", text=f"Requested by {ctx.author} | {bot_version}")
	
	await ctx.send(embed=em)

#DON'T TOUCH THIS! ADD YOUR TOKEN FROM THE VARIABLE!
client.run(TOKEN)