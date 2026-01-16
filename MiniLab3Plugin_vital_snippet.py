elif plugin_name == 'Vital':
    recognized_plugin = True

    PARAM_MAP = {
        '14': 382,  # Fader 1: Oscillator 1 Level
        '15': 405,  # Fader 2: Oscillator 2 Level
        '30': 513,  # Fader 3: Oscillator 3 Level
        '31': 449,  # Fader 4: Sample Level

        '86': 211,  # Knob 1: Macro 1
        '87': 212,  # Knob 2: Macro 2
        '89': 213,  # Knob 3: Macro 3
        '90': 214,  # Knob 4: Macro 4

        '110': 48,  # Knob 5: Env 1 Attack
        '111': 50,  # Knob 6: Env 1 Decay
        '116': 54,  # Knob 7: Env 1 Sustain
        '117': 52,  # Knob 8: Env 1 Release

        '1': -1
    }
