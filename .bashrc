PS1='\[\033[1;47m\]\[\033[1;30m\]Nix -\[\033[1;34m\] \w \[\033[1;30m\]$ \[\033[0m\] '

alias msys='sudo apt update -y ; sudo apt upgrade -y ; sudo apt --purge autoremove -y'
alias nano='nano -ilm -T 4'
alias pip3='python3 -m pip'
alias gcom='git add . && git commit -m "@$USER"'
alias gpush='gcom; git push'

alias ..="cd .."
alias psearch='grep -rnw . -e'
alias vpy='python3 -m venv'
alias py='python3'
