# headers
ASSIGNMENT_RULE_HEADER = 'AssignmentRuleHeader'
EMAIL_HEADER = 'EmailHeader'

# elements
USE_DEFAULT_RULE = 'useDefaultRule'
TRIGGER_USER_EMAIL = 'triggerUserEmail'
ASSIGNMENT_RULE_ID = 'assignmentRuleId'


class SalesforceSoapHeaderElement(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value


class SalesforceSoapHeader(object):
    def __init__(self, name):
        self.name = name
        self.elements = []

    def add_elements(self, elements):
        for element in elements:
            self.add_element(element)
        return self

    def add_element(self, element):
        assert isinstance(element, SalesforceSoapHeaderElement)
        self.elements.append(element)
        return self


class SalesforceHeadersFactory(object):
    @staticmethod
    def create_assignment_rule_header(use_default_rule=False, assignment_rule_id=None):
        elements = []

        if assignment_rule_id:
            elements.append(SalesforceSoapHeaderElement(name=ASSIGNMENT_RULE_ID, value=assignment_rule_id))

        else:
            use_default_rule = bool_to_string(use_default_rule)
            elements.append(SalesforceSoapHeaderElement(name=USE_DEFAULT_RULE, value=use_default_rule))

        return SalesforceSoapHeader(name=ASSIGNMENT_RULE_HEADER) \
            .add_elements(elements)

    @staticmethod
    def create_email_header(trigger_user_email=True):
        trigger_user_email = bool_to_string(trigger_user_email)

        return SalesforceSoapHeader(name=EMAIL_HEADER) \
            .add_element(SalesforceSoapHeaderElement(name=TRIGGER_USER_EMAIL, value=trigger_user_email))


def bool_to_string(bool_value):
    return 'true' if bool_value else 'false'
