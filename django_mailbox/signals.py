from django.dispatch.dispatcher import Signal

# message_received = Signal(providing_args=['message'])
message_received = Signal('message')