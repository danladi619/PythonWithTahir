import threading


class FahadsMessenger(threading.Thread):

    def run(self):
        for _ in range(10):
            print(threading.current_thread().getName())


x = FahadsMessenger(name="send out messages")
y = FahadsMessenger(name="Receive Messages")

x.start()
y.start()