# learn.py
<br />
This is a learn module i created for Sopel bot.  The module has been tested significantly and is sanitized/hardened (or seems like it hehe...if you find any bugs please let me know!) 
<br />
Simply put learn.py, bookiecmds.py, and dictionary in your .sopel/modules folder, and activate both bookiecmds.py and learn.py module.  bookiecmds.py contains all the new commands, dictionary is the dictionary it grabs the commands from, and learn.py is the main module that does the heavy lifting.
<br />
After installation, do a !samplecommand to make sure it works.  !unbookie can remove the sample command after.
<br />
# commands
<br />
bookie (usage: !bookie cmd command stuff goes here) - This adds a new command.
<br />
rebookie (usage: !rebookie cmd new stuff goes here) - This overwrites an existing commands.
<br />
bookielist (usage: !bookielist) - This grabs a list of all custom made commands and PM's them to the user.
<br />
unbookie (usage: !unbookie command) - This deletes a command completely.
