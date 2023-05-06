"""Main config module."""

from dynaconf import Dynaconf

# Objeto único que irá ler as configurações do programa.
settings = Dynaconf(
    envvar_prefix="MYAPP",  # Setar o nome de seu aplicativo
    settings_files=['settings.toml'],  # Arquivo de configuração (.env, .toml, .yaml, .json, .py)
)
