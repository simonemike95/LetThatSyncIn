# LetThatSyncIn
A basic Python script to schedule the sync of drives/folders regardless of platform, every X amount of time.


## Why?
This project started out as an idea after I had established a large Plex server and did not want to move to a raid configuration.
While a raid setup would probably save me lots of time and energy, I had no desire to learn about how it all worked, not to mention moving my existing data (close to 12TB now...) would be a PITA.
Instead, I starting writing this script in order to replace my current bash scripts that get run manually every time new files are added.
Many, many tools like this already exist, but this is a fun project for when I have some free time here and there.
I also find myself wishing there was a simple to setup tool that did this, requiring no downloads or stnadalone applications.

## Moving Forward
I'd like to ensure this script is platform agnostic and reliable, as I plan to use it not only with my Plex server, but other machines I need to backup as well.
Flexibility is also a goal of this project, hopefully allowing various input/arguments to be used in the future.

## Known Issues
The project is still in its very very early stages, and there are bound to be issues in the future but here are some currently known issues...
- Upon the initial run (at least on MacOS), Python cannot locate part of the apscheduler module for some reason.
