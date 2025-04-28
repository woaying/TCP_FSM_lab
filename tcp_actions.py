from fsm_core import Action

class NoAction(Action):
    def execute(self, fsm, event):
        # Default action: print current state and event
        print(f"Event {event.get_name()} received, current State is {fsm.current_state_name()}.")
        # No state change

class SendDataAction(Action):
    def __init__(self, counter):
        self.counter = counter # a list to hold the counter value
        # Using a list to allow modification within the action

    def execute(self, fsm, event):
        self.counter[0] += event.get_value()
        print(f"DATA sent {self.counter[0]}")

class ReceiveDataAction(Action):
    def __init__(self, counter):
        self.counter = counter # a list to hold the counter value
        # Using a list to allow modification within the action

    def execute(self, fsm, event):
        self.counter[0] += event.get_value()
        print(f"DATA received {self.counter[0]}")
        # No state change