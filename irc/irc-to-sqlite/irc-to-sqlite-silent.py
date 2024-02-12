import sqlite3
import irc.client
import time

# SQLite database initialization
def initialize_database():
    conn = sqlite3.connect('irc_logs.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS irc_logs (
                      id INTEGER PRIMARY KEY,
                      channel TEXT,
                      username TEXT,
                      message TEXT,
                      timestamp TEXT)''')
    conn.commit()
    conn.close()

# IRC logger bot
class IRCLoggerBot(irc.client.SimpleIRCClient):
    def __init__(self):
        irc.client.SimpleIRCClient.__init__(self)

    def on_welcome(self, connection, event):
        print("Connected to IRC server.")
        connection.join("#your_channel_name")

    def on_pubmsg(self, connection, event):
        channel = event.target
        username = event.source.nick
        message = event.arguments[0]
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

        # Insert message into SQLite database
        conn = sqlite3.connect('irc_logs.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO irc_logs (channel, username, message, timestamp)
                          VALUES (?, ?, ?, ?)''', (channel, username, message, timestamp))
        conn.commit()
        conn.close()

def main():
    initialize_database()

    # IRC connection settings
    server = "irc.server.com"
    port = 6667
    nickname = "YourBotNickname"
    channel = "#your_channel_name"

    # Start IRC logger bot
    client = IRCLoggerBot()
    try:
        client.connect(server, port, nickname)
        client.start()
    except irc.client.ServerConnectionError as e:
        print(str(e))

if __name__ == "__main__":
    main()
