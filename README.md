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
Below are some basic goals for the project (not in order of priority).

- Drive statistic options
  - Space available in existing partitions
  - Read/Write speed test to set drives
- Drive path options
  - File/directory exclusion options
  - Network drive support
- Output/logging configuration options
  - Verbose (output all logging info messages once added, along with statistics from the run)
  - Run completion (success/fail, succinct summary)
  - Save logs to external file
  - Setting max size of log file files/directory
