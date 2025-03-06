# def test_evalExpression(model):
# 	assert model("1 + 2") == "3"

import pytest


@pytest.mark.parametrize(
    "expression, expected_result", [("1 + 2", "3"), ("1 + 21", "22")]
)
def test_calculateResult(controller, expression, expected_result):
    """Test the function of _calculateResult."""
    controller._view.setDisplayText(expression)
    controller._calculateResult()
    assert controller._view.displayText() == expected_result
