import os
import discord
from discord.ext import commands
"""import config"""

intents= discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("puneet_bot is ready sir!")
    await bot.tree.sync()

@bot.event
async def on_message(msg: discord.Message):
    content = msg.content
    if msg.author == bot.user:
        return

    if "puneet kaha hai".lower() in content.lower():
        await msg.reply("cheyaaaaaaaaaaaa mai yahaa hun")

    cuss_word = ["madarchod","fuck","chutiye","chutiya","mc","gandwe","rand","randi"]
    for i in cuss_word:
        if i.lower() in content.lower():
            await msg.reply(f"{i} bolega tu ab dekh tu batata hun m ab tujhe tu dekh")
            break

async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}!")

@bot.tree.command()
async def jaag_jaa_puneet(interaction: discord.Interaction):
    await interaction.response.send_message("cheyaaa kaise ho mere chaane walo")
@bot.tree.command()
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("hiii!" , ephemfckeral=True)

@bot.tree.command()
async def profile(inter: discord.Interaction):
    """Profile"""
    embed = discord.Embed(title="The Puneet Superstar's Bot", description="TOH KAISE HO MERE CHAHNE WALO?", color= 0xfa5cb8)
    embed.set_thumbnail(url = "https://i.pinimg.com/564x/85/e6/47/85e64767b129d2cae2d1c47b1ed0aece.jpg")
    await inter.response.send_message(embed=embed)

@bot.tree.command()
@commands.has_permissions(manage_messages=True)
async def clear(interaction: discord.Interaction, amount: int):
    """Clears a specified number of messages."""
    await interaction.response.defer(thinking=True,ephemeral=True)
    await interaction.channel.purge(limit=amount+1)
    await interaction.followup.send(f"Deleted {amount} messages")

@clear.error
async def on_error(interaction: discord.Integration, error: commands.CommandError):
    if isinstance(error, commands.MissingPermissions):
        await interaction.followup.send("You don't have permission to use this command!", ephemeral=True)

@bot.tree.command()
async def kick(interaction: discord.Interaction, member: discord.Member, *, reason: str):
    """Kicks a member from the server."""
    await member.kick(reason=reason)
    await interaction.followup.send(f"{member.display_name} has been kicked for {reason}")


@bot.tree.command()
async def dm(interaction: discord.Interaction, member: discord.Member, *, message: str):
    """Sends a DM to a member."""
    await member.send(message)
    await interaction.response.send_message(f"DM sent to {member.display_name}")
@bot.event
async def on_guild_channel_create(channel: discord.abc.GuildChannel):
    """Create a guid channel"""
    print("channel created")
    print(channel.name)



bot.run(os.getenv("DISCORD_TOKEN_puneet"))
