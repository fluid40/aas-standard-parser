from basyx.aas.model import ModelReference


def construct_idshort_path_from_reference(reference: ModelReference) -> str:
    idshort_path: str = ""

    # start from the second Key and omit the Identifiable at the beginning of the list
    for key in reference.key[1:]:
        idshort_path += key.value + "."

    # get rid of the trailing dot
    return idshort_path[:-1]


def get_values_from_keys(reference: ModelReference) -> list[str]:
    """Returns the values from all keys in reference as list.

    :param reference: reference to extract values from
    :return: list of values from all keys in the reference
    """
    return [key.value for key in reference.key]


def get_value_from_key_at_index(reference: ModelReference, index: int) -> str:
    """Returns the value from the key at the given index in reference.

    :param reference: reference to extract value from
    :param index: index of the key to get the value from
    :return: value from the key at the given index
    """
    return reference.key[index].value
