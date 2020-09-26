"""
@author: Arkan M. Gerges<arkan.m.gerges@gmail.com>
"""
import json
import traceback
from logging import Logger
from typing import List
from uuid import uuid4

from fastapi import APIRouter, Depends, Query, Body

import src.portadapter.api.rest.AppDi as AppDi
from src.portadapter.api.rest.model.User import User
from src.portadapter.api.rest.model.request.User import User
from src.portadapter.api.rest.router.v1.auth import CustomHttpBearer
from src.portadapter.messaging.common.SimpleProducer import SimpleProducer
from src.portadapter.messaging.common.model.Command import Command
from src.portadapter.messaging.common.model.CommandConstant import CommandConstant
from src.resource.logging.logger import logger

router = APIRouter()


@router.get(path="/", summary='Get all users', response_model=List[User])
async def getAllUsers(*, _=Depends(CustomHttpBearer())):
    """Return all users
    """
    try:
        return []
    except:
        logger = AppDi.instance.get(Logger)
        logger.warning(traceback.format_exc())
        return []


@router.get(path="/{userId}/", summary='Get user',
            response_model=User)
async def getUser(*, userId: str = Query(...,
                                         description='User id that is used to fetch user data'),
                  _=Depends(CustomHttpBearer())):
    """Get a User by id
    """
    try:
        return User()
    except:
        logger.warning(traceback.format_exc())
        return User()


def _customFunc(args):
    pass


@router.post("/create", summary='Create a new user')
async def create(*, title: str = Body(..., description='Title of the user', embed=True),
                 _=Depends(CustomHttpBearer()),
                 ):
    # ), backgroundTasks: BackgroundTasks):
    """Call async
    """
    # backgroundTasks.add_task(_customFunc, args)

    abcd = [
        {
            "_id": "5f6f052f2443819725e18359",
            "index": 0,
            "guid": "dbc94950-fa9b-4150-984c-364078014147",
            "isActive": False,
            "balance": "$1,029.24",
            "picture": "http://placehold.it/32x32",
            "age": 24,
            "eyeColor": "blue",
            "name": {
                "first": "Glenn",
                "last": "Cortez"
            },
            "company": "ENERSOL",
            "email": "glenn.cortez@enersol.biz",
            "phone": "+1 (990) 446-3238",
            "address": "953 Albee Square, Slovan, Arizona, 675",
            "about": "In enim veniam consequat officia Lorem sint nostrud. Elit pariatur tempor dolore do anim consequat elit ipsum commodo quis exercitation irure culpa irure. Do quis laborum occaecat laborum. Occaecat velit elit adipisicing esse nostrud qui elit.",
            "registered": "Wednesday, November 25, 2015 4:06 PM",
            "latitude": "77.099585",
            "longitude": "-100.664477",
            "tags": [
                "amet",
                "minim",
                "excepteur",
                "ex",
                "voluptate"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Lilia Farley"
                },
                {
                    "id": 1,
                    "name": "Katheryn Logan"
                },
                {
                    "id": 2,
                    "name": "Sallie Mays"
                }
            ],
            "greeting": "Hello, Glenn! You have 10 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "5f6f052f3f7491cbaec9d803",
            "index": 1,
            "guid": "ed0dd651-f804-4ae7-96ee-8348551d3d1c",
            "isActive": False,
            "balance": "$3,567.49",
            "picture": "http://placehold.it/32x32",
            "age": 23,
            "eyeColor": "brown",
            "name": {
                "first": "Zimmerman",
                "last": "Bridges"
            },
            "company": "PANZENT",
            "email": "zimmerman.bridges@panzent.ca",
            "phone": "+1 (876) 436-3520",
            "address": "140 Williams Avenue, Jenkinsville, Nevada, 5244",
            "about": "Incididunt cillum ea excepteur officia aliqua eiusmod ipsum reprehenderit ad incididunt aute in commodo anim. Qui cillum adipisicing irure duis commodo dolor sunt veniam amet. Consequat nisi ea et culpa commodo id id officia sint pariatur ea nisi minim sint. Excepteur anim ullamco non sit duis dolor non aliqua pariatur labore. Anim ea exercitation deserunt nisi labore cupidatat voluptate minim exercitation in incididunt qui do.",
            "registered": "Tuesday, November 17, 2015 6:05 AM",
            "latitude": "-23.106315",
            "longitude": "-125.254612",
            "tags": [
                "incididunt",
                "aliqua",
                "ullamco",
                "exercitation",
                "voluptate"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Conrad Morris"
                },
                {
                    "id": 1,
                    "name": "Gregory Lyons"
                },
                {
                    "id": 2,
                    "name": "Bernadette Duffy"
                }
            ],
            "greeting": "Hello, Zimmerman! You have 8 unread messages.",
            "favoriteFruit": "banana"
        },
        {
            "_id": "5f6f052f9c6542013aa6d1b9",
            "index": 2,
            "guid": "2464ae65-fabc-4d3e-9b0a-d29805265ada",
            "isActive": True,
            "balance": "$2,186.06",
            "picture": "http://placehold.it/32x32",
            "age": 40,
            "eyeColor": "green",
            "name": {
                "first": "Caroline",
                "last": "Meyer"
            },
            "company": "TEMORAK",
            "email": "caroline.meyer@temorak.com",
            "phone": "+1 (917) 480-2559",
            "address": "263 Erskine Loop, Bynum, Iowa, 9053",
            "about": "Irure officia est velit elit ea eu ad est esse ex dolor. Dolor qui pariatur est velit ea consequat amet eiusmod enim. Consectetur enim nostrud dolor exercitation cupidatat. Dolore Lorem quis incididunt est veniam nostrud deserunt. Esse consequat adipisicing ex adipisicing.",
            "registered": "Tuesday, May 29, 2018 5:43 PM",
            "latitude": "-3.879958",
            "longitude": "43.486942",
            "tags": [
                "nisi",
                "amet",
                "nisi",
                "reprehenderit",
                "ullamco"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Loretta Tyson"
                },
                {
                    "id": 1,
                    "name": "Parks Brewer"
                },
                {
                    "id": 2,
                    "name": "Scott Duke"
                }
            ],
            "greeting": "Hello, Caroline! You have 6 unread messages.",
            "favoriteFruit": "banana"
        },
        {
            "_id": "5f6f052fe2ce69ce097b1063",
            "index": 3,
            "guid": "90d0ec4e-d105-4696-b036-250c3e922ab6",
            "isActive": True,
            "balance": "$1,548.39",
            "picture": "http://placehold.it/32x32",
            "age": 29,
            "eyeColor": "brown",
            "name": {
                "first": "Della",
                "last": "Hatfield"
            },
            "company": "NETAGY",
            "email": "della.hatfield@netagy.biz",
            "phone": "+1 (828) 468-3733",
            "address": "803 Friel Place, Williston, Georgia, 4187",
            "about": "Consequat consectetur proident ex esse occaecat officia eu. Quis aute sint ipsum ea irure laboris ex. Excepteur laborum consectetur elit ad laboris elit aliqua. Eiusmod Lorem nostrud culpa aliqua proident esse sit officia esse consequat do. Elit ea mollit aute laborum exercitation. Ea ipsum mollit ipsum occaecat consectetur adipisicing duis cillum.",
            "registered": "Wednesday, April 13, 2016 7:26 AM",
            "latitude": "-78.911602",
            "longitude": "62.487913",
            "tags": [
                "id",
                "magna",
                "eu",
                "duis",
                "enim"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Vaughan Hoover"
                },
                {
                    "id": 1,
                    "name": "Vazquez Cunningham"
                },
                {
                    "id": 2,
                    "name": "Beverly Francis"
                }
            ],
            "greeting": "Hello, Della! You have 10 unread messages.",
            "favoriteFruit": "banana"
        },
        {
            "_id": "5f6f052fbc5b21811136a79f",
            "index": 4,
            "guid": "ebfc4163-2d15-4c95-85e4-26a84456eb1e",
            "isActive": False,
            "balance": "$1,821.12",
            "picture": "http://placehold.it/32x32",
            "age": 26,
            "eyeColor": "green",
            "name": {
                "first": "Lyons",
                "last": "Patrick"
            },
            "company": "ECSTASIA",
            "email": "lyons.patrick@ecstasia.name",
            "phone": "+1 (943) 488-3171",
            "address": "642 Sullivan Place, Greensburg, Connecticut, 3147",
            "about": "Ut nulla laborum duis nostrud est amet qui excepteur reprehenderit fugiat mollit laborum qui aliqua. Nostrud ullamco fugiat irure est culpa velit. Reprehenderit deserunt exercitation sunt cupidatat nostrud nisi cupidatat dolor ea fugiat.",
            "registered": "Wednesday, March 2, 2016 2:40 PM",
            "latitude": "13.252117",
            "longitude": "112.805324",
            "tags": [
                "Lorem",
                "id",
                "occaecat",
                "non",
                "enim"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Millicent Roy"
                },
                {
                    "id": 1,
                    "name": "Davenport Huffman"
                },
                {
                    "id": 2,
                    "name": "Fowler Santos"
                }
            ],
            "greeting": "Hello, Lyons! You have 6 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "5f6f052f338d713b20bb2829",
            "index": 5,
            "guid": "529b29f7-e49e-4e5a-9e7f-6522bfa97ae8",
            "isActive": False,
            "balance": "$3,943.59",
            "picture": "http://placehold.it/32x32",
            "age": 38,
            "eyeColor": "green",
            "name": {
                "first": "Annette",
                "last": "Reid"
            },
            "company": "BOSTONIC",
            "email": "annette.reid@bostonic.us",
            "phone": "+1 (802) 502-3491",
            "address": "473 Boerum Street, Caln, New Jersey, 9139",
            "about": "Voluptate aute do eu est voluptate anim sit tempor officia ullamco do consequat. Eu anim mollit eu exercitation non sunt anim sunt commodo magna. Cillum est officia et minim adipisicing. Mollit pariatur do non irure occaecat nostrud.",
            "registered": "Saturday, November 26, 2016 4:01 PM",
            "latitude": "10.976326",
            "longitude": "4.866443",
            "tags": [
                "dolor",
                "elit",
                "dolor",
                "laborum",
                "sint"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "Molina Taylor"
                },
                {
                    "id": 1,
                    "name": "White Mcleod"
                },
                {
                    "id": 2,
                    "name": "Hopper Riddle"
                }
            ],
            "greeting": "Hello, Annette! You have 9 unread messages.",
            "favoriteFruit": "strawberry"
        },
        {
            "_id": "5f6f052f5e6504e735c9c8db",
            "index": 6,
            "guid": "47468ca4-7726-4acd-9dab-31a40cf771a5",
            "isActive": False,
            "balance": "$2,624.45",
            "picture": "http://placehold.it/32x32",
            "age": 34,
            "eyeColor": "blue",
            "name": {
                "first": "Kidd",
                "last": "Cardenas"
            },
            "company": "NETPLODE",
            "email": "kidd.cardenas@netplode.net",
            "phone": "+1 (813) 575-3141",
            "address": "707 Martense Street, Independence, Federated States Of Micronesia, 6729",
            "about": "Anim mollit sint ullamco proident fugiat aliquip reprehenderit ex esse cupidatat. Aute sunt id consequat laboris exercitation do non mollit proident amet nisi nostrud. Consequat velit ipsum et ea sit in cillum tempor exercitation. Nisi est incididunt enim duis. Adipisicing dolore enim aute sit ex qui minim labore pariatur nostrud nostrud. Pariatur id ea minim nostrud culpa. Irure aliquip eiusmod esse nulla pariatur qui.",
            "registered": "Thursday, August 3, 2017 9:16 PM",
            "latitude": "28.674017",
            "longitude": "29.9696",
            "tags": [
                "eiusmod",
                "amet",
                "laborum",
                "id",
                "cillum"
            ],
            "range": [
                0,
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9
            ],
            "friends": [
                {
                    "id": 0,
                    "name": "French Morrow"
                },
                {
                    "id": 1,
                    "name": "Gina Stuart"
                },
                {
                    "id": 2,
                    "name": "Baird Hoffman"
                }
            ],
            "greeting": "Hello, Kidd! You have 10 unread messages.",
            "favoriteFruit": "apple"
        }
    ]

    producer = AppDi.instance.get(SimpleProducer)
    producer.produce(obj=Command(id=str(uuid4()), name=CommandConstant.CREATE_USER.name, data=''),
                     schema=Command.get_schema())
