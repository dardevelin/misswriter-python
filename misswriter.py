from __future__ import print_function
__module_name__ = "Miss Writer"
__module_version__ = "0.98"
__module_description__ = "The version is because we can, writer, because it writes"
__module_author__ = "Darcy 'dardevelin' Bras da Silva"

import hexchat


# chanlist holds the channel name->prefix association
# FIXME: keep track of the server name as well to avoid name clash
chanlist = {}

def command_handler(word, word_eol, userdata):
	"""
	responds to
        /misswriter set "prefix"
        /misswriter setmask "prefix"
        /misswriter unset
        /misswriter unsetmask
	"""
	wcount = len(word)
	channel = hexchat.get_info("channel")
        # stores the final message to display to the user
        cmdmsg = ""
        
	lw = word[1].lower() # don't repeat the operation
	if wcount > 2:
		if lw == "set" or lw == "setmask":
			if channel in chanlist:
                                cmdmsg = "updated {}: prefix of {} to {}".format(channel,chanlist[channel], word_eol[2])
				chanlist.update({channel:word_eol[2]})
			else:
                                cmdmsg = "{}: prefix was set to {}".format(channel, word_eol[2])
				chanlist[channel] = word_eol[2]
			
	if lw == "unset" or lw == "unsetmask":
                chanlist.pop(channel, None)
                cmdmsg = "{} prefix was removed".format(channel)

        print("\0034 {} \003".format(cmdmsg))

def trap_cb(word, word_eol, userdata):
	#it is a good idea to get this data before the user changes it
	nickname = hexchat.get_info("nickname")
	channel = hexchat.get_info("channel")

	if channel in chanlist:
		msg = "{} {}".format(chanlist[channel],word_eol[0])
	else:
		msg = "{}".format(word_eol[0])

	hexchat.command("MSG {} {}".format(channel,msg))
	return hexchat.EAT_ALL


def unload_cb(userdata):
	print("\0034 {} {} {}".format(__module_name__, __module_version__, "has been unloaded\003"))


def on_init_cb():
	hexchat.hook_command("misswriter", command_handler, None, hexchat.PRI_NORM)
	hexchat.hook_command("", trap_cb, None, hexchat.PRI_NORM)
	hexchat.hook_unload(unload_cb)
	print("\0034 {} {} {}".format(__module_name__, __module_version__, "has been loaded\003"))

on_init_cb()
