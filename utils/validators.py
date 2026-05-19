from models.integration import Integration


def validate_integrations_schema(data):
    assert isinstance(data, list), "Integrations response must be a list"

    for i, item in enumerate(data):
        assert isinstance(item, dict), f"Item {i} is not a dict"

        try:
            Integration(**item)
        except Exception as e:
            raise AssertionError(f"Invalid integration schema at index {i}: {e}")

    return True