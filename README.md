# LetThatSyncIn
A basic Python script to schedule the sync of drives/folders regardless of platform, every X amount of time.


## Commands and Responses

### Websocket
The websocket used for commands and responses will be run at:
`localhost:1800`
### List Drives
*Example: Input*
```
{
  "request": "ListDrives"
}
```

*Example: Output (if there are existing drives)*
```
{
  "response": "ListDrives",
  "Drives": [
    "Test Drive": {
      "Source": "C:\Whatever",
      "Target": "D:\Whatever",
      "Sleep": 12,
      "Units": "Hour"
    }
  ]
}
```

### Adding a Drive
*Example: Input*
```
{
  "request": "AddDrive",
  "Drives": [
    "1": {
      "Name": "Test Drive",
      "Source": "C:\Whatever",
      "Target": "D:\Whatever",
      "Sleep": 12,
      "Units": "Hour"
    }
  ]
}
```
*NOTE: Drive name defaults to its index in the list of drives.*

*NOTE: Valid time units include: Seconds, Minutes, Hours, Days. Defaults to "Days" if field is omitted.*


*Example: Ouptut when adding a drive succeeds.*
```
{
  "response": "AddDrive",
  "Result": "Success"
}
```

*Example: Ouptut when adding a drive fails.*
```
{
  "response": "AddDrive",
  "Result": "Failure",
  "Error": "Invalid Source Path",
  "Warning": "Invalid Units"
}
```
*NOTE: Error and Warning fields may appear independent of each other or simultaneously.*

*NOTE: Possible values for "Error" field are: Invalid Source Path, Invalid Target Path.*

*NOTE: Possible vlaues for "Warning" field are: Invalid Time, Invalid Units. Drives default to 1 day (one day) in the case of invalid input. This can be edited afterwards to correct any issues.*


## Current Work
The current objectives are:
- Necessary websocket(s) set up
- Various Drive commands outlined
- Command handler written according to documentation
- User configurable websocket address and port (low priority)
- Config file (low priority)
- Config file creator tool (very low priority)


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


## Why?
This project started out as an idea after I had established a large Plex server and did not want to move to a raid configuration.
While a raid setup would probably save me lots of time and energy, I had no desire to learn about how it all worked, not to mention moving my existing data (close to 12TB now...) would be a PITA.
Instead, I starting writing this script in order to replace my current bash scripts that get run manually every time new files are added.
Many, many tools like this already exist, but this is a fun project for when I have some free time here and there.
I also find myself wishing there was a simple to setup tool that did this, requiring no downloads or stnadalone applications.
