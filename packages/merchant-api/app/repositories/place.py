from sqlalchemy import Select
from sqlalchemy.orm import joinedload

from app.models import Place
from core.repository import BaseRepository


class PlaceRepository(BaseRepository[Place]):
    """
    Place repository provides all the database operations for the Place model.
    """

    async def get_places(self, limit: int=10, join_: set[str] | None = None,skip: int=0) -> list[Place]:
        """
        Get outlets with limit, by default 10 outlets
        :param limit: Limit number of outlets
        :return: list of outlets with limit
        """
        query = await self._query(join_)
        query = await self.get_all(query,skip, limit)
        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)

    async def get_by_place_name(
        self, name: str | None=None, join_: set[str] | None = None
    ) -> list[Place]:
        """
        Get all outlet by outlet name.

        :param author_id: The outlet name to match.
        :param join_: The joins to make.
        :return: A list of outlets.
        """
        query = await self._query(join_)
        query = await self._get_by(query, "name", name)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)
    
    async def get_all_places(self, join_: set[str] | None = None
                                     ) -> list[Place]:
        """
        Get all outlets

        :param join_: The joins to make.
        :return: all outlets.
        """
        query = await self._query(join_)
        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)
       
    async def get_by_merchant_id(
        self, merchant_id: int, join_: set[str] | None = None
    ) -> list[Place]:
        """
        Get all tasks by author id.

        :param author_id: The author id to match.
        :param join_: The joins to make.
        :return: A list of tasks.
        """
        query = self._query()
        query = await self._get_by(query, "merchant_id", merchant_id)

        if join_ is not None:
            return await self.all_unique(query)

        return await self._all(query)
    