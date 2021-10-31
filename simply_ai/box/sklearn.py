from simply_ai.box.box import Box


class SkLearnBox(Box):
    pass


class LinearRegressionSKLBox(SkLearnBox):
    pass


SKLEARN_AVAILABLE_BOXES = {
    "LinearRegressionSKLBox": LinearRegressionSKLBox
}


def sklearn_check_model(config):
    from simply_ai.utils import checking
    rules = {}
    checking.check_config(config, rules)
