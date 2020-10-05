#!/bin/sh
# init-root.sh - Initialize system-level(root) requirements for our project
# Should be set in the Vagrantfilee to run once as root.

# Install basic manipulation packages
dnf -y install vim dos2unix lsof
echo "-----1ST INIT DONE-----"