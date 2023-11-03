from fastapi import FastAPI
from models.cosmetic import Cosmetic
from services.cosmetics_access_service import get_all_cosmetics_registered, \
                                            get_all_properties_registered, \
                                            get_all_cosmetics_expired, \
                                            get_cosmetic_by_name, update_cosmetic, \
                                            create_cosmetic, \
                                            create_list_of_cosmetics, \
                                            delete_cosmetic_by_name, \
                                            search_cosmetics_per_property, \
                                            search_cosmetics_per_family, \
                                            search_cosmetics_per_family_and_properties

app = FastAPI()

@app.get('/all/expired')
async def get_all_cosmetics_expired():
    cosmeticsList = get_all_cosmetics_expired()
    return cosmeticsList

@app.get('/all/properties')
async def get_all_properties():
    propertiesList = get_all_properties_registered()
    return propertiesList 

@app.get("/all")
async def get_all_cosmetics():
    cosmeticsList = get_all_cosmetics_registered()
    return cosmeticsList

@app.get('/cosmetic/{name}')
async def get_cosmetic_by_name(name: str):
    cosmetic = get_cosmetic_by_name(name)
    return cosmetic

@app.post("/cosmetic/{name}")
async def update_cosmetic(name: str, cosmetic: Cosmetic):
    success = update_cosmetic(name, cosmetic)

@app.post("/cosmetic/")
async def create_cosmetic(cosmetic: Cosmetic):
    success = create_cosmetic(cosmetic)

@app.post("/cosmetic/")
async def create_cosmetics(cosmetics: list<Cosmetic>):
    success = create_list_of_cosmetics(cosmetics)

@app.delete("/cosmetic/{name}")
async def delete_cosmetic_by_name(name: str):
    success = delete_cosmetic_by_name(name)

@app.post('/cosmetics/properties')
async def get_cosmetics_per_properties(properties: list<str>):
    cosmeticsList = search_cosmetics_per_properties(properties)
    return cosmeticsList

@app.get('/cosmetics/family/{family}')
async def get_cosmetics_per_family(family: str):
    cosmeticsList = search_cosmetics_per_family(family)
    return cosmeticsList

@app.get('/cosmetics/properties/family/{family}')
async def get_cosmetics_per_family_and_properties(family: str, properties: list<str>):
    cosmeticsList = search_cosmetics_per_family_and_properties(family, properties)
    return cosmeticsList