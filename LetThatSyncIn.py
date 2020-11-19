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
PLEX_DIR = ""
PLEX_DIR_CLONE = ""

PLEX1_DIR = ""
PLEX1_DIR_CLONE = ""

PLEX2_DIR = ""
PLEX2_DIR_CLONE = ""

def doSync(source, target):
    sync(source, target, 'sync', purge = True)

'''
Obviously changing the "hours" parameter will allow
you to change the time between scheduled runs.
For me, 12 hours is often enough.
'''
scheduler = BlockingScheduler()
scheduler.add_job(doSync, 'interval', hours=12)

print("Starting scheduler.")
scheduler.start()