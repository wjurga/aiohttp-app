from aiohttp import web

from resources.shelters import Shelters
from resources.pets import Pets
from database import init_db

init_db()
app = web.Application()

shelters = Shelters()
pets = Pets()

app.add_routes([web.get('/shelters', shelters.shelter_list),
                web.get('/shelters/{id}', shelters.shelter_info),
                web.get('/shelters/{id}/pets', shelters.pet_list_in_shelter),
                web.post('/shelters', shelters.add_shelter)])

app.add_routes([web.get('/pets', pets.pets_list),
                web.get('/pets/{id}', pets.pet_info),
                web.post('/pets', pets.add_pet),
                web.put('/pets', pets.update_pet),
                web.delete('/pets/{id}', pets.delete_pet)])

if __name__ == '__main__':
    web.run_app(app)
