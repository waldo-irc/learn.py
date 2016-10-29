# learn.py
This is a learn module i created for Sopel bot.  The module has been tested significantly and is sanitized/hardened (or seems like it hehe...if you find any bugs please let me know!) 
&nbsp;

# Installation
Simply put learn.py and dictionary in your .sopel/modules folder, and activate the learn module.

Learn.py does the heavy lifting, dictionary holds the commands, learn_bl holds users who have been blacklisted from created commands for 24 hrs (in order to throttle).
&nbsp;

After installation, do a !samplecommand to make sure it works.  !unbookie samplecommand can remove the sample command after.
&nbsp;

# Commands
bookie (usage: !bookie cmd command stuff goes here) - This adds a new command.
&nbsp;

rebookie (usage: !rebookie cmd new stuff goes here) - This overwrites an existing commands.
&nbsp;

bookielist (usage: !bookielist) - This grabs a list of all custom made commands and PM's them to the user.
&nbsp;

mybookielist (usage: !mybookielist) - This grabs a list of all custom made commands made by the user and PM's them to the user.
&nbsp;

unbookie (usage: !unbookie cmd) - This deletes a command completely.
&nbsp;

!yournewcommand - To run your newly created command.

# Current known issues - 
None -

# Plans to come
Plans to add a command limit.
