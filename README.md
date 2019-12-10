# aiohttp app
1. mikroserwis wykonany w oparciu o aiohttp
2. automatyzacja w oparciu o Dockera
3. baza danych PostgreSQL

# Uruchomienie serwisu:

~~~~
docker-compose up -d db
docker-compose run --rm aiohttp-app python database.py
docker-compose up
~~~~

# Endpointy

- `'/pets'`
- `'/pets/<id>'`
- `'/shelters'`
- `'/shelters/<id>'`
- `'/shelters/<id>/pets'`


# Dalsze kroki:
1. wykonanie testów automatycznych