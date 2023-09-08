# Stats website
The website displays MLB news, standings, team rosters and player statistics.

See the live demo at [https://mlb.softifacts.com](https://mlb.softifacts.com)

## Homepage 
Show divisional standings and recent news stories.
<img src="https://github.com/cd155/assignment/assets/16947266/997b8b36-ea1f-4380-b743-fb155a99e3f6" alt="" width="600"/>

## Team page
Show current roster and player stats
<img src="https://github.com/cd155/assignment/assets/16947266/c780a7a8-7509-450c-98a5-b8daa775d575" alt="" width="600"/>

## Filter for different players
Show players based on their roles (eg: hitters, pitchers)
<img src="https://github.com/cd155/assignment/assets/16947266/f5d91458-db82-491f-999d-5ff62d4c25b4" alt="" width="600"/>

## Player page
Show player history

<img src="https://github.com/cd155/assignment/assets/16947266/f320dda7-2b80-4529-8fad-0d88fedb6050" alt="" width="600"/>

## Leaderboards
Show current statistical leaders (eg: HR, OPS, ERA, Strikeouts)
<img src="https://github.com/cd155/assignment/assets/16947266/72209fe7-0deb-494d-b19e-f4c616494bb7" alt="" width="600"/>

# How to run this app
python virtual environment

1. Clone the repository, then go to the root directory
```bash
cd assignment
```
2. Run those commands
```bash
# Create a virtual environment folder
python -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# install all required python packages
pip install -r requirements.txt
```
3. Run the app in the local hoster

`cd blueJays` make sure you are in the project folder
```bash
python manage.py runserver
```

(If you use nixos, you can use `nix-shell shell.nix`)
