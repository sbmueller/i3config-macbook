# i3config-macbook
## Dependencies
Needs i3pystatus installed. Also, the `light` fork from my repos needs to be built and installed from the master and keyboard branch. This enables control of screen and keyboard backlight.
## Tuning
To change CMD and CRTL keys, edit the `/usr/share/X11/xkb/symbols/pc` file and switch the corresponding entries. Then delete all `*.xmk` files in `/var/lib/xkb`.
## Installation
Put all in your i3 config directory (`~/.i3/` or `~/.config/i3`)
