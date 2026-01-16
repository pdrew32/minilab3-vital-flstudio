# MiniLab 3 → Vital (FL Studio)

This repository provides a custom Arturia MiniLab 3 controller-script
mapping for Vital in FL Studio.

It allows MiniLab knobs and faders to control meaningful Vital parameters
without per-instance MIDI linking.

This is based on a post by Tobago on the [Arturia Forums](https://forum.arturia.com/t/guide-mapping-knobs-faders-to-3rd-party-plugin-parameters-fl-studio/7408). Check that out if you're interested in mapping other plugins.


## What this does
- Automatic mapping when Vital is focused
- No manual MIDI learn per instance
- Uses FL Studio controller scripting

## Files
- `MiniLab3Plugin_vital_snippet.py` – code to paste into FL’s script
- `vital_param_map.txt` – parameter IDs and how to discover your own

## Installation
1. Locate:
   C:\Users\[username]\Documents/Image-Line/FL Studio/Settings/Hardware/Arturia/MiniLab3/
2. Open `MiniLab3Plugin.py`
3. Paste the snippet under the plugin mapping section that begins with the following

```
def Plugin(hw_param, hw_value, moved_param) :
    recognized_plugin = False
    plugin_name = plugins.getPluginName(channels.selectedChannel())
    
    global ABSOLUTE_VALUE
    
    if plugin_name == 'FLEX' :
        recognized_plugin = True
        ## FLEX ##
    
        PARAM_MAP = {
                '14':10,
                '15':11,
                '30':12,
                '31':13,
                '86':21,
                '87':22,
                '89':25,
                '90':30,
                '110':0,
                '111':2,
                '116':3,
                '117':4,
                '1':-1
                }
```

                
4. Save the file and close.
5. Restart FL Studio if it was open.

## Customizing the mapping
See `vital_param_map.txt` for the list of available parameters if you want to change the mappings. I recommend opening an instance of Vital in FL Studio and tweaking the parameter you're interested in mapping so you can see the name of the parameter in FL Studio's `hint panel`. You can then ctrl-f that name in `vital_param_map.txt` to find its parameter number.

