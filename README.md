# Pedidos


## Como Desenvolver?
1. Clone o repositório.
2. Crie um virtualenv com Python 3.9
3. Ative o virutalenv.
4. Instale as dependências.
5. Configure a instância com o .env
6. Execute os testes

````console
git clone https://github.com/Sidneyasjr/pedidos.git
cd wttd
python -m venv .venv
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env.sample .env
python manage.py test
````

## Como fazer o deploy
1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Define uma SECRET_KEY segura para instância.
4. Degina DEBUG=False
5. Configure o serviço de email.
6. Envie o código para o heroku


````console
heroku create minhainstancia
heroku config:push
heroku config:set SECRET_KEY=`python contrib/secret_gen.py`
heroku config:set DEBUG=False
# configura o email
git push heroku master --force
````


