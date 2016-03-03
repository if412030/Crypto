import binascii

str_hex = "53616c616d2064616d616920646172692074616e616820746f6261202d2064656c"

hex_d = str_hex.decode("hex")

res_hex = binascii.b2a_base64(hex_d)

print res_hex

#conver base64 to see message
