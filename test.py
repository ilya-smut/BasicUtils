import encoder, extended_euclidean_find_inverse, gcd

print(gcd.gcd(77, 33))
print(encoder.b64_e('Hello, I am base64 encoded'))

inverse = extended_euclidean_find_inverse.findModInverse(17, 26)
print(17, inverse)
print((((17*8) % 26)*inverse)%26)