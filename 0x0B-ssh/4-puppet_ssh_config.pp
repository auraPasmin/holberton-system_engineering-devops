#! / usr / bin / env bash
# conectar con marioneta
file_line { ' Declare_identity_file ' :
    ruta = >  ' / etc / ssh / ssh_config ' ,
    line = >  ' IdentityFile ~ / .ssh / holberton ' ,
}

file_line { ' Turn_off_passwd_auth ' :
    ruta = >  ' / etc / ssh / ssh_config ' ,
    line = >  ' PasswordAuthentication no ' ,
}
