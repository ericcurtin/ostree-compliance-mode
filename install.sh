#!/bin/bash

set -e

if [ -z "$PREFIX" ]; then
  PREFIX="/usr"
fi

if [ $EUID != 0 ]; then
   echo "This script must be run as root" 
   exit 1
fi

meson build --buildtype=release --prefix=$PREFIX
ninja -v -C build
ninja -v -C build install
chmod 4011 $PREFIX/bin/ostree-compliance-mode
mkdir -p $PREFIX/libexec
cp ostree-compliance-mode-helper $PREFIX/libexec/ostree-compliance-mode-helper
chmod 100 $PREFIX/libexec/ostree-compliance-mode-helper
cp ostree-compliance-mode.conf /etc/ostree-compliance-mode.conf
chmod 600 /etc/ostree-compliance-mode.conf

