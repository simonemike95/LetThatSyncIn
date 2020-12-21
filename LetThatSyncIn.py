import sys, os

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

'''
FIXME: There seems to be some sort of error on the first time the
script gets run, not sure why this results in an ImportError but
the others don't...
'''
try:
    from apscheduler.schedulers.blocking import BlockingScheduler
except ImportError:
    importPackage("apscheduler")
    from apscheduler.schedulers.blocking import BlockingScheduler
except Exception as e:
        print("The following error occurred while attempting to import APScheduler:")
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

def jobListener(event):
    if event.exception:
        print(f"Job failed, error: {event}")
    else:
        print("Job completed successfully.")

def doSync(source, target):
    sync(source, target, 'sync', purge = True)

'''
Obviously changing the "hours" parameter will allow
you to change the time between scheduled runs.
For me, 12 hours is often enough.

A job for each drive to be synced should be set up.
'''
scheduler = BlockingScheduler()
scheduler.add_job(doSync(PLEX_DIR, PLEX_DIR_CLONE), 'interval', hours=12)
scheduler.add_job(doSync(PLEX1_DIR, PLEX1_DIR_CLONE), 'interval', hours=12)
scheduler.add_job(doSync(PLEX2_DIR, PLEX2_DIR_CLONE), 'interval', hours=12)
scheduler.add_job(doSync(METADATA, METADATA_CLONE), 'interval', hours=12)

scheduler.add_listener(jobListener, BlockingScheduler.EVENT_JOB_EXECUTED | BlockingScheduler.EVENT_JOB_ERROR)

print("Starting scheduler.")
scheduler.start()