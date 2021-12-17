from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine

from app.db.schema import goods_table
from app.utils.pg import PG_URL


class NotFound(Exception):
    pass


class Database:
    def __init__(self):
        self.engine = create_async_engine('postgresql+asyncpg' + PG_URL)

    async def get_good(self, good_id: int) -> dict:
        async with self.engine.connect() as conn:
            result = await conn.execute(
                select(goods_table).where(goods_table.c.id == good_id)
            )

        return good_to_json(result.fetchone())

    async def get_all_goods(self) -> List[dict]:
        async with self.engine.connect() as conn:
            result = await conn.execute(
                select(goods_table)
            )

        return list(map(good_to_json, result.fetchall()))

    async def create_good(self, name: str, description: str, image: str,
                          price: int, active: bool, count: int) -> int:
        async with self.engine.begin() as conn:
            result = await conn.execute(
                goods_table.insert().returning(goods_table.c.id).values(
                    {
                        'name': name,
                        'description': description,
                        'image': image,
                        'price': price,
                        'active': active,
                        'count': count
                    }
                )
            )
            return result.fetchone()[0]

    async def ping_db(self):
        async with self.engine.connect() as conn:
            try:
                await conn.execute(goods_table.select().limit(1))
            except Exception as e:
                raise ConnectionError(e)

    async def update_good(self, good_id: int, name: str, description: str,
                          image: str, price: int, active: bool,
                          count: int):
        async with self.engine.begin() as conn:
            result = await conn.execute(
                select(goods_table).where(goods_table.c.id == good_id)
            )

            if not result.fetchone():
                raise NotFound()

            await conn.execute(
                goods_table.update().where(goods_table.c.id == good_id).values(
                    {
                        'name': name,
                        'description': description,
                        'image': image,
                        'price': price,
                        'active': active,
                        'count': count
                    }
                )
            )

    async def delete_good(self, good_id: int):
        async with self.engine.begin() as conn:
            result = await conn.execute(
                select(goods_table).where(goods_table.c.id == good_id)
            )

            if not result.fetchone():
                raise NotFound()

            await conn.execute(
                goods_table.delete().where(goods_table.c.id == good_id))


def good_to_json(obj):
    return {
        "id": obj[0],
        "name": obj[1],
        "description": obj[2],
        "image": obj[3],
        "price": obj[4],
        "active": obj[5],
        "count": obj[6],
    }
