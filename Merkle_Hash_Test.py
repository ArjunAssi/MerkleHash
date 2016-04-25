# ------------------------------------------------------------
# AUTHOR : LEONIDAS
# DATE : 25th APRIL 2016
# DESCRIPTION : TEST CLASS TO TEST HASHING API
#------------------------------------------------------------

# Import the Hash_Util API
import Merkle_Hash_Util

# Generate the list of hashes for the input files
hash_list_a = Merkle_Hash_Util.generate_sha1_for_file("/home/leonidas/Desktop/","sortedFile.txt")
hash_list_b = Merkle_Hash_Util.generate_sha1_for_file("/home/leonidas/Desktop/","inputURLS.txt")
hash_list_c = Merkle_Hash_Util.generate_sha1_for_file("/home/leonidas/Desktop/","sortedFile.txt")

# Generate the Merkle root hash for all 3
interim_hash_list_a= Merkle_Hash_Util.generate_merkle_hash(hash_list_a)
interim_hash_list_b= Merkle_Hash_Util.generate_merkle_hash(hash_list_b)
interim_hash_list_c= Merkle_Hash_Util.generate_merkle_hash(hash_list_c)

# Check for equality of files
print Merkle_Hash_Util.compare_hashes(interim_hash_list_a,interim_hash_list_b)
print Merkle_Hash_Util.compare_hashes(interim_hash_list_a,interim_hash_list_c)
print Merkle_Hash_Util.compare_hashes(interim_hash_list_b,interim_hash_list_c)
