"""Module to handle requests session"""

from requests_toolbelt.sessions import BaseUrlSession
from requests.auth import HTTPBasicAuth

from aind_slims_service_server.configs import Settings

settings = Settings()


def get_session():
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    session = BaseUrlSession(base_url=settings.host)
    session.auth = HTTPBasicAuth(
        settings.username, settings.password.get_secret_value()
    )
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
    })
    try:
        yield session
    finally:
        session.close()
