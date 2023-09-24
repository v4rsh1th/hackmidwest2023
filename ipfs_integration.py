import requests
import json

api_key = "0ee8f60cc5e859ca6872"
api_secret = "0c8307b834fba3fe8713c25c869775438b5b70185e6045a2215c441a70d79877"

def upload_to_ipfs(file_path):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    
    headers = {
        "Content-Type": "multipart/form-data",
        "pinata_api_key": api_key,
        "pinata_secret_api_key": api_secret,
    }

    files = {
        "file": (file_path, open(file_path, "rb")),
    }

    response = requests.post(url, headers=headers, files=files)
    
    if response.status_code == 200:
        result = json.loads(response.text)
        return result.get("IpfsHash")
    else:
        print("Error uploading to IPFS:", response.status_code, response.text)
        return None

# Example usage:
# ipfs_hash = upload_to_ipfs("path/to/your/file.txt")
# if ipfs_hash:
#     print("File uploaded to IPFS with hash:", ipfs_hash)
