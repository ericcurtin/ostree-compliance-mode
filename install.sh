#!/bin/bash

PREFIX="/var"

if [ $EUID != 0 ]; then
   echo "This script must be run as root" 
   exit 1
fi

mkdir -p $PREFIX/bin
gcc -O2 ostree-dev-mode.c -o $PREFIX/bin/ostree-dev-mode
chmod 4011 $PREFIX/bin/ostree-dev-mode
mkdir -p $PREFIX/libexec
cp ostree-dev-mode-helper $PREFIX/libexec/ostree-dev-mode-helper
chmod 100 $PREFIX/libexec/ostree-dev-mode-helper
cp ostree-dev-mode.conf /etc/ostree-dev-mode.conf
chmod 600 /etc/ostree-dev-mode.conf 

