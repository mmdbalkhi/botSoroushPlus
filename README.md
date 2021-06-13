# botSoroushPlus

Soroush + bot with python

## how to run

To run bot in development mode; Just use steps below:

1. Install `python3`,  `virtualenv` in your system.
2. Clone the project `https://github.com/KomeilParseh/botSoroushPlus.git`.
3. Make development environment ready using commands below

  

``` bash
git clone https://github.com/KomeilParseh/botSoroushPlus.git && cd botSoroushPlus
```

```bash
virtualenv -p python3 venv  # Create virtualenv named build
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
mv  config.py.sample config.py
```

4. edit ``bot.py`` and add your token:

``

``` python

bot_token = "your token"

```

power by [goodreads.com](https://www.goodreads.com/)
