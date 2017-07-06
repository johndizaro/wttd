#EVENTEX

Sistema de Eventos encomendado pela morena 

## COMO DESENVOLVER

1. Clone o repositorio
2. Crie um venv com python 3.5
3. Ative o virtualenv
4. Instale s dependencias
5. Configure as sinstancias com .en
6. Execute os testes.

```console
git clonegit@github.com:johndizaro/eventex.git wttd
cd wttd
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env
python manage test
```
## COMO FAZER UM DEPLOY

1. Crie uma instancia no Heroku
2. Envie as configuraçoes para o Heroku
3. Defina uma SECRE_KEY para a instancia
4. Defina DEBUG=False
5. Configure o servico de email
6. Envie o codigof para o Heroku

```console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=False
#Configuro of email
git push heroku master --force
```
# wttd
# wttd
