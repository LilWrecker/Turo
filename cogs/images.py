import discord
from discord.ext import commands
from utils.embeds import success_embed


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gay(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/gay?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def glass(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/glass?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def wasted(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def greyscale(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def invert(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/invert?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def invertgreyscale(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/invertgreyscale?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def brightness(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/brightness?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def threshold(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        url = f"https://some-random-api.ml/canvas/threshold?avatar={member.avatar.url}"
        em = success_embed()
        em.set_image(url=url)
        em.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Images(bot))