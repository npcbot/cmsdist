### RPM external py2-jupyter_console 5.2.0
## IMPORT build-with-pip

BuildRequires: py2-backports-shutil_get_terminal_size
Requires: py2-ipykernel
%define PipPostBuild perl -p -i -e "s|^#!.*python|#!/usr/bin/env python|" %{i}/bin/jupyter-console
