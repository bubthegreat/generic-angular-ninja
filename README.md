# Skill Matrix

Skill matrix is a website for building out skill matrices and doing self and team assessments based on them.

## Documentation

Included documentation for django and django-ninja for offline use

## Getting Started

### Install MiniKube

https://minikube.sigs.k8s.io/docs/start/

Install the minikube service on WSL2

```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb
sudo dpkg -i minikube_latest_amd64.deb
```

Enable the various required plugins:

```
minikube addons enable ingress
minikube addons enable ingress-dns
minikube addons enable dashboard
minikube addons enable metrics-server
```

### Install Tilt

```
curl -fsSL https://raw.githubusercontent.com/tilt-dev/tilt/master/scripts/install.sh | bash
```

### Git'er Done

```
tilt up
```

[Admin UI](./files/admin_ui.png, "The Admin UI")