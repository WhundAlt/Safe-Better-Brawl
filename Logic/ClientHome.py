from Logic.Home.LogicDailyData import LogicDailyData
from Logic.Home.LogicConfData import LogicConfData

class LogicClientHome:

    def encode(self):
        LogicDailyData.encode(self)
        LogicConfData.encode(self)

        self.writeLong(self.player.ID)

        self.writeVInt(1)  # array
        self.writeVInt(81) # Notification ID
        self.writeInt(3) # Notification Index
        self.writeBoolean(False) # Notification Read
        self.writeInt(0) # Notification Time Ago
        self.writeString(f"pon") # Notification Message Entry
        self.writeVInt(1)#0-служба поддержки 1-система
        # Custom Support Message Notification End
        for x in range(0):
            pass

        self.writeVInt(0)  # Unknown

        self.writeUInt8(0) # Unknown
