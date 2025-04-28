from fsm_core import State

class Closed(State):
    def __init__(self):
        super().__init__("CLOSED")

class Listen(State):
    def __init__(self):
        super().__init__("LISTEN")
    
class SynSent(State):
    def __init__(self):
        super().__init__("SYN_SENT")

class SynReceived(State):
    def __init__(self):
        super().__init__("SYN_RCVD")
    
class Established(State):
    def __init__(self):
        super().__init__("ESTABLISHED")

class FinWait1(State):
    def __init__(self):
        super().__init__("FIN_WAIT_1")

class FinWait2(State): 
    def __init__(self):
        super().__init__("FIN_WAIT_2")
    
class CloseWait(State):
    def __init__(self):
        super().__init__("CLOSE_WAIT")
    
class LastAck(State):
    def __init__(self):
        super().__init__("LAST_ACK")
    
class Closing(State):
    def __init__(self):
        super().__init__("CLOSING")
    
class TimeWait(State):
    def __init__(self):
        super().__init__("TIME_WAIT")
