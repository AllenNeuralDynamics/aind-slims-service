"""Module to handle requests session"""

from slims.slims import Slims

from aind_slims_service_server.configs import Settings

settings = Settings()

def get_session(settings=None):
    """
    Yield a session object. This will automatically close the session when
    finished.
    """
    session = Slims(
        name=settings.db,
        username=settings.username,
        password=settings.password.get_secret_value(),
        url=settings.host,
    )
    yield session
