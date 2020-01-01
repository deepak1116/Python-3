import json

import pyobjcrypto

dictionary = {
    'quiz': {
        'sport': {
            'q1': {
                'question': 'Which one is correct team name in NBA?',
                'options': [
                    'New York Bulls',
                    'Los Angeles Kings',
                    'Golden State Warriros',
                    'Huston Rocket'
                ],
                'answer': 'Huston Rocket'
            }
        },
        'maths': {
            'q1': {
                'question': '5 + 7 = ?',
                'options': [
                    '10',
                    '11',
                    '12',
                    '13'
                ],
                'answer': '12'
            },
            'q2': {
                'question': '12 - 8 = ?',
                'options': [
                    '1',
                    '2',
                    '3',
                    '4'
                ],
                'answer': '4'
            }
        }
    }
}

key = 'password' # 'key' to perform AES encryption and to decrypt
crypt = pyobjcrypto.Crypter(key)

# Encrypt the "dictionary" containing many types dict , list , object etc.
encrypted_dictionary = crypt.encrypt_object(dictionary)

# Decrypt the "encryted_dictionary"  containing many types dict , list . objects etc.
decrypted_dictionary = crypt.decrypt_object(encrypted_dictionary)

# Encrypting the JSON file and store the data in new file "enc_test_json.json" in the same directory.
with open('example_2.json') as to_encrypt_json:
    to_encrypt_json_data = json.load(to_encrypt_json)
    json_dict = json.dumps(to_encrypt_json_data)
    enc_json = crypt.encrypt_json(json_dict)
    with open('enc_test_json.json', 'w') as encrypt_json:
        json.dump(enc_json, encrypt_json)

#  Decrypting the encrypted JSON file "enc_test_json.json"and store the data in new file "dec_test_json.json" in the same directory.

with open('enc_test_json.json') as to_decrypt_json:
    to_decrypt_json_data = json.load(to_decrypt_json)
    json_dict = json.dumps(to_decrypt_json_data)
    dec_json = crypt.decrypt_json(json_dict)
    with open('dec_test_json.json', 'w') as decrypt_json:
        json.dump(dec_json, decrypt_json)
