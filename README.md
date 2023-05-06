# Introdução ao Dynaconf

Recentemente eu me deparei com a necessidade de acessar as variáveis de ambiente, as configurações sensíveis do projeto.
Eu já conhecia o python-decouple, python-dotenv entre outras bibliotecas que fazem esse trabalho, mas eu queria algo mais completo, que me permitisse fazer o deploy da aplicação em diferente ambientes, como por exemplo, local, desenvolvimento, homologação e produção.

Então eu encontrei o Dynaconf, uma biblioteca que faz exatamente isso, e muito mais.

## O que é o Dynaconf?

Segundo o próprio site..

> O dynaconf é um sistema de configuração em camadas para aplicativos Python. E é muito prático, fácil e inteligente.

Neste exemplo eu vou mostrar como usar o Dynaconf para acessar as variáveis de ambiente, sugiro que você leia a documentação oficial para conhecer todas as funcionalidades.

## Instalação

```bash
pip install dynaconf
```

## Configuração

Para configurar o Dynaconf, basta criar um arquivo chamado settings.toml na raiz do projeto, e adicionar as variáveis de ambiente que você deseja acessar.
Ou simplesmente executar o comando `dynaconf init` que ele vai criar o arquivo settings.toml para você.

```bash
dynaconf init
```

Dentro do arquivo `config.py' ja é instanciado o Dynaconf, na variável settings.

```python
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="MYAPP",  
    settings_files=['settings.toml'],  
)
```

O diferencial é que pode ler as configurações do projeto, variáveis de ambiente dentro de arquivos como (.env, .toml, .yaml, .json, .py).

## Ambientes de trabalho

Umas das coisas do Dynaconf que eu mais gostei, é a possibilidade de trabalhar com diferentes ambientes, como por exemplo, local, desenvolvimento, homologação e produção.
Sendo possível ter configurações específicas para cada ambientes de development, staging, testing e production.

Ah! Você também pode ter mais de um arquivo de configuração, por exemplo, um arquivo para as configurações do banco de dados, outro para as configurações do servidor de e-mail, etc.


