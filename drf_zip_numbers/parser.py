"""
Parser a string
"""
from typing import List

from drf_zip_numbers.exceptions import TooManyTokens

ZIP_START_DELIMITER = '('
ZIP_END_DELIMITER = ')'


class ZipNumberParser:
    """
    Parse zipped string to list of integer numbers
    """

    def __init__(self, max_length: int = 1000000):
        self.max_length = max_length
        self.int_base = 10
        self.count_tokens = 0

    def parse(self, source: str) -> List[int]:
        """
        Parse zipped string to list of integer numbers
        """
        self.count_tokens = 0
        items = []

        # Parse base for int
        if source.startswith('x'):
            base, source = source.split(';', maxsplit=1)
            self.int_base = int(base[1:])
        else:
            self.int_base = 10

        # Parse empty string as empty list
        if source:
            items = self._parse_string(source)

        return items

    def _parse_string(self, source: str) -> List[int]:
        """
        Parse string to tokens
        """
        buffer = ''
        delimiter = ','
        tokens = []
        zip_buffer = []

        for literal in source:
            if literal == ZIP_START_DELIMITER:
                zip_buffer.append(1)
            elif literal == ZIP_END_DELIMITER:
                zip_buffer.pop()

            if not zip_buffer and literal == delimiter:
                for item in self._parse_token(buffer):
                    tokens.append(item)
                buffer = ''
            else:
                buffer += literal

        if buffer:
            for item in self._parse_token(buffer):
                tokens.append(item)

        return tokens

    def _parse_token(self, token: str) -> List[int]:
        """
        Parse token from string
        """
        if ZIP_START_DELIMITER in token:
            base, sub_source = token.split(ZIP_START_DELIMITER, maxsplit=1)
            base = self._get_int(base)
            items = self._parse_string(sub_source[:-1])

            return [
                base + item
                for item in items
            ]

        if '-' in token:
            start, stop = token.split('-', maxsplit=1)
            start = self._get_int(start)
            stop = self._get_int(stop)
            self._check_length(abs(stop - start))
            token = [item for item in range(start, stop + 1)]
        else:
            token = [token]

        count_new_tokens = len(token)
        self._check_length(count_new_tokens)
        self.count_tokens += count_new_tokens

        return [self._get_int(item) for item in token]

    def _get_int(self, num) -> int:
        """
        Parse int
        """
        if isinstance(num, int):
            return num

        return int(num, base=self.int_base)

    def _check_length(self, new_count: int):
        """
        Check limit
        """
        if self.count_tokens + new_count > self.max_length:
            raise TooManyTokens()
