************
INSTALLATION 
************

.. code:: bash

  rsync -av home/ $HOME/
  git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
  vim +PluginInstall +qall
  echo "source $HOME/.local/rc/endless_histsize" >> ~/.profile
  echo "source $HOME/.local/rc/python" >> ~/.bashrc
  echo "source $HOME/.local/rc/ros" >> ~/.bashrc
  
Careful!! The first line replaces your .vimrc. Remove home/.vimrc first, if you don't want this.

************
USAGE 
************

Add a line like     

.. code:: python

  "voronoi/map.json": ("/web/map", OccupancyGrid)
  
to save_ros_msgs.py and run:

.. code:: bash

  python save_ros_msgs.py
  
The first string is the resulting filename, the last two are topic and topic type. To load the JSON as ros msg, do the following:

.. code:: python

  from rospy_message_converter import message_converter
  with open("map.json") as outfile:
    map_msg = message_converter.convert_dictionary_to_ros_message("nav_msgs/OccupancyGrid", json.load(outfile))
    
If you put this code in a .pyrc.py, you can access map_msg whenever you open python in interactive shell.
