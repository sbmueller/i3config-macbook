# coding: utf8
from i3pystatus import Status

globInterval = 10
status = Status()

status.register("shell",
        command = "setxkbmap -print | grep xkb_symbols | awk '{print $4}' | awk -F\"+\" '{print $2}'",
        on_leftclick = "(setxkbmap -query | grep -q \"layout:\s\+us\") && setxkbmap 'de(mac)' || setxkbmap us",
        on_rightclick = "run",
        )

status.register("clock",
	format="%a %-d %b %H:%M KW%V",)

status.register("uptime",
        format="UP {hours}:{mins}",)

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
	format_up="WIFI {quality:03.0f}%",
        format_down="WIFI DOWN",)

status.register("network",
        interface="enp2s0",
        format_up="ETH {v4}",
        format_down="ETH DOWN",)


status.register("mem_bar",)

status.register("mem",
	format="RAM {avail_mem} MB",)

status.register("cpu_usage",
	format="CPU {usage:02}%",)

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

status.register("github",
        username="",
        password="",
        format="{unread}",)

status.run()
