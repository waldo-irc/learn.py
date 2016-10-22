# learn.py
This is a learn module i created for Sopel bot.  The module has been tested significantly and is sanitized/hardened (or seems like it hehe...if you find any bugs please let me know!) 
&nbsp;

# Installation
Simply put learn.py, bookiecmds.py, and dictionary in your .sopel/modules folder, and activate both bookiecmds and learn modules.  
&nbsp;

bookiecmds.py contains all the new commands, dictionary is the dictionary it grabs the commands from, and learn.py is the main module that does the heavy lifting.
&nbsp;

After installation, do a !samplecommand to make sure it works.  !unbookie can remove the sample command after.
&nbsp;

# Commands
bookie (usage: !bookie cmd command stuff goes here) - This adds a new command.
&nbsp;

rebookie (usage: !rebookie cmd new stuff goes here) - This overwrites an existing commands.
&nbsp;

bookielist (usage: !bookielist) - This grabs a list of all custom made commands and PM's them to the user.
&nbsp;

unbookie (usage: !unbookie cmd) - This deletes a command completely.
&nbsp;

!yournewcommand - To run your newly created command.

# Current known issues - 
Unbookie doesn't do a good restart. The way it restarts breaks any other modules in progress as it does a full sopel --quit and sopel -d --quiet to fully remove the module command.
