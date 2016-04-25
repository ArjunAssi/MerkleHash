# ------------------------------------------------------------
# AUTHOR : LEONIDAS
# DATE : 25th APRIL 2016
# DESCRIPTION : CLASS TO PROVIDE HASHING UTILS
#------------------------------------------------------------

import hashlib
import os
#------------------------------------------------------------
# Function to generate a list of sha1 digest for a huge file
# The function takes a file as input and then reads blocks
# from the file and generates a list of sha1 hashes
#------------------------------------------------------------
def generate_sha1_for_file(root_directory, file_name, block_size=2 ** 20):
    # Initialize the output hashList
    output_hash_list = []

    # Iterate over the file and read block sizes
    with open(os.path.join(root_directory, file_name), "rb") as file:
        while True:
            buffer = file.read(block_size)
            if not buffer:
                break
            hash = hashlib.md5()
            hash.update(buffer)

            # Append to the hashList
            output_hash_list.append(hash.hexdigest())

    # return the list of outputHash
    return output_hash_list


#------------------------------------------------------------
# Function to generate a Merkle root hash for a list of hash
# using Recursion to generate the final hash root
#------------------------------------------------------------
def generate_merkle_hash(hash_list):
    # Check if only one entry in the list
    if len(hash_list) == 1:
        return hash_list[0]

    interim_hash_list = []
    # Process pairs. For odd length, the last is skipped
    for i in range(0, len(hash_list) - 1, 2):
        interim_hash_list.append(binary_hash(hash_list[i], hash_list[i + 1]))
    # odd, hash last item twice
    if len(hash_list) % 2 == 1:
        interim_hash_list.append(binary_hash(hash_list[-1], hash_list[-1]))
    return generate_merkle_hash(interim_hash_list)


#------------------------------------------------------------
# Function to generate a binary hash from two sha1 hashes
#------------------------------------------------------------
def binary_hash(a, b):
    # Reverse inputs before and after hashing
    rev_a = a.decode('hex')[::-1]
    rev_b = b.decode('hex')[::-1]
    h = hashlib.sha256(hashlib.sha256(rev_a + rev_b).digest()).digest()
    return h[::-1].encode('hex')


#------------------------------------------------------------
# Function to check whether the merkle root has of two files
# is same or not
#------------------------------------------------------------
def compare_hashes(hash_a, hash_b):
    # Return true or false based on the hash
    if hash_a == hash_b:
        return True
    else:
        return False
