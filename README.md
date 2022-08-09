# Generic UI / API

This is a generic setup for is a website for building out a website with an API deployed in kubernetes.  Really though right now this is some bare bones implementation stuff.

Items in the to do list: 

* Add a persistent database deployment with postgres and make it available
* Add a persistent redis deployment
* Add a persistent rabbitmq deployment
* Add a spark cluster option
* Add some pulsar love https://pulsar.apache.org/docs/next/helm-install
* 


## Getting Started

If you're on WSL2 you can run:
```
./setup.sh
```

![Admin UI](img/install.sh.png?raw=true)

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
## Default locations

### Admin UI
Once you've got things started up, you should be able to reach the admin UI at http://app.localhost/admin/

![Admin UI](img/admin_ui.png?raw=true)

### Angular UI
Once you've got things started up, you should be able to reach the admin UI at http://app.localhost/ui/

![Admin UI](img/angular_ui.png?raw=true)

### Django Ninja Swagger Docs
Once you've got things started up, you should be able to reach the admin UI at http://app.localhost/api/docs/

![Admin UI](img/api_docs.png?raw=true)