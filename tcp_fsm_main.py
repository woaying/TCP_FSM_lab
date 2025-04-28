from fsm_core import FSM, Transition, FsmException
from tcp_states import *
from tcp_events import *
from tcp_actions import *

import sys

def build_tcp_fsm():
    # Create counters for data sent and received
    send_counter = [0]
    receive_counter = [0]

    # Create FSM
    closed = Closed()
    listen = Listen()
    syn_sent = SynSent()
    syn_rcvd = SynReceived()
    established = Established()
    fin_wait_1 = FinWait1()
    fin_wait_2 = FinWait2()
    close_wait = CloseWait()
    last_ack = LastAck()
    closing = Closing()
    time_wait = TimeWait()

    # Initialize the FSM
    fsm = FSM("TCP_FSM", Closed())

    # Default action
    default_action = NoAction()
    # Sepecial actions
    send_data_action = SendDataAction(send_counter)
    receive_data_action = ReceiveDataAction(receive_counter)

    # Build transitions based on given Figure 1
    transitions = [
        # Connection setup
        Transition(closed, PassiveOpen(), listen, default_action),
        Transition(closed, ActiveOpen(), syn_sent, default_action),
        Transition(listen, ReceiveSyn(), syn_rcvd, default_action),
        Transition(syn_sent, ReceiveSyn(), syn_rcvd, default_action),
        Transition(syn_sent, ReceiveSynAck(), established, default_action),
        Transition(syn_rcvd, ReceiveAck(), established, default_action),
        # Closed during connection setup
        Transition(syn_sent, Close(), closed, default_action),
        Transition(syn_rcvd, Close(), fin_wait_1, default_action),
        Transition(listen, Close(), closed, default_action),
        # Data transfer
        Transition(established, SData(1), established, send_data_action),
        Transition(established, RData(1), established, receive_data_action),
        # Normal termination
        Transition(established, Close(), fin_wait_1, default_action),
        Transition(fin_wait_1, ReceiveAck(), fin_wait_2, default_action),
        Transition(fin_wait_2, ReceiveFin(), time_wait, default_action),
        Transition(time_wait, Timeout(), closed, default_action),
        # Peer closes first
        Transition(established, ReceiveFin(), close_wait, default_action),
        Transition(close_wait, Close(), last_ack, default_action),
        Transition(last_ack, ReceiveAck(), closed, default_action),
        # Simultaneous close
        Transition(fin_wait_1, ReceiveFin(), closing, default_action),
        Transition(closing, ReceiveAck(), time_wait, default_action),
    ]

    # Add transitions to the FSM
    for t in transitions:
        fsm.add_transition(t)

    return fsm

def parse_input(token):
    token = token.strip().upper()
    if token == "ACTIVE":
        return ActiveOpen()
    elif token == "PASSIVE":
        return PassiveOpen()
    elif token == "SYN":
        return ReceiveSyn()
    elif token == "SYNACK":
        return ReceiveSynAck()
    elif token == "ACK":
        return ReceiveAck()
    elif token == "FIN":
        return ReceiveFin()
    elif token == "CLOSE":
        return Close()
    elif token == "SDATA":
        return SData(1)
    elif token == "RDATA":
        return RData(1)
    elif token == "TIMEOUT":
        return Timeout()
    else:
        return None
    
def main():
    fsm = build_tcp_fsm()
    print("TCP FSM simulation started.")
    print("Please enter events separated by spaces to trigger state transitions.")
    print("(Press Enter without typing anything to exit.)\n")

    try:
        while True:
            lin = input("Enter events:> ").strip()
            if not lin:
                print("\nNo input detected. FSM simulation ended.")
                break
            tokens = lin.split()
            for token in tokens:
                event = parse_input(token)
                if event is None:
                    print(f"Error: unexpected Event: {token}")
                    continue
                try:
                    fsm.do_event(event)
                except FsmException as e:
                    print(e)
    except EOFError:
        print("\nEnd of input detected. FSM simulation ended.")

if __name__ == "__main__":
    main()