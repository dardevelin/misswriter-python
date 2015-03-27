Miss Writer - because mr writer failed

hexchat - python plugin script that can always prefix messages of a given channel

particularly useful for game channels where is common practice to have a character name
before the actual messages

How to use the plugin:

/misswriter set <captain>
/misswriter setmask <captain>

the plugin takes the name of the current channel and associates it with the prefix "<captain>"
from there on all your messages in that channel will be sent with a prefix of "<captain>"

eg, if you type "_this is a demo_"
"<captain> this is a demo_" would be sent instead


/misswriter unset
/misswriter unsetmask
removes the prefix associated with the current channel

see LICENSE file for full gplv3
