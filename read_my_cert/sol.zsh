#!/usr/bin/zsh

tail +2 readmycert.csr | head -n -1 | base64 -d

