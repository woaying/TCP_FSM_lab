from fsm_core import Event

class ActiveOpen(Event):
    def __init__(self):
        super().__init__("ACTIVE_OPEN")

class PassiveOpen(Event):
    def __init__(self):
        super().__init__("PASSIVE_OPEN")

# class Send(Event):
#     def __init__(self):
#         super().__init__("SEND")

class ReceiveSyn(Event):
    def __init__(self):
        super().__init__("SYN")

class ReceiveSynAck(Event):
    def __init__(self):
        super().__init__("SYNACK")

class ReceiveAck(Event):
    def __init__(self):
        super().__init__("ACK")

class Close(Event):
    def __init__(self):
        super().__init__("CLOSE")

class ReceiveFin(Event):
    def __init__(self):
        super().__init__("FIN")

class Timeout(Event):
    def __init__(self):
        super().__init__("TIMEOUT")

class SData(Event):
    def __init__(self, value=1):
        super().__init__("SDATA", value)

class RData(Event):
    def __init__(self, value=1):
        super().__init__("RDATA", value)