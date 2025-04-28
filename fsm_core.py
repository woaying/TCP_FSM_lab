# Basic FSM framework (Mealy Machine Style) matching Java FSM behavior

class FsmException(Exception):
    pass

class State:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return self.name

class Event:
    def __init__(self, name, value=None):
        self.name = name
        self.value = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __str__(self):
        return f"Event({self.name})"

class Action:
    def execute(self, fsm, event):
        raise NotImplementedError("Action subclasses must implement execute(fsm, event)")

class Transition:
    def __init__(self, current_state, event, next_state, action):
        self.current_state = current_state
        self.event = event
        self.next_state = next_state
        self.action = action

    def get_current_state(self):
        return self.current_state

    def get_event(self):
        return self.event

    def get_next_state(self):
        return self.next_state

    def do_action(self, fsm, event):
        self.action.execute(fsm, event)

    def get_key(self):
        return (self.current_state.get_name(), self.event.get_name())

class FSM:
    def __init__(self, fsm_name, start_state=None):
        self.fsm_name = fsm_name
        self.start_state = start_state
        self.current_state = start_state
        self.transitions = {}
        self.tracing = False

    def add_transition(self, transition):
        key = transition.get_key()
        if key in self.transitions:
            raise FsmException(f"Duplicate transition for ({key[0]}, {key[1]})")
        self.transitions[key] = transition

    def do_event(self, event):
        key = (self.current_state.get_name(), event.get_name())
        if key not in self.transitions:
            raise FsmException(f"No transition for ({key[0]}, {key[1]})")
        transition = self.transitions[key]
        if self.tracing:
            print(f"Transitioning on event {event.get_name()} from {self.current_state.get_name()} to {transition.get_next_state().get_name()}")
        transition.do_action(self, event)
        self.current_state = transition.get_next_state()

    def current_state_name(self):
        return self.current_state.get_name()

    def next_state(self, state):
        self.current_state = state

    def reset(self):
        self.current_state = self.start_state

    def trace_on(self):
        self.tracing = True

    def trace_off(self):
        self.tracing = False



if __name__ == "__main__":
    print("FSM framework initialized. Ready to build the TCP state machine.")