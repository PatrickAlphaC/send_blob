import os

from dotenv import load_dotenv
from eth_abi import abi
from eth_utils import to_hex
from web3 import HTTPProvider, Web3

load_dotenv()


def send_blob():
    rpc_url = os.getenv("RPC_URL")
    private_key = os.getenv("ANVIL_PRIVATE_KEY")
    w3 = Web3(HTTPProvider(rpc_url))

    text = "<( o.O )>"
    encoded_text = abi.encode(["string"], [text])

    print("Text:", encoded_text)

    # Blob data must be comprised of 4096 32-byte field elements
    # So yeah, blobs must be pretty big
    BLOB_DATA = (b"\x00" * 32 * (4096 - len(encoded_text) // 32)) + encoded_text

    acct = w3.eth.account.from_key(private_key)

    tx = {
        "type": 3,
        "chainId": 31337,  # Anvil
        "from": acct.address,
        "to": "0x0000000000000000000000000000000000000000",
        "value": 0,
        "maxFeePerGas": 10**12,
        "maxPriorityFeePerGas": 10**12,
        "maxFeePerBlobGas": to_hex(10**12),
        "nonce": w3.eth.get_transaction_count(acct.address),
    }

    gas_estimate = w3.eth.estimate_gas(tx)
    tx["gas"] = gas_estimate

    signed = acct.sign_transaction(tx, blobs=[BLOB_DATA])

    print("Signed Transaction:", signed, "\n")

    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Tx receipt: {tx_receipt}")


def main() -> int:
    send_blob()
    return 0


if __name__ == "__main__":
    main()
