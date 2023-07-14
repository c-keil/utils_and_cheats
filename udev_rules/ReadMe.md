# Udev Rules
It is possible to configure a udev rule to assign a specific name to a serial/video/... device. This can be used to destinguish between different devices that connect as /dev/ttyACM0,ACM1,etc.

NOTE, a simple way to do this can be to use the `/dev/serial/by-id/` or `/dev/v4l/by-id/` (for video) path for each device.

# Setting a custom symlink
A custom symlink can be set for most connected devices. To do this you need to add a rule to the user udev rules location: `/etc/udev/rules.d/`. A rule is a file with the name having the format `##-name.rules` the ## should likely be 99. Higher numbers override rules with lower numbers. To make a rule for a ublox gnss device, I did the following:
 - Find a unique attribute with `$ udevadm info -an /dev/ttyACM0`. This gives a long list of attributes. I found a unique one like: `ATTRS{product}=="u-blox GNSS receiver"`. Note that `$  udevadm info /dev/ttyACM0` without the `-a` option will give different results. These can be used as environment variables in the rule if desired.
 - With the unique attribute write a rule in the rules directory. This should be something like ` /etc/udev/rules.d/99-ublox.rules` with the contents:
 ``` 
 ACTION=="add|change", SUBSYSTEM=="tty", ATTRS{product}=="u-blox GNSS receiver", SYMLINK="ttyACM_UBLOX" 
 ```
 - This should make the serial port show up as `/dev/ttyACM0` and the symlink `/dev/ttyACM_UBLOX`.
 - Reload the udev rules with: `# udevadm control --reload`.
 - I also used the commands `$ udevadm trigger` adn `$ udevadm test` but I do not know how they are supposed to be used.