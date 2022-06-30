curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
minikube config set cpus 6
minikube config set memory 12g
minikube start
minikube addons enable ingress
minikube addons enable ingress-dns
minikube addons enable dashboard
minikube addons enable metrics-server
