docker_build('skill-matrix-api-image', 'skill_matrix_api/', live_update=[
    sync('./skill_matrix_api/skill_matrix', '/usr/src/skill_matrix/skill_matrix'),
])
docker_build('skill-matrix-app-image', 'skill_matrix_app/')
docker_build(
    'skill-matrix-gateway',
    context='./gateway',
    dockerfile='./gateway/Dockerfile',
    live_update=[
        sync('./gateway/nginx.conf', '/etc/nginx/nginx.conf'),
        run('nginx -s reload', trigger=['./gateway/nginx.conf'])
    ]
)


k8s_yaml('skill_matrix_api/kubernetes.yaml')
k8s_yaml('skill_matrix_app/kubernetes.yaml')
k8s_yaml('gateway/kubernetes.yaml')


k8s_resource('skill-matrix-app', port_forwards=8080, labels=['app'])
k8s_resource('skill-matrix-api', port_forwards=8000, labels=['api'])
k8s_resource('skill-matrix-gateway', port_forwards=[port_forward(8040, 80, host="localhost")], labels=['platform'])

local_resource(
    "port_forward_to_80",
    serve_cmd="ncat --sh-exec 'ncat 127.0.0.1 8040' -l 80 --keep-open",
    labels=['platform']
)