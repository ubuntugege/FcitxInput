#!/bin/bash
# filename: sublime_text{version}_fcitx.sh
# by: FcitxInput
# from: https://github.com/ubuntugege/FcitxInput

sh -c "LD_PRELOAD='{pkg_dir}/sublime_fcitx.{arch}.so' '{st_exe}' --class=sublime-text '$@'"
