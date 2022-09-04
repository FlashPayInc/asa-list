#!/usr/bin/env python3
from pathlib import Path
from typing import Dict, List, Union

import requests
from algosdk.v2client.indexer import IndexerClient
from decouple import config
import cloudinary.uploader

ROOT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = ROOT_DIR / 'assets'
NETWORK = config('NETWORK')
API_ENDPOINT = config('API_ENDPOINT')
API_KEY = config('API_KEY')

if NETWORK == 'testnet':
    INDEXER_ADDRESS = 'https://algoindexer.testnet.algoexplorerapi.io'
elif NETWORK == 'mainnet':
    INDEXER_ADDRESS = 'https://algoindexer.algoexplorerapi.io'
else:
    raise ValueError('Invalid NETWORK env')
INDEXER_CLIENT = IndexerClient('lorem', INDEXER_ADDRESS, {'X-API-Key': 'lorem'})


def get_last_updated_timestamp() -> int:
    """Retrieve the last time the assets were synced with the database."""
    info_path = ROOT_DIR / 'info.txt'
    with open(info_path, mode='r') as file:
        last_update_timestamp_line = file.readline()
        return int(last_update_timestamp_line.split('=')[-1].strip())


def get_assets_info_to_sync() -> List[Dict[str, str]]:
    """Retrieve assets information to sync since last sync."""
    assets_info = []
    last_updated_ts = get_last_updated_timestamp()

    for asset in ASSETS_DIR.iterdir():
        if asset.stat().st_ctime > last_updated_ts:
            asset_name, asa_id = asset.name.split('-')
            asset_info = retrieve_asset_info_from_blockchain(int(asa_id))
            asset_image_url = upload_asset_image(
                path=asset / 'icon.svg',
                asa_id=asset_info['asa_id'],
            )
            asset_info['image_url'] = asset_image_url
            assets_info.append(asset_info)

    return assets_info


def retrieve_asset_info_from_blockchain(asa_id: int) -> Dict[str, Union[str, int]]:
    """Retrieves information about an ASA from the blockchain."""
    # can only be Algorand native token.
    if asa_id == 0 or asa_id == 1:
        return {
            'long_name': 'Algorand',
            'short_name': 'ALGO',
            'decimals': 6,
            'asa_id': asa_id,
        }

    asset_info = INDEXER_CLIENT.asset_info(asa_id)
    return {
        'long_name': asset_info['asset']['params']['name'],
        'short_name': asset_info['asset']['params']['unit-name'],
        'decimals': asset_info['asset']['params']['decimals'],
        'asa_id': asset_info['asset']['index'],
        'network': NETWORK,
    }


def upload_asset_image(path: Path, asa_id: int) -> str:
    """Uploads asset's image to Cloudinary and returns the URL."""
    url = cloudinary.uploader.upload(
        file=str(path),
        public_id=str(asa_id),
        folder='assets/',
    )
    return url['secure_url']


def upload_assets_to_db(assets: List[Dict[str, Union[str, int]]]) -> None:
    """Upload the assets info to the database."""
    print(f'The current network is: {NETWORK} with assets info -> \n{str(assets)}')
    res = requests.post(
        url=API_ENDPOINT,
        json=assets,
        headers={'Authorization': f'Token {API_KEY}'},
    )
    assert res.status_code == 201


def main() -> None:
    """Entrypoint"""
    assets_info = get_assets_info_to_sync()
    upload_assets_to_db(assets=assets_info)


main()
