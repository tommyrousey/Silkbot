# Silkbot

Do you have that one friend that really likes Hollow Knight. Are they waiting for Silksong to come out? Heckle them with this Discord bot.

# Installation

### Python
You should have `python3` installed, instruction can be found [here](https://realpython.com/installing-python/).

### Discord.py
Install `discord.py` with additional voice extensions, instructions can be found [here](https://discordpy.readthedocs.io/en/stable/intro.html#installing).

### Additional Linux Packages
Note that linux systems will need additional packages installed:
- libffi
- libnacl
- python3-dev

Debian example:
```bash
apt install libffi-dev libnacl-dev python3-dev
```

### Install Packages
```bash
pip3 install -r requirements.txt
```

### Tokens
This script expects to have a file named `.env` holding 2 vars

#### TOKEN
The `TOKEN` var is the discord bot token. This can be obtained through the Discord Developer Portal, instructions found [here](https://discord.com/developers/docs/intro#bots-and-apps).

#### YT_API_KEY
The `YT_API_KEY` var is the youtube API key. This can be obtained through GCP, instruction found [here](https://developers.google.com/youtube/v3/getting-started).

Example `.env` file:
```
TOKEN=thisisnotarealtoken
YT_API_KEY=thisisnotarealkey
```

# Run
```bash
python3 main.py
```

# Tips
### Customize to target your one friend who is desparate for Silksong to come out
Change the member name check on line 38 (Note this is their account name, not their server nickname):
```python
# check if ben
if member.name != "parasol24":
    return
```

### Detach to run constantly in the background
I recommend using `tmux` to just have the Python bot run in the background constantly to serve requests.

Starting up the tmux
```bash
tmux new -s silkbot
```

Detaching from the session:

Press `Crtl+b` then press `d`

Reconnect to session:
```bash
tmux attach -t silkbot
```
