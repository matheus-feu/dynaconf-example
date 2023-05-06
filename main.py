"""
$ pip install dynaconf
$ dynaconf init
⚙️  Configuring your Dynaconf environment
------------------------------------------
🐍 The file 'config.py' was generated.
    on your code now use 'from config import settings'
    (you must have a config.py in your PYTHONPATH)

🎛️ .settings.toml created to hold your settings.

🔑 .secrets.toml created to hold your secrets.

🙈 the .secrets.toml is also included in `.gitignore`
  beware to not push your secrets to a public repo
  or use dynaconf builtin support for Vault Servers.

🎉 Dynaconf is configured! read more on https://dynaconf.com
   Use `dynaconf -i config.settings list` to see your settings
"""

from config import settings

url = f"{settings.protocol}://{settings.host}:{settings.port}"
print(url)

msg = settings.msg
print(msg)

