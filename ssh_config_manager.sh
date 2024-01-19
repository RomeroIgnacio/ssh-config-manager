#! /bin/bash

while true
do
    # Ingresar el nombre del Host
    echo -n "Type your Host Name: "
    read host

    # Ingresar el nombre del HostName
	echo -n "Type your HostName ('github.com' default): "
    read hostname

    # Ingresar el nombre del Usuario
	echo -n "Type your User ('git' default): "
    read user

    # Ingresar el nombre del IdentityFile
	echo -n "Type your IdentityFile (~/.ssh/): "
    read idfile

    # Mostrar la configuración ingresada
    echo -n -e "\nHost $host\n\tHostName $hostname\n\tUser $user\n\tIdentityFile ~/.ssh/$idfile"

    # Preguntar si desea añadir la configuración
    echo -n -e "\nDo you want to add this configuration? (y/n): "
    read op

    if [ "$op" == "y" ]
    then
        # Añadir los datos ingresados al archivo $HOME/.ssh/config
        echo -e "\nHost $host\n\tHostName $hostname\n\tUser $user\n\tIdentityFile ~/.ssh/$idfile" >> $HOME/.ssh/config

        # Mostrar los datos añadidos
        echo -e "Host added successfully!"
		cat ~/.ssh/config

        # Preguntar si desea añadir otro usuario
        echo -n -e "\nDo you want to add another configuration? (y/n): "
        read sn

        if [ "$sn" != "y" ]
        then
            break
        fi
    else
        break
    fi
done
