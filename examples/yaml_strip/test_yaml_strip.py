import pytest
from examples.yaml_strip.yaml_strip import yaml_safe_load

class TestYamlStrip:
    @pytest.mark.parametrize(
            "yaml_str,expected",
            [
                ("""\
foo: bar""", {"foo": "bar"}),
            ]
            )
    def test_clean_yaml(self, yaml_str, expected):
        assert yaml_safe_load(yaml_str) == expected
