import discord
import responses
import function


async def send_message(message, user_message):
    try:
        response = responses.get_response(user_message)
        await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = "12345" # Enter your BOT TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

        custom_status = discord.Activity(type=discord.ActivityType.watching, name="ARE 100B students")
        await client.change_presence(status=discord.Status.online, activity=custom_status)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        if user_message == "\TakingDerivatives":
            await message.channel.send("Please enter the function that need to take derivative on\n")
            first_function = await client.wait_for("message", check=lambda m: m.author == message.author and m.channel == message.channel)

            derivative = function.derivative(first_function.content, "x")
            first_order_condition = function.solution(derivative, "x")


            await message.channel.send(f"The derivative is {derivative} and the value of x is {first_order_condition}"
                                      f" when setting the derivative equal to zero")

        if user_message == "\EqualFunction":
            # I want to ask the client for two math functions so I can set them equal to each other in discord
            await message.channel.send("Please enter the first math function\n")
            first_function = await client.wait_for("message", check=lambda m: m.author == message.author and m.channel == message.channel)

            await message.channel.send("Please enter the second math function\n")
            second_function = await client.wait_for("message", check=lambda
                m: m.author == message.author and m.channel == message.channel)

            result = function.systems(first_function.content, second_function.content, "x")

            await message.channel.send(f"The value of x is {result}\n")

    client.run(TOKEN)



