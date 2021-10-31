from typing import Dict, List, Any


class SimplyAINotImplementedError(NotImplementedError):
    def __init__(self, k, v, rules):
        available = rules[k] if type(rules[k]) == dict else ', '.join(rules[k].keys())
        super(SimplyAINotImplementedError, self).__init__(f"{v} is not a supported {k}: {available}")


class SimplyAITypeError(TypeError):
    def __init__(self, k, v, rules):
        super(SimplyAITypeError, self).__init__(f"{v}({type(v)}) is not of type: {rules[k]}")


def check_config(config: Dict[str, Any], rules: Dict[str, Any]):
    """
    Loops through provided rules and verifies input checks out
    """
    for k, rule_config in rules.items():

        if k not in config:
            raise ValueError(f"Required value ({k}) was not a provided")

        v = config[k]

        if type(rule_config) == dict:

            if type(v) == str:
                if v not in rule_config:
                    raise SimplyAINotImplementedError(k, v, rules)

            elif type(v) != dict:
                SimplyAITypeError(k, v, rules)

            elif v.keys() != rule_config.keys():
                SimplyAINotImplementedError(k, v, rules)

        elif type(rule_config) == type:
            if type(v) != rule_config:
                raise SimplyAITypeError(k, v, rules)

        elif type(rule_config) == list and type(v) == list:
            # if it's a list of list
            if not isinstance(v[0], type(rule_config[0])):
                continue

            for _v in v:
                for i in range(len(rule_config[0])):

                    if isinstance(rule_config[0][i], dict) and _v[i] not in rule_config[0][i]:
                        raise SimplyAITypeError(k, v, rules)
                    elif isinstance(rule_config[0][i], type) and not isinstance(_v[i], rule_config[0][i]):
                        raise SimplyAITypeError(k, v, rules)

        elif type(rule_config) == tuple:

            for rule_idx, _type in enumerate(rule_config):

                if type(v) == _type:
                    pass

                # if type([int, str]) == list
                if type(_type) == list and not isinstance(v, (int, str)) and len(_type) == len(v):

                    for sub_list_idx, sub_rule in enumerate(_type):

                        # if it's a class list
                        if isinstance(sub_rule, dict) and isinstance(v[sub_list_idx], str) and v[sub_list_idx] not in sub_rule:
                            raise SimplyAITypeError(k, v, rules)

                        if isinstance(sub_rule, (int, str)) and (not isinstance(v[sub_list_idx] , (int, str))):
                            raise SimplyAITypeError(k, v, rules)

                    # loop through config and verify it's all the same type
                    # same_type = None
                    # for value in v:  # [1,2,3]
                    #     if not same_type:
                    #         same_type = type(value)
                    #     if type(value) != same_type:
                    #         raise SimplyAITypeError(k, v)
