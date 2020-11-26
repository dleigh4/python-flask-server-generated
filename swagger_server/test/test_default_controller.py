# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.phonenumber import Phonenumber  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_phone_get(self):
        """Test case for phone_get

        Requests a phone number to be allotted by the server
        """
        response = self.client.open(
            '/dleigh4/phone/1.0.0/phone',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_phone_number_get(self):
        """Test case for phone_number_get

        Requests a specific number to be allotted, which is returned if available; if unavailable, responds with a system-allotted number
        """
        response = self.client.open(
            '/dleigh4/phone/1.0.0/phone/{number}'.format(number=56),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
                       
                       
                       


if __name__ == '__main__':
    import unittest
    unittest.main()
