# -*- coding: utf-8 -*-
#   
# HexBinDecConverter is a number converter for Sublime Text 3
#
# https://github.com/rohanrhu/sublime-HexBinDecConverter
#
# Licensed under MIT
# Copyright (C) 2018, Oğuzhan Eroğlu (https://oguzhaneroglu.com/) <rohanrhu2@gmail.com>

import sublime
import sublime_plugin

numbers = [str(i) for i in range(10)]

class HexBinDecConverterCommand(sublime_plugin.TextCommand):
    def run(self, edit, from_event=False, show_all=False, point=False):
        view = self.view

        for region in view.sel():
            if point:
                wordloc = view.word(point.conjugate())
                word = view.substr(wordloc)
            else:
                word = view.substr(view.word(region))
            
            if word.__len__() > 0:
                is_dec = False
                is_hex = False
                is_bin = False

                if word.__len__() > 2 and word[:2] == '0x':
                    is_hex = True
                    decval = int(word[2:], 16)
                elif word[0] in numbers:
                    if word[-1] == 'h' or word[-1] == 'H':
                        is_hex = True
                        decval = int(word[:-1], 16)
                    elif word[-1] == 'b' or word[-1] == 'B':
                        binary = word[:-1]

                        is_bin = True
                        for i in binary:
                            if i != '0' and i != '1':
                                is_bin = False
                                break

                        if is_bin:
                            decval = int(binary, 2)

                if show_all or not from_event:
                    is_dec = True

                    for i in word:
                        if i not in numbers:
                            is_dec = False
                            break

                    if is_dec:
                        decval = int(word)
                        hexval = hex(decval)
                    elif is_bin:
                        hexval = hex(decval)

                if is_dec or is_hex or is_bin:
                    binval = '{0:b}'.format(decval).zfill(64)
                    binval = binval[:8] + ' ' + binval[8:]
                    binval = binval[:17] + ' ' + binval[17:]
                    binval = binval[:26] + ' ' + binval[26:]
                    binval = binval[:35] + ' ' + binval[35:]
                    binval = binval[:44] + ' ' + binval[44:]
                    binval = binval[:53] + ' ' + binval[53:]
                    binval = binval[:62] + ' ' + binval[62:]
                    binval = binval[:36] + '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + binval[36:]

                    decval = str(decval)

                    loc = -1
                    if point:
                        loc = wordloc.end()

                    if is_hex:
                        view.show_popup('<b style="color: red;">Dec:</b> '+decval+'<br><b style="color: blue;">Bin</b>: '+binval, location=loc)
                    elif is_bin:
                        view.show_popup('<b style="color: red;">Dec:</b> '+decval+'<br><b style="color: green;">Hex</b>: '+hexval+'<br><b style="color: blue;">Bin</b>: '+binval, location=loc)
                    else:
                        view.show_popup('<b style="color: red;">Hex:</b> '+hexval+'<br><b style="color: blue;">Bin</b>: '+binval, location=loc)


class EventListener(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        view.run_command('hex_bin_dec_converter', {"from_event": True})
    def on_hover(self, view, point, hover_zone):
        if hover_zone == sublime.HOVER_TEXT:
            view.run_command('hex_bin_dec_converter', {"from_event": True, "show_all": True, "point": point})