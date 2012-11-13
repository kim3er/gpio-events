import event

def button(pin, state):
	print pin, state

def another_handler(pin, state):
	print ('We rock' if state else 'We flock'), pin

event.register_event(1, button)
event.register_event(1, another_handler)
event.register_event(2, another_handler)

event.trigger_event(1)

event.watch_state_changes()