# Lists some tools to use for doing things with SSH

## SSH Config & Proxy Jump
Use the ssh config to streamline ssh-ing. The config file is `~/.ssh/config`. A simple entry looks like:
```bash
Host <COMPUTER-NAME>
    HostName <IP-ADDRESS> (or website)
    User <USER-NAME>
    Port <probably 22>
```
You can then get in with: `ssh <COMPUTER-NAME>`
To get into computers in ISEC you can use a proxy jump. An entry like this works for me.
```bash
Host ccs
    HostName login.ccs.neu.edu
    User <USERNAME>
    Port <22?>

Host <ISEC-TARGET-COMPUTER>
    HostName <IP-ADDRESS>
    User <USER-NAME>
    Port <22?>
    ProxyJump ccs
```
You can then get in with `ssh <ISEC-TARGET-COMPUTER>`

## Screen
Screen is useful for starting long tasks over ssh. For simple use you can start a screen session with:
```bash
screen 
```
The run whatever commands... and then close the screen with `ctrl` `A`+`D`. The session can be reopened with `screen -r`. End a screen session with `exit`, like closing an ssh connection.

### More Screen
You can use `Screen -S <NAME>` to make a named "screen session" (instead of numbered). This lets you restart it by name.
You can use `Screen -ls` to get a list of active "Screens" The output looks like:
```
There are screens on:
	804416.test	(05/21/2023 04:11:49 PM)	(Detached)
	804196.pts-7.cbox20	(05/21/2023 04:07:44 PM)	(Detached)
2 Sockets in /run/screen/S-colin.
```
Note, one of the above screens is named `test`. These can be restarted either using the number (pid): `screen -r 804416` or by name: `screen -r test`
For more, see <https://www.howtogeek.com/662422/how-to-use-linuxs-screen-command/>