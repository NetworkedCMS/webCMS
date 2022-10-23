import sentry_sdk
from pydantic import HttpUrl
from sentry_sdk.integrations.flask import FlaskIntegration
from core import NetworkedCMS


class SentryLogger:
    """ Creates a base sentry logger class"""

    def __init__(self, dsn: HttpUrl = None, app: NetworkedCMS = None, 
            traces_sample_rate: float = 1.0):
        self.app = app
        self.dsn = dsn
        self.traces_sample_rate = traces_sample_rate

    def init_logger(self):
        """Instantiates a sentry logger object"""

        sentry_sdk.init(
            dsn="https://examplePublicKey@o0.ingest.sentry.io/0",
                integrations=[
                    FlaskIntegration(),
                ],

            # Set traces_sample_rate to 1.0 to capture 100%
            # of transactions for performance monitoring.
            # We recommend adjusting this value in production.
            traces_sample_rate=self.traces_sample_rate,

            # By default the SDK will try to use the SENTRY_RELEASE
            # environment variable, or infer a git commit
            # SHA as release, however you may want to set
            # something more human-readable.
            # release="myapp@1.0.0",
        )
