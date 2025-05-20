#!/usr/bin/env python3
'''Testing the utils module'''

import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized

from typing import (
    Dict,
    Mapping,
    Sequence,
    Tuple,
    Union,
)

from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ("simple_access", {"a": 1}, ("a",)),
        ("intermediate_access", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("nested_value_access", {"a": {"b": 2}}, ("a", "b"))
    ])
    def test_access_nested_map(self, 
                               nested_map: Mapping, 
                               path: Sequence, 
                               expected_output: Union[Dict, int]):
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, 
                                         nested_map: Mapping, 
                                         path: Sequence, 
                                         exception: Exception) -> None:
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)

    class TestGetJson(unittest.TestCase):
        '''Tests the `utils.get_json` function.
        '''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict,
            ) -> None:
        '''Tests `get_json`'s output.
        '''

        attrs = {'json.return_value': test_payload}

        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), test_payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests the `memoize` function."""
    def test_memoize(self) -> None:
        """Tests `memoize`'s output."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
                TestClass,
                "a_method",
                return_value=lambda: 42,
                ) as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()