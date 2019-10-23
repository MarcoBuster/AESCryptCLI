import argparse

import crypto

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', '--input', dest='input', type=str, help='The input file (or folder)', default='')
    parser.add_argument('--out', '--output', dest='output', type=str, help='The output file (or folder, optional)',
                        default='')
    parser.add_argument('--passw', '--pass', '--password', dest='password', type=str, help='The password of the file',
                        default='')
    parser.add_argument('--encrypt', '--en', dest='encrypt', help='Encrypts the file', default=False, const=True,
                        nargs='?')
    parser.add_argument('--decrypt', '--de', dest='decrypt', help='Decrypts the file', default=False, const=True,
                        nargs='?')

    args = parser.parse_args()

    if (args.input == '' or args.password == '') or (args.decrypt is False and args.encrypt is False):
        print("Invalid arguments.")
        exit(0)

    print(args)

    if args.encrypt is True:
        if args.output != '':
            print(crypto.encrypt_file(args.input, args.output, args.password))
        else:
            print(crypto.encrypt(args.input, args.password))
    elif args.decrypt is True:
        if args.output != '':
            print(crypto.decrypt_file(args.input, args.output, args.password))
        else:
            print(crypto.decrypt(args.input, args.password))
