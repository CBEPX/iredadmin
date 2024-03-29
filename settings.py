############################################################
# DO NOT TOUCH BELOW LINE.
#
from libs.default_settings import *

############################################################
# General settings.
#
# Site webmaster's mail address.
webmaster = "postmaster@"

# Default language.
default_language = 'en_US'

# Database backend: mysql.
backend = 'mysql'

# Base directory used to store all mail data.
# iRedMail uses '/var/vmail/vmail1' as default storage directory.
# Tip: You can set a per-domain storage directory in domain profile page.
storage_base_directory = "/var/vmail/vmail1"

# Default mta transport.
# iRedMail uses 'dovecot' as defualt transport.
# Tip: You can set a per-domain or per-user transport in domain or user
#      profile page.
default_mta_transport = 'dovecot'

# Min/Max admin password length.
#   - min_passwd_length: 0 means unlimited, but at least 1 character
#                        is required.
#   - max_passwd_length: 0 means unlimited.
# User password length is controlled in domain profile.
min_passwd_length = 8
max_passwd_length = 0

#####################################################################
# Database used to store iRedAdmin data. e.g. sessions, log.
#
iredadmin_db_host = "127.0.0.1"
iredadmin_db_port = "3306"
iredadmin_db_name = "iredadmin"
iredadmin_db_user = "iredadmin"
iredadmin_db_password = "dfODvBAqOR4EaMNLKhQOYWIZmwSFuc"

############################################
# Database used to store mail accounts.
#
vmail_db_host = "127.0.0.1"
vmail_db_port = "3306"
vmail_db_name = "vmail"
vmail_db_user = "vmailadmin"
vmail_db_password = "GYyFEFmsMvnL8dKsJpzBcNqYXeyOi0"

#################################################################
# Settings used for Policyd (1.8.x) integration. Provides global
# white-/blacklist, sender/recipient throttling, etc.
#
# Enable policyd integration: True, False.
policyd_enabled = True

# SQL Database used to store policyd data, eg. whitelist, blacklist.
# You can find related information in policyd config files:
#   - On RHEL/CentOS:   /etc/policyd.conf
#   - On Debian/Ubuntu: /etc/postfix-policyd.conf
#   - On FreeBSD:       /usr/local/etc/policyd.conf
# Related parameters:
#   host    -> MYSQLHOST
#   port    -> 3306 (Default)
#   db      -> MYSQLDBASE
#   user    -> MYSQLUSER
#   passwd  -> MYSQLPASS
policyd_db_host = "127.0.0.1"
policyd_db_port = "3306"
policyd_db_name = "cluebringer"
policyd_db_user = "cluebringer"
policyd_db_password = "Xb765wxwAqvxDaLGdqlCrL78tAfMAT"

##############################################################################
# Settings used for Amavisd-new integration. Provides spam/virus quaranting,
# releasing, etc.
#
# Log basic info of in/out emails into SQL (@storage_sql_dsn): True, False.
# It's @storage_sql_dsn setting in amavisd. You can find this setting
# in amavisd-new config files:
#   - On RHEL/CentOS:   /etc/amavisd.conf or /etc/amavisd/amavisd.conf
#   - On Debian/Ubuntu: /etc/amavis/conf.d/50-user.conf
#   - On FreeBSD:       /usr/local/etc/amavisd.conf
# Reference:
# http://www.iredmail.org/wiki/index.php?title=IRedMail/FAQ/Integrate.MySQL.in.Amavisd
amavisd_enable_logging = True

amavisd_db_host = "127.0.0.1"
amavisd_db_port = "3306"
amavisd_db_name = "amavisd"
amavisd_db_user = "amavisd"
amavisd_db_password = "Xu271JsyU7F37ihtPhlBRoQzQlpSkt"

# #### Quarantining ####
# Release quarantined SPAM/Virus mails: True, False.
# iRedAdmin-Pro will connect to @quarantine_server to release quarantined mails.
# How to enable quarantining in Amavisd-new:
# http://www.iredmail.org/wiki/index.php?title=IRedMail/FAQ/Quarantining.SPAM
amavisd_enable_quarantine = True

# Port of Amavisd protocol 'AM.PDP-INET'. Default is 9998.
amavisd_quarantine_port = "9998"

# Enable per-recipient spam policy, white/blacklist.
amavisd_enable_policy_lookup = True

##############################################################################
# Place your custom settings below, you can override all settings in this file
# and libs/default_settings.py here.
#
DEFAULT_PASSWORD_SCHEME = 'SSHA512'
