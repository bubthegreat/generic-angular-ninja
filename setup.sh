curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
minikube config set cpus 4
minikube config set memory 12g
minikube addons enable ingress
minikube addons enable ingress-dns
minikube addons enable dashboard
minikube addons enable metrics-server
minikube start --extra-config=kubelet.housekeeping-interval=10s
