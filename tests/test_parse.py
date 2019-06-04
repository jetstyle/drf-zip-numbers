"""
Tests for parser
"""
import pytest

from drf_zip_numbers.exceptions import TooManyTokens
from drf_zip_numbers.parser import ZipNumberParser


@pytest.mark.usefixtures
class TestParser:
    """
    Tests for parser
    """

    @staticmethod
    def assert_parse(source, result, **kwargs):
        """
        Run parse and check result
        """
        parser = ZipNumberParser(**kwargs)
        assert parser.parse(source) == result

    def test_no_zipped_string(self, no_zipped):
        """
        Test parse list from string without zip
        """
        for source, result in no_zipped:
            self.assert_parse(source, result)

    def test_ranges(self, ranges):
        """
        Test parse ranges like "1-3"
        """
        for source, result in ranges:
            self.assert_parse(source, result)

    def test_zipped_string(self, zipped):
        """
        Test parse zipped strings
        """
        for source, result in zipped:
            self.assert_parse(source, result)

    def test_mixed_string(self, mixed):
        """
        Test mixed strings
        """
        for source, result in mixed:
            self.assert_parse(source, result)

    def test_string_with_base(self, bases):
        """
        Test mixed strings
        """
        for source, result in bases:
            self.assert_parse(source, result)

    def test_limit(self, greater_10, less_10):
        """
        Test limits
        """
        for source in greater_10:
            with pytest.raises(TooManyTokens):
                self.assert_parse(source, [], max_length=10)

        for source, result in less_10:
            self.assert_parse(source, result, max_length=10)
