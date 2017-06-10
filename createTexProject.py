#!/usr/bin/env python
# -*- coding: utf8 -*-

import os
import sys
import pathlib
import shutil


if len(sys.argv) == 1:
    print("You must specify a name for the project", file=sys.stderr)
    sys.exit(1)

projname = sys.argv[1]

if os.path.exists(projname):
    print("There's allreaddy a file or folder with that name, choose another", file=sys.stderr)
    sys.exit(1)

bodypath = pathlib.Path('~/Dropbox/Crap/LaTeX/Document_templates/bigProject/bigProjectBody.tex').expanduser()
preamblepath = pathlib.Path('~/Dropbox/Crap/LaTeX/Document_templates/bigProject/bigProjectPreamble.tex').expanduser()

preambleName = projname + 'Preamble.tex'
bodyName = projname + 'Main.tex'
try:
    os.mkdir(projname)
    shutil.copy(preamblepath, os.path.join(projname, preambleName))
    with open(bodypath) as fid:
        strrep = fid.read()
        strrep.replace('bigProjectPreamble', preambleName)
    with open(os.path.join(projname, bodyName), 'w') as fid:
        fid.write(strrep)
except Exception as e:
    print("Something went wrong!", file=sys.stderr, end='\n\n\n')
    raise e

