import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print("Bot Aktif ! technoteori.xyz") 
    print("Developer: ☨Akşamcı#0001")
    await bot.change_presence(activity=discord.Game(name=f'{len(bot.guilds)} Sunucuda Aktif!'))


@bot.command()
async def serverping(ctx):
    await ctx.send(f'Status: {round(bot.latency * 1000)}ms')

@bot.command()
async def yardim(ctx):
    await ctx.send('!userstats !avatar !clear !mute !unmute !site !mail !serverping')

@bot.command()
async def site(ctx):
    await ctx.send('https://technoteori.xyz')
    
@bot.command()
async def mail(ctx):
    await ctx.send('tahastats@tehcnoteori.xyz')

@bot.command()
@commands.has_role("TT")
async def clear(ctx, amount = 0):
          await ctx.channel.purge(limit=amount)
        
@bot.command()
async def userstats(ctx):
    user = ctx.author
    embed=discord.Embed(title="KULLANICI BİLGİSİ", description=f"Kullanıcı Hakkında Bilgiler {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="ADI", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="SUNUCU ROL", value=user.top_role.name, inline=True)
    await ctx.send(embed=embed)

@bot.command()
async def merhaba(ctx):
    await ctx.send('Merhaba Dostum Nasılsın ?')

@bot.command()
async def yardimet(ctx):
    await ctx.send('@Yardim yardıma ihtiyacı olan bir üyen var !')
@bot.command()
async def avatar(ctx):
    user = ctx.author
    embed=discord.Embed(title="Avatar", description=f"Kullanıcı Avatarı {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)
    
@bot.command(description="Kullanıcıyı susturur.")
@commands.has_permissions(manage_messages=True)
@commands.has_role("TT")
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Cezalı!")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Cezalı!")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Susturuldu {member.mention}  {reason}")
    await member.send(f"Sunucuda susturuldun {guild.name}  {reason}")

@bot.command(description="Sustumayı kaldırır")
@commands.has_role("TT")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Susturulması kaldırıldı! {member.mention}")
    await member.send(f"Sunucuda susturulman kaldırıldı {ctx.guild.name}")
    

bot.run('OTIxNDE1Mzg3MzAyNzQ0MTE0.Ybyk8w.se9G96QGB_EOQJe4wCZ96QoA4zc')