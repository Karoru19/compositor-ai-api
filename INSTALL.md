# Installation
## Linux
### Linux libs (Ubuntu)
sudo apt install timidity python-tk

## Python 2
### Tensorflow
export TF_BINARY_URL=https://storage.googleapis.com/tensorflow/linux/cpu/tensorflow-0.8.0-cp27-none-linux_x86_64.whl
sudo pip2 install --upgrade $TF_BINARY_URL

### Python 2 libs
pip2 install mathplotlib==2.0.2 numpy

### Python Midi
cd ~
git clone https://github.com/vishnubob/python-midi
cd python-midi
sudo python2 setup.py install

### Python Mingus
cd ~
git clone https://github.com/bspaans/python-mingus
cd python-mingus
sudo python2 setup.py install

## Python 3
### Python 3 libs
pip3 install --user -r requirements.txt

# Running
python3 manage.py runserver
