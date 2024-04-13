sudo apt-get -y update
sudo apt-get install -y apache2
sudo systemctl start apache2
sudo systemctl enable apache2
sudo rm -r /var/www/html
sudo mkdir /var/www/html
cd /home/ubuntu/home/src/frontend/build/
sudo mv * /var/www/html