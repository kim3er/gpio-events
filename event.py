import time
import RPi.GPIO as GPIO

pins = { }

def register_event(pin, handler, pull_up_down = GPIO.PUD_OFF):
	if not(pin in pins):
		pins[pin] = { 'state': True, 'events': [] }
		GPIO.setup(pin, GPIO.IN, pull_up_down)

	pins[pin]['events'].append(handler)

def trigger_event(pin):
	if pin in pins:
		for event in pins[pin]['events']:
			event(pin, pins[pin]['state'])

def check_state(pin):
	old_state = pins[pin]['state']
	pins[pin]['state'] = GPIO.input(pin)
	return not(pins[pin]['state'] == old_state)

def watch_state_changes(delay = 0):
	while True:
		for pin in pins:
			if check_state(pin):
				trigger_event(pin)

		time.sleep(delay)