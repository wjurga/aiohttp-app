import json
from aiohttp import web

from models import Pet
from database import db_session


class Pets:
    async def pets_list(self, request):
        pet_type = request.query.get('type')
        shelterId = request.query.get('shelterId')
        pets = db_session.query(Pet)

        if pet_type is not None:
            pets = pets.filter(Pet.type == pet_type)
        if shelterId is not None:
            pets = pets.filter(Pet.shelterId == shelterId)

        pets = pets.all()

        data = {'pets': [pet.json() for pet in pets]}
        body = json.dumps(data).encode('utf-8')

        return web.Response(status=200,
                            body=body,
                            content_type='application/json')

    async def pet_info(self, request):
        id = request.match_info.get('id')
        pet = db_session.query(Pet).filter(Pet.id == id).first()

        if pet is None:
            message = {'message': 'Pet not found.'}
            return web.Response(status=404,
                                body=json.dumps(message).encode('utf-8'),
                                content_type='application/json')
        else:
            return web.Response(status=200,
                                body=json.dumps(pet.json()).encode('utf-8'),
                                content_type='application/json')

    async def add_pet(self, request):
        data = await request.json()
        pet = Pet(**data)
        pet.save_to_db()
        return web.Response(status=201,
                            body=json.dumps(pet.json()).encode('utf-8'),
                            content_type='application/json')

    async def update_pet(self, request):
        data = await request.json()
        pet = db_session.query(Pet).filter(Pet.id == data['id']).first()

        pet.name = data['name']
        pet.type = data['type']
        pet.available = data['available']
        pet.addedAt = data['addedAt']
        pet.adoptedAt = data['adoptedAt']
        pet.description = data['description']
        pet.shelterId = data['shelterId']

        pet.save_to_db()

        return web.Response(status=201,
                            body=json.dumps(pet.json()).encode('utf-8'),
                            content_type='application/json')

    async def delete_pet(self, request):
        id = request.match_info.get('id')
        pet = db_session.query(Pet).filter(Pet.id == id).first()
        if pet is None:
            message = {'message': 'Pet not found.'}
            return web.Response(status=404,
                                body=json.dumps(message).encode('utf-8'),
                                content_type='application/json')
        else:
            pet.delete_from_db()
        message = {'message': 'Pet was deleted.'}
        return web.Response(status=200,
                            body=json.dumps(message).encode('utf-8'),
                            content_type='application/json')
