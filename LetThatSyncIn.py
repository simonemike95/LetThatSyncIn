import sys, os
import asyncio
import websockets
import json

import Drive

'''
I tried to make this script idiot proof by catching
and automatically importing these libraries, but
there may be issues still. This is a very simple script
so there shouldn't be too many issues...
'''
def importPackage(packageName, cmd="pip3 install --user"):
    print(f"Couldn't import {packageName}, trying to install via pip3")
    print(f"Running command: {cmd} {packageName}")
    os.system(f"{cmd} {packageName}")

try:
    from dirsync import sync
except ImportError:
    importPackage("dirsync")
    from dirsync import sync
except Exception as e:
        print("The following error occurred while attempting to import dirsync:")
        print(e)

print("All imports completed successfully.")

'''
These directories will be different for each person
For my use case, I just sync a bunch of Plex storage
I was too lazy to set up a raid configuration, so I
do things in a very stupid way for now.
'''
PLEX_DIR = "G:"
PLEX_DIR_CLONE = "F:"

PLEX1_DIR = "E:"
PLEX1_DIR_CLONE = "J:"

PLEX2_DIR = "I:"
PLEX2_DIR_CLONE = "H:"

METADATA = "C:\\Users\\Mike\\AppData\\Local\\Plex Media Server"
METADATA_CLONE = "D:\\Backups\\Plex-Metadata"

drive_list = []

async def doSync(source, target):
    # Still not sure if async is the answer here.
    # May want to use pure threading when actually doing the sync
    # so that there is no sleeping necessary while copying files
    sync(source, target, 'sync', purge = True)

async def copyJob(drive):
    while 1:
        # TODO: Add supporting class
        source = drive.getSourcePath()
        target = drive.getTargetPath()
        sleep_timer = drive.getSleepTimer()

        await doSync(source, target)
        await asyncio.sleep(1)

async def handleDriveCmd(cmd):
    # TODO: Fill this out with various drive commands
    request = cmd.get("request", None)

    if request == "AddDrive":
        # Add a new drive
        # FIXME: Check for source, target, time, time units
        # before creating a new Drive
        # This is just an example for now
        drive = Drive(PLEX_DIR, PLEX_DIR_CLONE, 1, 4)
        asyncio.get_event_loop().create_task(copyJob(drive))
        drive_list.append(drive)

async def cmdHandler(websocket):
    while 1:
        try:
            msg = websocket.receive()
        except websockets.exceptions.ConnectionClosedError:
            print("Client disconnected unexpectedly")
        except websocket.exceptions.ConnectionClosedOK:
            print("Client disconnected OK")
        except Exception as e:
            print(f"Got an exception: {e}")

        cmd = json.loads(msg)
        request = cmd.get("request", None)

        if "Drive" in request:
            await handleDriveCmd()

        # We don't want to hammer the CPU unnecessarily
        await asyncio.sleep(.5)

def main():
    loop = asyncio.get_event_loop()
    cmd_server = websockets.serve(cmdHandler, "", 1800)
    loop.run_until_complete(cmd_server)
    
    # TODO: Set up websockets for IPC
    # TODO: Set up command handler
        # Ideally, once websockets are setup for IPC, there will be some sort of
        # command/response structure in order to add/remove drives as well as
        # edit existing paths, timers, etc.
    # TODO: Set up config file to save and load previous configurations
    # TODO: Create config file helper to make new config files


    drive1 = Drive(PLEX_DIR, PLEX_DIR_CLONE, 1, 4)
    drive1_task = loop.create_task(copyJob(drive1))

    loop.run_forever()

if __name__ == '__main__':
    main()