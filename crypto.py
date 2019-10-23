import pyAesCrypt
import extUtils
import glob

from os import remove, path, listdir

buffer = 64 * 1024


def encrypt_file(file_in, file_out, password):
    pyAesCrypt.encryptFile(file_in, file_out, password, buffer)
    remove(file_in)
    return file_out


def decrypt_file(file_in, file_out, password):
    pyAesCrypt.decryptFile(file_in, file_out, password, buffer)
    remove(file_in)
    return file_out


def encrypt(file_in, password):
    if path.isfile(file_in):
        return encrypt_file(file_in, extUtils.add_ext(file_in), password)
    else:
        return encrypt_folder(file_in, password)


def decrypt(file_in, password):
    if path.isfile(file_in):
        return decrypt_file(file_in, extUtils.remove_ext(file_in), password)
    else:
        return decrypt_folder(file_in, password)


def encrypt_folder(path, password):
    files = [f for f in glob.glob(path + "**/*.*", recursive=True)]
    output = []
    for f in files:
        output.append(encrypt(f, password))
    return output


def decrypt_folder(path, password):
    files = [f for f in glob.glob(path + "**/*.*", recursive=True)]
    output = []
    for f in files:
        output.append(decrypt(f, password))
    return output
