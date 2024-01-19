#! /usr/bin/env python

import os

FILEPATH = os.path.expanduser("~/.ssh/config")

def readfile():
    try:
        with open(FILEPATH, 'r') as f:
            print(f.read())
    
    except FileNotFoundError:
        print(f"El archivo {FILEPATH} no existe.")

    except Exception:
        print(f"Error al leer el archivo {e}")

def writefile(host, hostname, user, idfile):
    try:
        with open(FILEPATH, 'a') as f:
            f.write(f"\nHost {host}\n\tHostName {hostname}\n\tUser {user}\n\tIdentityFile {idfile}\n")
            print("Configuración agregada correctamente.")

    except Exception as e:
        print(f"Error al escribir en el archivo {FILEPATH}: {e}")

def getuser():
    host = input("Ingresa el Host: ")
    hostname = input("Ingresa el HostName ('github.com'): ")
    user = input("Ingresa el User ('git'): ")
    idfile = input("Ingresa el IdentityFile ('~/.ssh/'): ")

    return host, hostname, user, idfile

def main():
    readfile()

    while True:
        host, hostname, user, idfile = getuser()

        print(f"\nHost {host}\n\tHostName {hostname}\n\tUser {user}\n\tHostName {idfile}\n")

        op = input("¿Quieres añadir esta configuración al archivo? (y/n): ").lower()
        if op == "y":
            writefile(host, hostname, user, idfile)

        sn = input("\n¿Quieres añadir otra configuración? (y/n): ").lower()
        if sn != "y":
            break

if __name__ == "__main__":
    main()