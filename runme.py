import sys
import load

#Quick framework to load the plugin from the cmd line / pycharm
load.plugin_start('.')
if sys.version_info[0] < 3:
    anyKey = raw_input("Enter command..")
else:
    anyKey = input("Enter command...")
print(anyKey + " isn't the any key, but I'll stop anyway!")
load.plugin_stop()