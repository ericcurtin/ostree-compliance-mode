#!/bin/bash

gcc -O2 ostree-dev-mode.c -o /usr/bin/ostree-dev-mode
cp ostree-dev-mode-helper /usr/libexec/ostree-dev-mode-helper
chmod 700 /usr/libexec/ostree-dev-mode-helper
cp ostree-dev-mode.conf /etc/ostree-dev-mode.conf
chmod 700 /etc/ostree-dev-mode.conf 

