import logging
from telethon import TelegramClient, events
from datetime import datetime, timedelta

# Setup logging
logging.basicConfig(level=logging.INFO)

# Fill in your API details here
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
string_session = 'YOUR_STRING_SESSION'  # If you're using a string session

# Log group ID (replace with your private log group ID)
LOG_GROUP_ID = -1001234567890

# Dictionary to store user data
user_data = {}

# Initialize Telegram client
client = TelegramClient(string_session, api_id, api_hash)


@client.on(events.NewMessage(pattern='.extract'))
async def extract_online_users(event):
    seven_days_ago = datetime.now() - timedelta(days=7)
    online_users = []

    # Get all dialogs (chats)
    async for dialog in client.iter_dialogs():
        if dialog.is_user:
            user = await client.get_entity(dialog.id)
            # Check if the user was online in the last 7 days
            if user.status and user.status.was_online and user.status.was_online >= seven_days_ago:
                online_users.append(user.id)

    # Log the online users in the log group, one message per user
    if not online_users:
        await event.reply("No users found who were online in the last 7 days.")
        return

    for user_id in online_users:
        await client.send_message(LOG_GROUP_ID, f"User ID: {user_id}")
        user_data[user_id] = user_id  # Store user data for broadcasting

    await event.reply(f"Extracted and sent data of {len(online_users)} users.")


@client.on(events.NewMessage(pattern=r'\.ebroad (\d+) (.+)'))
async def broadcast_message(event):
    # Extract number of users and the message from the command
    params = event.pattern_match.group(1, 2)
    no_of_users = int(params[0])
    message = params[1]

    # Get the user IDs stored in user_data
    user_ids = list(user_data.keys())

    # Check if there are enough users in the log
    if no_of_users > len(user_ids):
        await event.reply(f"Error: Only {len(user_ids)} users are available for broadcasting.")
        return

    # Broadcast the message to the specified number of users
    for i in range(no_of_users):
        user_id = user_ids[i]
        try:
            await client.send_message(user_id, message)
            del user_data[user_id]  # Remove user data after successful broadcast
        except Exception as e:
            logging.error(f"Failed to send message to user {user_id}: {str(e)}")

    await event.reply(f"Broadcasted the message to {no_of_users} users and deleted their data.")


# Start the Telegram client
with client:
    client.run_until_disconnected()
