import sys, os
import asyncio
import websockets

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
    import six
except ImportError:
    importPackage("six", "pip3 install --ignore-installed --user")
except Exception as e:
    print("The following error occurred while attempting to import six:")
    print(e)

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

def main():
    loop = asyncio.get_event_loop()
    # TODO: Set up websockets for IPC
    # TODO: Set up command handler

if __name__ == '__main__':
    main()