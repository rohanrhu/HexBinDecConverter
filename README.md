# HexBinDecConverter
Hexadecimal, Binary and Decimal number converter plugin for Sublime Text 3

![alt text](http://oguzhaneroglu.com/static/images/hexbindecconverter.jpg "Hex/Bin/Dec number converter plugin for Sublime Text 3")

## Installation

#### Git

##### Linux
```bash
cd ~/.config/sublime-text-3/Packages/
git clone https://github.com/rohanrhu/HexBinDecConverter.git HexBinDecConverter
```

##### Windows

```bash
cd "%HOMEPATH%\AppData\Roaming\Sublime Text 3\Packages"
git clone https://github.com/rohanrhu/HexBinDecConverter.git HexBinDecConverter
```

## Usage

#### Events
Cursor on hexadecimal or binary and hover mouse point on hexadecimal, binary or decimal shows popup

Hexadecimal Syntaxes:
```assembly
0xa
0ah
```

Binary Syntaxes:
```assembly
1010b
```

#### Shortcuts
You can set shorcut with `hex_bin_dec_converter` function
```json
{"keys": ["ctrl+k", "ctrl+i"], "command": "hex_bin_dec_converter"}
```

#### Menu Commands
There're one menu (ctrl+shift+p) command

- Show Popup: `HexBinDecConverter: Show Popup`

## License
MIT
