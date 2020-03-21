# Standard library imports...
from unittest.mock import Mock, patch

# Third-party imports...
from nose.tools import assert_is_not_none

# Local imports...
from ahp.api.nhl.accessor import Accessor


@patch('ahp.api.nhl.accessor.Accessor._get')
def test_getting_todos(mock):
    # Configure the mock to return a response with an OK status code.
    mock.return_value.ok = True

    # Call the service, which will send a request to the server.
    accessor = Accessor()
    response = accessor._get(url='test')

    # If the request is sent successfully, then I expect a response to be returned.
    assert_is_not_none(response)
