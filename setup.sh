#!/usr/bin/bash

# install dev tools
sudo yum -y groupinstall 'Development Tools'

# install PyQt4 for webpage previews


wget https://sourceforge.net/projects/pyqt/files/sip/sip-4.19.6/sip-4.19.6.tar.gz
tar -xzf sip-4.19.6.tar.gz

(
        cd sip-4.19.6/
        python configure.py
        sudo make
        sudo make install
)

wget http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.12.1/PyQt4_gpl_x11-4.12.1.tar.gz
tar -xzf PyQt4_gpl_x11-4.12.1.tar.gz

/usr/bin/python2.7 configure.py -v /usr/bin/sip
