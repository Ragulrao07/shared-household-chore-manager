import os
from django.core.wsgi import get_wsgi_application
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.instrumentation.django import DjangoInstrumentor

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Configure OTel Resource with service name and environment
environment = os.getenv('APP_ENV', 'dev')
resource = Resource.create({
    "service.name": "shared-household-chore-manager",
    "deployment.environment": environment,
})

provider = TracerProvider(resource=resource)
trace.set_tracer_provider(provider)

# Instrument Django
DjangoInstrumentor().instrument()

application = get_wsgi_application()
