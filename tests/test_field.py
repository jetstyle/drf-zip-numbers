"""
Test filed for DRF
"""
import pytest

from drf_zip_numbers.fields import ZipNumberField


@pytest.mark.usefixtures
class TestField:
    """
    Tests for field
    """

    @staticmethod
    def test_to_internal_value(greater_10, less_10):
        """
        Test parsing string
        """
        field = ZipNumberField(max_length=10)

        for invalid_string in greater_10:
            with pytest.raises(Exception):
                field.to_internal_value(invalid_string)

        for valid_string, internal_value in less_10:
            assert field.to_internal_value(valid_string) == internal_value

    @staticmethod
    def test_to_representation(field_zipped):
        """
        Test making a zipped string
        """
        field = ZipNumberField()

        for value, representation in field_zipped:
            assert field.to_representation(value) == representation
