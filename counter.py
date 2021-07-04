@client.event
async def on_message(nwordcount):
    if nwordcount.content.startswith('!nwordcount'):
        channel = nwordcount.channel
        count = 0
        async for nwordcount in channel.history(limit=500000):
            for nwordcount in re.finditer(r"\b(nigga)(s\b|\b)", nwordcount.content, re.IGNORECASE):
                count = count + 1
            else:
                await channel.send('You have said the N-Word ' + str(count) + ' time(s)')
                return
