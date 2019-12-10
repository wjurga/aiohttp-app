import json
from aiohttp import web

from models import Shelter, Pet
from database import db_session


class Shelters:
    async def shelter_list(self, request):
        city = request.query.get('city')
        if city:
            shelters = db_session.query(Shelter).filter(Shelter.city == city)
        else:
            shelters = db_session.query(Shelter).all()

        data = {'shelters': [shelter.json() for shelter in shelters]}
        body = json.dumps(data).encode('utf-8')

        return web.Response(status=200,
                            body=body,
                            content_type='application/json')

    async def shelter_info(self, request):
        id = request.match_info.get('id')
        shelter = db_session.query(Shelter).filter(Shelter.id == id).first()
        if shelter:
            data = shelter.json()
            body = json.dumps(data).encode('utf-8')

            return web.Response(status=200,
                                body=body,
                                content_type='application/json')

        message = {'message': 'Shelter not found.'}
        return web.Response(status=404,
                            body=json.dumps(message).encode('utf-8'),
                            content_type='application/json')

    async def pet_list_in_shelter(self, request):
        pet_type = request.query.get('type')
        id = request.match_info.get('id')
        pets = db_session.query(Pet).filter(Pet.shelterId == id).all()

        if len(pets) > 0:
            if pet_type:
                pets = [pet for pet in pets if pet.type == pet_type]
            data = {'pets': [pet.json() for pet in pets]}
            body = json.dumps(data).encode('utf-8')

            return web.Response(status=200,
                                body=body,
                                content_type='application/json')

        message = {'message': 'Shelter not found.'}
        return web.Response(status=404,
                            body=json.dumps(message).encode('utf-8'),
                            content_type='application/json')

    async def add_shelter(self, request):
        data = await request.json()
        shelter = Shelter(**data)
        shelter.save_to_db()

        return web.Response(status=201,
                            body=json.dumps(shelter.json()).encode('utf-8'),
                            content_type='application/json')
