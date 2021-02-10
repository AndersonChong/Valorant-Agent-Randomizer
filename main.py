import discord
import os
import random

client = discord.Client()

# all valorant agents

agents = {'Brimstone': 'Controller', 'Pheonix': 'Duelist', 'Sage': 'Sentinel', 'Sova': 'Initiator', 'Viper': 'Controller', 'Cyper': 'Sentinel', 'Reyna': 'Duelist', 'Killjoy': 'Sentinel', 'Breach': 'Initiator', 'Omen': 'Controller', 'Jett': 'Duelist', 'Raze': 'Duelist', 'Skye': 'Initiator', 'Yoru': 'Duelist'}

# method for randomizing agent based on role

def search_random_agent(role):
    agents_with_role = []
    for name in agents:
        if agents[name] == role:
            agents_with_role.append(name)
    agent = random.choice(agents_with_role)
    return agent

@client.event
async def on_ready():
    print('{0.user} logged in'.format(client))

@client.event
async def on_message(message):
    # check if bot is reading its own message

    if message.author == client.user:
        return

    # show all available commands

    if message.content == ('$valo'):
        await message.channel.send('These are commands that can be used:\n```$valo-help : the user manual\n$valo-random : generate a random agent\n$valo-random-[roles] : generate a random agent based on roles```')
    
    # user manual

    if message.content == '$valo-help':
        await message.channel.send('Generate random agent:\n```$valo-random```\nGenerate random agent based on role:\n```$valo-random-duelist\n$valo-random-controller\n$valo-random-initiator\n$valo-random-sentinel```\nGenerate random agent based on role (shorthand):\n```$valo-random-d\n$valo-random-c\n$valo-random-i\n$valo-random-s```')
    
    # random agent

    if message.content == '$valo-random':
        agent = random.choice(list(agents.keys()))
        await message.channel.send(agent)

    # random agent based on role

    if message.content == '$valo-random-controller' or message.content == '$valo-random-c':
        searched_agent = search_random_agent('Controller')
        await message.channel.send(searched_agent)
    
    if message.content == '$valo-random-duelist' or message.content == '$valo-random-d':
        searched_agent = search_random_agent('Duelist')
        await message.channel.send(searched_agent)

    if message.content == '$valo-random-sentinel' or message.content == '$valo-random-s':
        searched_agent = search_random_agent('Sentinel')
        await message.channel.send(searched_agent)

    if message.content == '$valo-random-initiator' or message.content == '$valo-random-i':
        searched_agent = search_random_agent('Initiator')
        await message.channel.send(searched_agent)
        
client.run(os.getenv('TOKEN'))