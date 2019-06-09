"""
Field for DRF
"""
from functools import reduce
from typing import List, Tuple

from rest_framework.fields import Field

from drf_zip_numbers.exceptions import TooManyTokens
from drf_zip_numbers.parser import ZipNumberParser


class ZipNumberField(Field):
    """
    Field for "zip numbers"
    """
    default_error_messages = {
        'max_length': "Too many tokens"
    }

    def __init__(self, max_length=1000000, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length
        self.parser = ZipNumberParser(max_length=max_length)

    def to_internal_value(self, data: str):
        """
        Parse value
        """
        try:
            return self.parser.parse(data)
        except TooManyTokens:
            self.fail('max_length')

    def to_representation(self, value: List[int]):
        """
        Make zipped string
        """
        source = value[0:self.max_length]

        if len(source) > 2:
            source.sort()
            min_value = source[0]
            ranges = self._get_ranges([
                item - min_value
                for item in source
            ])
            # Make string:
            # >> min_value = 10
            # >> ranges = [(0, 4), (6), (8-9)]
            # representation -> '10(0-4,6,8-9)'
            representation = f'{min_value}({",".join(["-".join([str(_) for _ in r]) for r in ranges])})'
        else:
            representation = ','.join([str(number) for number in source])

        return representation

    @staticmethod
    def _get_ranges(source_list: List[int]) -> List[Tuple[int]]:
        """
        Get ranges from sorted list
        """
        def reducer(last, current):
            if isinstance(last, int):
                last = ([(last,)], last)

            ranges_cache, previous = last
            current_range = ranges_cache.pop()
            if current_range[-1] == current - 1:
                current_range = (current_range[0], current)
            else:
                ranges_cache.append(current_range)
                current_range = (current,)

            ranges_cache.append(current_range)

            return (ranges_cache, current)

        ranges, _ = reduce(reducer, source_list)

        return ranges
