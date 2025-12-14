dbMessages = [
    """
    CREATE TABLE IF NOT EXISTS messages (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      contactId TEXT NOT NULL,
      channelId INTEGER NOT NULL,
      message TEXT NOT NULL,
      sender TEXT,
      mentions TEXT,
      fromNodeNum INTEGER,
      toNodeNum INTEGER,
      toNodeType INTEGER DEFAULT 0,
      messageId INTEGER,
      options TEXT,
      sentTimestamp INTEGER,
      recvTimestamp INTEGER,
      protocol TEXT NOT NULL,
      connId TEXT
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_messages_contact ON messages(contactId)",
    "CREATE INDEX IF NOT EXISTS idx_messages_channel ON messages(channelId)",
]
