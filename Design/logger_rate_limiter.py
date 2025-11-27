class Logger:

    def __init__(self):
        self.message_to_timestamp = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.message_to_timestamp:
            self.message_to_timestamp[message] = timestamp
            return True

        if timestamp >= self.message_to_timestamp[message] + 10:
            self.message_to_timestamp[message] = timestamp
            return True
        else:
            return False

        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
