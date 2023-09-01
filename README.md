# EventIF

Sistema do evento do IF que está sendo desenvolvido na disciplina de Desenvolvimento de Sistemas 2.

## Como desenvolver

1. Clone o repositório
2. crie um virtualenv com python 3.10 ou superior
3. Ative o virtualenv
4. Instale as dependências
5. Configure a instância com o arquivo .env
6. Execute os testes

```console
git clone git@github.com:clebersfonseca/eventif
cd eventif
python -m venv .eventif
source .eventif/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage.py test
```