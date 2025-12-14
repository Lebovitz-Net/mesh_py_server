"""
General utilities for the server.
Includes timestamp normalization helpers.
"""
# src/meshtastic/utils/packet_utils.py

import binascii
import asyncio

# Example: repeaterContacts could be a dict {name: {"publicKey": "..."}}
repeaterContacts = {}

def get_hex_key(name: str):
    """
    Look up a contact by name and return its publicKey as bytes.
    """
    try:
        key = repeaterContacts[name]["publicKey"]
        return get_hex_from_key(key)
    except Exception:
        return None

def get_hex_from_key(key: str):
    """
    Convert a hex string into bytes.
    """
    if isinstance(key, str):
        return bytes.fromhex(key)
    return None

def get_text_from_key(key: bytes):
    """
    Convert bytes into an uppercase hex string.
    """
    if isinstance(key, (bytes, bytearray)):
        return binascii.hexlify(key).decode("utf-8").upper()
    return None

def get_public_key_value(key: bytes):
    """
    Sum all byte values in the key.
    """
    if isinstance(key, (bytes, bytearray)):
        return sum(key)
    return None

def hash_public_key(public_key: bytes) -> int:
    """
    Compute FNV-1a 32-bit hash of a public key (bytes).
    Equivalent to the JS hashPublicKey function.
    """
    # FNV offset basis and prime
    hash_val = 0x811c9dc5
    prime = 0x01000193

    for byte in public_key:
        hash_val ^= byte
        hash_val = (hash_val * prime) & 0xffffffff  # keep in 32-bit unsigned range

    return hash_val


def normalize_in(time: int | float) -> int | float:
    """
    Normalize incoming time values.
    If time < 2_000_000_000, treat as seconds and convert to ms.
    Otherwise assume already ms.
    """
    return time * 1000 if time < 2_000_000_000 else time

def normalize_out(time: int | float) -> int | float:
    """
    Normalize outgoing time values.
    If time < 2_000_000_000, assume already seconds.
    Otherwise convert ms to seconds.
    """
    return time if time < 2_000_000_000 else time / 1000

def normalize_channel_key(key: bytes | None, length: int = 32) -> bytes:
    """
    Normalize a channel key for Meshcore/Meshtastic.
    - If key is None or empty (b""), return all zeros of the given length.
    - Otherwise, pad or truncate the key to the fixed length.
    """
    if not key:  # None or b""
        return bytes(length)  # all zeros
    return key.ljust(length, b"\x00")[:length]
