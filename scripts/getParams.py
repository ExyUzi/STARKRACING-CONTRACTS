
MAX_LEN_FELT = 31


def str_to_felt(text):
    if len(text) > MAX_LEN_FELT:
        raise Exception("Text length too long to convert to felt.")

    return int.from_bytes(text.encode(), "big")


def felt_to_str(felt):
    length = (felt.bit_length() + 7) // 8
    return felt.to_bytes(length, byteorder="big").decode("utf-8")


def str_to_felt_array(text):
    return [str_to_felt(text[i:i+MAX_LEN_FELT]) for i in range(0, len(text), MAX_LEN_FELT)]


def uint256_to_int(uint256):
    return uint256[0] + uint256[1]*2**128


def uint256(val):
    return (val & 2**128-1, (val & (2**256-2**128)) >> 128)


def hex_to_felt(val):
    return int(val, 16)

name = str_to_felt("StarkRacing")
symbol = str_to_felt("RACING")
owner = hex_to_felt("0x04a71727f73352b28C2D2f29fD8038d01b0E14b66660e8fa9b08535535bd7F3e")
tokenuri = str_to_felt_array("https://gateway.pinata.cloud/ipfs/QmNdYYTVBDguR4Aj3osHxJNTthR22Tw2AubN24pLbsfGpw/")
end_uri = str_to_felt(".json") 
lengthtokenuri = len(tokenuri)

params = [
        name, 
        symbol, 
        owner,
        lengthtokenuri, 
        *tokenuri, 
        end_uri,
    ]
    
print(params)
