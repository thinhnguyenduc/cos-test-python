def cook_element(element: tuple, replace_string):
    locator = element[0]
    value = element[1]
    new_value = value % replace_string
    return (locator, new_value)
