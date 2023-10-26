from app.models import Place
from app.repositories import PlaceRepository
from core.controller import BaseController
from core.database.transactional import Propagation, Transactional
from datetime import datetime
import numpy as np

class PlaceController(BaseController[Place]):
    """Place controller."""

    def __init__(self, place_repository: PlaceRepository):
        super().__init__(model=Place, repository=place_repository)
        self.place_repository = place_repository

    async def get_by_place_name(self, place_name: str | None=None) -> list[Place]:
        """
        Returns a list of places based on place name.

        :param author_id: The author id.
        :return: A list of places.
        """
        return await self.place_repository.get_by_place_name(place_name)
    

    async def get_all_places(self)-> list[Place]:
        return self.place_repository.get_all_places()
    

    async def get_places(self,limit:int) -> list[Place]:
        return self.place_repository.get_places(limit=limit)
    

    async def get_place_by_lat_lng(self,lat:float | None = None,lng:float | None=None)->list[Place]:
        if lat is None or lng is None:
            return self.get_place()
        else:
            places = self.get_all_place()
            lats = [l for l in places.lat]
            lngs = [l for l in places.lng]
            distances = []
            for la, lo in zip(lats, lngs):
                d= np.sqrt((la-lat)**2 + (lo-lat)**2)
                distances.append(d)
            sort_index = sorted(enumerate(distances), key=lambda x :x[1])
            index = [i for i,x in enumerate(sort_index)]
            loc = [places[i] for i in index]
            return loc
        
    async def get_by_merchant_id(self, merchant_id: int) -> list[Place]:
        """
        Returns a list of tasks based on author_id.

        :param author_id: The author id.
        :return: A list of tasks.
        """

        return await self.place_repository.get_by_merchant_id(merchant_id)

    