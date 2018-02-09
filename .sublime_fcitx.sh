#!/bin/bash
# filename: sublime_text{version}_fcitx.sh
# by: SublimeFcitx
# from: https://github.com/ubuntugege/SublimeFcitx

sh -c "LD_PRELOAD='{pkg_dir}/sublime_fcitx.{arch}.so' '{st_exe}' --class=sublime-text '$@'"
