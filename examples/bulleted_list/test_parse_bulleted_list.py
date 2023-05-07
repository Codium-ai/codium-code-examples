from examples.bulleted_list.parse_bulleted_list import parse_bullet_list


class TestParseBulletedList:
    def test_parse_multiline_items(self):
        """
        Testes the following features:
        - For each item, prefix or suffix of whitespaces and / or '-' are ignored.
        - Items can be multiline (delimited by '\n-')
        """
        data = """

- first
still first
--second   

--  --  -  third

It is still third  ------    

    """
        expected_first = """first
still first"""
        expected_second = "second"
        expected_third = """third

It is still third"""
        expected = [
            expected_first,
            expected_second,
            expected_third,
        ]
        assert parse_bullet_list(data) == expected
