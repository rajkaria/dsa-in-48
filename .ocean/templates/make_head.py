#!/usr/bin/env python3
"""Instantiate a learn-module head from the template.
Usage: python3 .ocean/templates/make_head.py <slug> "<Title>" "<Desc>" "<FAV>" <acc> <acc_deep> <acc_darkdeep> <acc_rgb>
Writes to stdout."""
import sys
slug, title, desc, fav, acc, deep, darkdeep, rgb = sys.argv[1:9]
t = open(".ocean/templates/learn-head-base.html").read()
t = (t.replace("__TITLE__", title).replace("__DESC__", desc).replace("__FAV__", fav)
      .replace("__ACC_URL__", acc.lstrip("#")).replace("__ACC_DEEP__", deep)
      .replace("__ACC_DARKDEEP__", darkdeep).replace("__ACC_RGB__", rgb)
      .replace("__ACC__", acc))
sys.stdout.write(t)
