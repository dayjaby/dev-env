#!/bin/sh

rsync -av home/ $HOME/
mkdir -p ~/.local/bin
cd ~/.local/bin
git clone https://github.com/nojhan/liquidprompt.git
cd -
echo "source $HOME/.local/rc/.profile" >> ~/.profile
echo "source $HOME/.local/rc/.bashrc" >> ~/.bashrc
vim +PluginInstall +qall

