from datetime import datetime
def strToDateTime(time):
    tempTime = time.replace("0000","000").replace("T", " ").split("+")[0]
    return datetime.fromisoformat(tempTime)