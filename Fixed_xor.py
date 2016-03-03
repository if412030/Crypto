#if412030
#tobatrack

str1 = "1c0111001f010100061a024b53535009181c"
str2 = "686974207468652062756c6c277320657965"
hsl = "746865206b696420646f6e277420706c6179"

def xor_hex(hex1, hex2):
	if len(hex1) != len(hex2):
		print "err hex"

	h_dec1 = hex1.decode("hex")
	h_dec2 = hex2.decode("hex")
	
	hasil = ""

	for i, j in zip(h_dec1, h_dec2):
		hasil = hasil + (chr(ord(i) ^ ord(j)))

	return hasil.encode("hex")

try:
	assert(xor_hex(str1, str2).strip() == hsl)
	print "sama"
except AssertionError:
	print "tidak sama"
