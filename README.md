# Telethon Userbot

This is a Telethon-based userbot that provides two key functionalities:
1. **Extract User Data**: Extracts user IDs of people who were online in the last 7 days and logs them into a private group.
2. **Broadcast Message**: Broadcasts a message to a specified number of users from the extracted data and deletes the data after broadcasting.

## Features

- **.extract**: Extracts the user IDs of all users who were online in the last 7 days and sends each user ID as a separate message to a private log group.
- **.ebroad <no_of_users> <text>**: Broadcasts the given text to the specified number of users from the extracted data, and then deletes the data of those users after broadcasting.

## Usage

### 1. Install Requirements
Ensure you have the `Telethon` library installed. You can install it using:

```bash
pip install telethon

2. Clone the Repository

git clone https://github.com/yourusername/your-repo.git
cd your-repo

3. Edit the Configuration

In the userbot.py file, update the following details:

Replace YOUR_API_ID, YOUR_API_HASH, and YOUR_STRING_SESSION with your Telegram API credentials.

Replace LOG_GROUP_ID with the ID of your private log group where user data will be sent.


4. Run the Userbot

Run the bot using:

python3 bot.py

5. Commands

.extract: Sends the user IDs of all users who were online in the last 7 days to the log group.

.ebroad <no_of_users> <text>: Broadcasts the given text to the specified number of users whose data has been logged using the .extract command. After broadcasting, the data of those users is deleted.


Example

.extract

This will log the user IDs of users who were online in the last 7 days into the log group, one message per user.

.ebroad 5 Hello, this is a broadcast message!

This will broadcast the message "Hello, this is a broadcast message!" to the first 5 users in the extracted data, then delete their information from the log.

# Hosting on Contabo

To host the userbot on Contabo:

1. Set up a VPS on Contabo.


2. SSH into your VPS and clone this repository.


3. Install Python and required dependencies (see "Install Requirements").


4. Run the bot using screen or similar to keep it running in the background:

screen -S userbot
python3 userbot.py



Credits

This userbot was created by Alphabotz.

Feel free to use and modify the code, but please give credit to Alphabotz for the original implementation.

License

This project is licensed under the MIT License.

