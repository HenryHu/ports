#! /bin/sh
#
# gen-patch.sh
# Copyright (C) 2018 henryhu <henryhu@goldpeak>
#
# Distributed under terms of the MIT license.
#


diff -ruN -x work -x sync-patch.sh -x gen-patch.sh -x update.txt -x check-diff.py -x files.bak /usr/ports/net-im/telegram-desktop .
