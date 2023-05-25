import requests
from aiohttp import ClientSession
from ujson import dumps

async def main():
    async with ClientSession(
        base_url='https://mempool.space',
    ) as session:
        response = await session.get(
            url='/api/adress/1wiz18xYmhRX6xStj2b9t1rwWX4GKUgpv',
            params='address' "1wiz18xYmhRX6xStj2b9t1rwWX4GKUgpv",
                    chain_stats: {
                    funded_txo_count: 5,
                    funded_txo_sum: 15007599040,
                    spent_txo_count: 5,
                    spent_txo_sum: 15007599040,
                    tx_count: 7
                    },
                    mempool_stats: {
                         funded_txo_count: 0,
                         funded_txo_sum: 0,
                         spent_txo_count: 0,
                         spent_txo_sum: 0,
                        tx_count: 0
                    }
                 })
