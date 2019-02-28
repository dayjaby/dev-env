#!/bin/sh

rsync -av home/ $HOME/
git clone https://github.com/nojhan/liquidprompt.git ~/.local/bin/liquidprompt
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
echo "source $HOME/.local/rc/.profile" >> ~/.profile
echo "source $HOME/.local/rc/.bashrc" >> ~/.bashrc
vim +PluginInstall +qall

