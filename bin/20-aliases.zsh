# useful aliases
APPLICATIONS_DIR="/Applications"

alias c='clear '
alias bif='brew info '
alias dlc='cd ~/.local'
alias less='cless '
alias md='mkdir -p '
alias min="$APPLICATIONS_DIR/Min.app/Contents/MacOS/Min"
alias mv='mv -i '
alias path='echo ${PATH//:/":\n"}'
alias pip='pip3 '
alias pd='pushd '
alias pysrv='python3 -m http.server'
alias python='python3 '
alias rlp='defaults write com.apple.dock ResetLaunchPad -bool true; killall Dock'
alias xx='popd '
alias X='exit '

# useful functions
_bounce(){
    P=$PWD
    cd ..
    cd $P
}
alias bounce=_bounce
