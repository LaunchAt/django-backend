from django_hosts import host, patterns

host_patterns = patterns(
    '',
    host(r'admin(\.\w+)*', 'project.urls', name='admin'),
    host(r'api(\.\w+)*', 'project.api.urls', name='api'),
)
