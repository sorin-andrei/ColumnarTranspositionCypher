# ColumnarTranspositionCypher
Python implementation of the columnar transposition cipher 

As described on Wikipedia:
https://en.wikipedia.org/wiki/Transposition_cipher
-----------------------------------

Plaintexts can be rearranged into a ciphertext using a key, scrambling the order of characters like the shuffled pieces of a jigsaw puzzle. The resulting message is hard to decipher without the key because there are many ways the characters can be arranged.

For example, the plaintext "THIS IS WIKIPEDIA" could be encrypted to "TWDIP SIHII IKASE". To decipher the encrypted message without the key, an attacker could try to guess possible words and phrases like DIATHESIS, DISSIPATE, WIDTH, etc., but it would take them some time to reconstruct the plaintext because there are many combinations of letters and words. By contrast, someone with the key could reconstruct the message easily:

------------------------------------
```
C I P H E R     Key
1 4 5 3 2 6     Sequence (key letters in alphabetical order)
T H I S I S     Plaintext
W I K I P E
D I A * * *

Ciphertext by column:
  #1 TWD, #2 IP, #3 SI, #4 HII, #5 IKA, #6 SE
Ciphertext in groups of 5 for readability:
  TWDIP SIHII IKASE
  ```
----------------------------------

Example Output
```
Text to encrypt: CYBERSECURITYGOOD.
Plaintext arranged into the grid:
[['C' 'E' 'Y']
['Y' 'C' 'G']
['B' 'U' 'O']
['E' 'R' 'O']
['R' 'I' 'D']
['S' 'T' '.']]
Key: CIPHER
Permutation: [0, 3, 4, 2, 1, 5]
Encrypted Result: CEYRIDEROYCGBUOST.
----------------
Text to decrypt: CEYRIDEROYCGBUOST.
Group size: 3
Crypted text arranged into the grid:
[['C' 'R' 'E' 'Y' 'B' 'S']
['E' 'I' 'R' 'C' 'U' 'T']
['Y' 'D' 'O' 'G' 'O' '.']]
Key: CIPHER
Key Permutation:[0, 3, 4, 2, 1, 5]
Decrypted Result: CYBERSECURITYGOOD
```
