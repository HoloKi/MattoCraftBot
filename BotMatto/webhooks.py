from discord_webhook import DiscordWebhook, DiscordEmbed

#generale
webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/711636672378306570/9z2QPwlEJ7UCg5l_UeRn9y54FxLwmNmsWRw_FNYJMp0bkY-Hrk0aMIFJcPc0HEfy-ggC')

# create embed object for webhook
embed = DiscordEmbed(title='Indovina?!', description="Nic è gay", color=1127128)

# add embed object to webhook
webhook.add_embed(embed)

response = webhook.execute()
