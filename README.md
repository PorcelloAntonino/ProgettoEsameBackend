"# ProgettoEsame" 

comandi python

-alembic:

alembic  revision --autogenerate -m ''

'' commento

il comando serve per creare le migration per il db

DOPO aver fatto la migration allora 

alembic upgrade head 

in caso voglio tornare indietro 

alembic downgrade -1     

-pip 

per generare il requirements

pip freeze > requirements.txt

per l intsallazione di paccchetti 

pip install 'nome pacchetto'

-VENV
in caso non attivo il venv allora 

.\.venv\Scripts\activate             