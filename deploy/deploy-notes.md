# Where this is hosted

In an oracle always-free VM instance.

# Stuff I installed

```sh
sudo apt update && sudo apt install -y python3-virtualenv gcc python3-dev certbot
./run.sh
sudo cp deploy/filegen.service /etc/systemd/system/

sudo systemctl enable filegen
sudo systemctl start filegen
```

# Certs

Had a bit of a problem with oracle's iptables setup. Smooth otherwise.

```sh
sudo systemctl disable iptables
sudo certbot certonly
```

