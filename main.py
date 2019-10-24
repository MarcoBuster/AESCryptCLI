import argparse
from getpass import getpass

import crypto

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt', dest='encrypt', help='Encrypt mode', default=False, action='store_true')
    parser.add_argument('-d', '--decrypt', dest='decrypt', help='Decrypt mode', default=False, action='store_true')
    parser.add_argument('-i', '--input', dest='input', type=str, help='The input file (or folder)', default='')
    parser.add_argument('-o', '--output', dest='output', type=str, help='The output file (or folder, optional)',
                        default='')
    parser.add_argument('-p', '--password', dest='password', type=str, help='The password of the file',
                        default='')

    args = parser.parse_args()

    if not args.input or (not args.decrypt and not args.encrypt):
        print("Invalid arguments.")
        exit(0)

    if args.password:
        password = args.password
    else:
        password = getpass()

    if args.encrypt:
        if args.output:
            print(crypto.encrypt_file(args.input, args.output, password))
        else:
            print(crypto.encrypt(args.input, password))
    elif args.decrypt:
        if args.output:
            print(crypto.decrypt_file(args.input, args.output, password))
        else:
            print(crypto.decrypt(args.input, password))
    else:
        print("Invalid arguments.")
