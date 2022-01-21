from micropython import const

from kmk.modules import Module
from kmk.keys import make_argumented_key

'''
example
KC.PR(KC.LGUI(KC.LCTRL(KC.RIGHT)), KC.LGUI(KC.LCTRL(KC.LEFT)))
'''
class PressReleaseMeta:
    def __init__(self,press,release):
        self.press=press
        self.release=release
class PressRelease(Module):
    tap_time = 30

    def __init__(self):
        self.was_pressed=False
        make_argumented_key(
            validator=lambda press,release:PressReleaseMeta(press=press,release=release),
            names=('PR',),
        )

    def during_bootup(self, keyboard):
        return

    def before_matrix_scan(self, keyboard):
        return

    def after_matrix_scan(self, keyboard):
        return

    def process_key(self, keyboard, key, is_pressed):
        if not isinstance(key.meta,PressReleaseMeta):
            return key
        if is_pressed:
            if not self.was_pressed:
                #add and reserve remove
                keyboard.tap_key(key.meta.press)
                self.was_pressed=True
                return None
            #already removed 
            return None
        #add and reserve remove
        keyboard.tap_key(key.meta.release)
        self.was_pressed=False
        return None

    def before_hid_send(self, keyboard):
        return

    def after_hid_send(self, keyboard):
        return

    def on_powersave_enable(self, keyboard):
        return

    def on_powersave_disable(self, keyboard):
        return
