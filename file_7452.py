import threading
def job(): print("Running")
t = threading.Thread(target=job)
t.start()