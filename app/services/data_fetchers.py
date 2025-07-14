import aiohttp
import os
from typing import Dict, Any

class BlockchainDataFetcher:
    def __init__(self):
        self.base_urls = {
            'ethereum': f"https://api.etherscan.io/api?apikey={os.getenv('ETHERSCAN_API_KEY')}",
            'polygon': f"https://api.polygonscan.com/api?apikey={os.getenv('POLYGONSCAN_API_KEY')}",
            'arbitrum': f"https://api.arbiscan.io/api?apikey={os.getenv('ARBISCAN_API_KEY')}"
        }
    
    async def fetch_contract_events(self, network: str, address: str):
        async with aiohttp.ClientSession() as session:
            url = f"{self.base_urls[network]}&module=logs&action=getLogs&address={address}"
            async with session.get(url) as response:
                return await response.json()