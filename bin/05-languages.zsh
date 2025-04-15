# install paths and directives for various languages
# this is early in the process because they may be used
# later in the process, unlike most programs

export PYTHONPATH="$HOME/.local/lib:$PYTHONPATH"
typeset -U PYTHONPATH
export VIRTUALENV_HOME=".venv"
