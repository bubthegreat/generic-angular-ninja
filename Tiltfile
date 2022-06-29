load('ext://uibutton', 'cmd_button', 'location', 'text_input')

# minikube addons enable ingress
# minikube addons enable ingress-dns
# minikube addons enable dashboard
# minikube addons enable metrics-server

# Get ingress logs: 
# kubectl logs -n ingress-nginx `kubectl get pods -n ingress-nginx | grep controller | awk '{print $1}'`

docker_build('skill-matrix-api-image', 'skill_matrix_api/', 
    live_update=[
        sync('./skill_matrix_api/skill_matrix/', '/usr/src/skill_matrix/skill_matrix/'),
        run(
            'pip install -r /usr/src/requirements.txt',
            trigger=['./skill_matrix_api/requirements.txt']
        )
    ]
)
docker_build('skill-matrix-ui-image', 'skill_matrix_ui/')
docker_prune_settings( disable = False , max_age_mins = 360 , num_builds = 0 , interval_hrs = 1 , keep_recent = 2 ) 
docker_build('util-ubuntu-image', 'ubuntu/')

k8s_yaml([
    'skill_matrix_api/k8s/deployment.yaml',
    'skill_matrix_api/k8s/service.yaml',
    'skill_matrix_api/k8s/volume-claim.yaml',
    'skill_matrix_api/k8s/volume.yaml',
])
k8s_yaml([
    'skill_matrix_ui/k8s/deployment.yaml',
    'skill_matrix_ui/k8s/service.yaml',
])
k8s_yaml('ingress.yaml')
k8s_yaml('storage-class.yaml')
k8s_yaml('ubuntu/deployment.yaml')
k8s_yaml([
    'postgres-server/secrets.yaml',
    'postgres-server/deployment.yaml',
    'postgres-server/service.yaml',
    'postgres-server/volume-claim.yaml',
    'postgres-server/volume.yaml',
])
k8s_yaml([
    'redis-server/secrets.yaml',
    'redis-server/deployment.yaml',
    'redis-server/service.yaml',
    'redis-server/volume-claim.yaml',
    'redis-server/volume.yaml',
])

k8s_resource('skill-matrix-ui', port_forwards=8080, labels=['services'])
k8s_resource('skill-matrix-api', port_forwards=8000, labels=['services'])
k8s_resource('postgres', port_forwards=5432, labels=['databases'])
k8s_resource('redis', port_forwards=6379, labels=['databases'])


# Kubernetes resources, all of these should be non-blocking so this seems ideal - maybe some of these shoudl be buttons?
local_resource('tunnel', cmd="minikube tunnel", labels=['kubernetes'], allow_parallel=True, auto_init=False)
local_resource('ingress-logs', cmd="kubectl logs --follow -n ingress-nginx `kubectl get pods -n ingress-nginx | grep controller | awk '{print $1}'`", labels=['kubernetes'], allow_parallel=True, auto_init=False)
local_resource('deployments', cmd="kubectl get deployments", resource_deps=['skill-matrix-ui', 'skill-matrix-api'], labels=['kubernetes'], allow_parallel=True)
local_resource('services', cmd="kubectl get services", resource_deps=['skill-matrix-ui', 'skill-matrix-api'], labels=['kubernetes'], allow_parallel=True)
local_resource('k8s-yaml', cmd="kubectl get all -o yaml", resource_deps=['skill-matrix-ui', 'skill-matrix-api'], labels=['kubernetes'], allow_parallel=True)
local_resource('dashboard', cmd="minikube dashboard",  labels=['kubernetes'], auto_init=False, allow_parallel=True)

# Open the kubernetes dashboard
cmd_button(
    name='nav-dashboard',
    argv=['minikube', 'dashboard'],
    text='Minikube Dashboard',
    location=location.NAV,
    icon_name='install_desktop'
)
cmd_button(
    name='nav-black',
    argv=['black', 'skill_matrix_api/skill_matrix_api/'],
    text='Python Black',
    location=location.NAV,
    icon_name='install_desktop'
)
