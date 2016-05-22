# coding: utf8
from i3pystatus import Status

globInterval = 1
status = Status()

status.register("clock",
	format="%a %-d %b %X KW%V",)

status.register("battery",
    format="{status}/{consumption:.2f}W {percentage:.2f}% {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=5,
    status={
        "DIS": "↓",
        "CHR": "↑",
        "FULL": "=",
    },)

status.register("network",
	interface="wlp3s0b1",
	format_up="{essid} {quality:03.0f}%",)

status.register("mem",
	format="RAM:{avail_mem} MB",)

status.register("cpu_usage",
	format="CPU:{usage:02}%",)

status.register("pulseaudio",
    format="♪{volume}%",)

status.register("backlight",
	interval=globInterval,
	format="☀{percentage}%",
	base_path="/sys/class/backlight/gmux_backlight/",)

status.register("backlight",
	interval=globInterval,
	format="☐{percentage}%",
	base_path="/sys/class/leds/smc::kbd_backlight/",)

status.run()
