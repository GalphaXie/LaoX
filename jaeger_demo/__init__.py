
# coding=utf-8

import logging

from tracer import Config


def init_tracer(service):
    logging.getLogger('').handlers = []
    logging.basicConfig(format='%(message)s', level=logging.DEBUG)

    config = Config(
        config={
            'sampler': {
                'type': 'const',
                'param': 1,
            },
            'logging': True,
        },
        service_name=service,
    )

    # this call also sets opentracing.tracer
    return config.initialize_tracer()



'''
with tracer.start_span('main-context') as span:
    with tracer.start_span('main-context') as span:
        with span_in_context(span):
        
        
with tracer.start_span("clean_github_data", child_of=get_current_span()) as span:


'''