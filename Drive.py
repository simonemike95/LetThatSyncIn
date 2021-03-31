# TODO: This will be the class used for each drive that the user has
# Ideally, once websockets are setup for IPC, there will be some sort of
# command/response structure in order to add/remove drives as well as
# edit existing paths, timers, etc.

# Each Drive object will consist of:
#   - Source path
#   - Target path
#   - Sleep timer (to be used in async task)