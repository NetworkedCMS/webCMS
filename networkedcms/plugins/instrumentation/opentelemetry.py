from opentelemetry.instrumentation.flask import FlaskInstrumentor
from core import NetworkedCMS
import typing as t
class OpenInstrumentation(FlaskInstrumentor):

    """Instrumentents NetworkedCMS app to any metrics frontend
        like promethues, datadog etc 
    """

    def instrument(self, **kwargs):
        return super().instrument(**kwargs)
        


def instrument_app(app:NetworkedCMS, request_hook=None, response_hook=None, 
        tracer_provider=None,excluded_urls:t.List= None, enable_commenter:bool = False,
        commenter_options=None, meter_provider=None 
        ):
    return OpenInstrumentation().instrument_app(app, request_hook, response_hook, tracer_provider, 
            excluded_urls, enable_commenter, commenter_options, meter_provider)