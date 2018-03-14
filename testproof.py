import hashlib
from uuid import uuid4

def valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
#    print("proof: %d guess: %s hash: %s") % (proof,guess,guess_hash)
    print("proof: ",str(proof),"guess: ",str(guess_hash))


    return guess_hash[:4] == "0000"

proof = 0
last_proof = 0
while valid_proof(last_proof, proof) is False:
    proof += 1


