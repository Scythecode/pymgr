# pymgr

Simple package manager written in python. Right now it's a work in progress, but should be ready one day.
I like penis

# How to use:

**Cum**ming soon!

# Config
You mainly edit with the config.json file. Like this:<br/>
```json
{
    "repositories": {
        "https://archlinux.org/packages/?sort=&repo=Extra": { // Replace with the link of your choice
            "nickname": "arch/extra", // Nickname for the repo
            "priority": 64 // Priority, if higher it will be more likely to be first to be checked
        }
    },
    "manager_name": "pymgr",
    "prompt": "Is this okay?",
    "input": [
        {
            "name": "y",
            "yes": true
        },
        {
            "name": "n",
            "yes": false
        }
    ]
}
```
<br/>
Note that comments aren't allowed in json, there are only added for for showcasing. Please remove them<br/>
Alternatively, the repositories key can be a string referencing a path to a .conf file which looks like this:<br/>
```ini
["https://archlinux.org/packages/?sort=&repo=Extra"]
nickname = arch/extra
priority = 512
```<br/>
