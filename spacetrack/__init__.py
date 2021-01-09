from .aio import AsyncSpaceTrackClient  # noqa
from .base import (  # noqa
    AuthenticationError, SpaceTrackClient, UnknownPredicateTypeWarning)
from .operators import (  # noqa
    greater_than, inclusive_range, less_than, like, not_equal, startswith)

__all__ = (
    'AsyncSpaceTrackClient',
    'AuthenticationError',
    'SpaceTrackClient',
    'greater_than',
    'inclusive_range',
    'less_than',
    'like',
    'not_equal',
    'startswith',
)

__version__ = '0.16.0'
__description__ = 'Python client for space-track.org'

__license__ = 'MIT'

__author__ = 'Frazer McLean'
__email__ = 'frazer@frazermclean.co.uk'
