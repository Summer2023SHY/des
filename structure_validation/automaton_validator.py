from typing import NotRequired, TypedDict

class __StateDict(TypedDict):
    all: list[str]
    initial: list[str]
    marked: list[list[str]]
    bad: list[str]

class __EventDict(TypedDict):
    all: list[str]
    attacker: list[str]
    controllable: list[list[str]]
    observable: list[list[str]]

class __TransitionDict(TypedDict):
    all: dict[str, list[str]]
    bad: dict[str, list[str]]

class Automaton(TypedDict):
    name: NotRequired[str]
    states: __StateDict
    events: __EventDict
    transitions: __TransitionDict

def validate(automaton: Automaton) -> bool:
    """Validates if an automaton is correctly formatted. This includes:

    1. Has a states area with "all", "initial", "marked", and "bad"
            - Must be a dictionary
            - "all", "initial", "marked", and "bad" are lists of strings
    2. Has an events area with "all", "controllable", "observable", and
       "attacker"
            - Must be a dictionary
            - "all" and "attacker" are lists of strings
            - "controllable" is a list of lists of strings, as is "observable"
              The two must have the same number of lists.
    3. Has a transitions area with "all" and "bad"
            - "all" and "bad" are dictionaries mapping strings to lists of
              strings

    If successful, returns True. If unsucessful, raises an exception explaining
    the problem.

    Parameters
    ----------
    automaton : dictionary
        The automaton to verify its structure

    Examples
    --------
    >>> validate(automaton1)
    True
    """

    if not isinstance(automaton, dict):
        raise Exception("The automaton must be a dictionary structure")

    for x in ["states", "events", "transitions"]:
        if x not in automaton:
            raise Exception("The automaton must have a key for " + x)

    # 1: STATES
    states = automaton["states"]
    if not isinstance(states, dict):
        raise Exception("The states subtree must be a dictionary structure")

    for x in ["all", "initial", "bad"]:
        if x not in states:
            raise Exception("The states subtree must have a key for " + x)
        for state in states[x]:
            if not isinstance(state, str):
                raise Exception("The only permitted type inside the states subtree " + x + " is a string")

    # marked is separate, because it's a list of lists
    marked = states["marked"]
    if not isinstance(marked, list):
        raise Exception("The marked states should be a list of lists")

    for x in marked:
        if not isinstance(marked, list):
            raise Exception("The marked states should be a list of lists")
        for state in x:
            if not isinstance(state, str):
                raise Exception("The only permitted type inside the marked states list is a string")

    # 2: EVENTS
    events = automaton["events"]
    if not isinstance(events, dict):
        raise Exception("The events subtree must be a dictionary structure")

    for x in ["all", "controllable", "observable"]:
        if x not in events:
            raise Exception("The events subtree must have a key for " + x)

    for x in ["all"]:
        for event in events[x]:
            if not isinstance(event, str):
                raise Exception("The only permitted type inside the events subtree " + x + " is a string")

    for x in ["observable", "controllable"]:
        if not isinstance(events[x], list):
            raise Exception("The " + x + " area must be a list-of-lists-of-strings structure")

        for lst in events[x]:
            if not isinstance(lst, list):
                raise Exception("The " + x + " area must be a list-of-lists-of-strings structure")
            for event in lst:
                if not isinstance(event, str):
                    raise Exception("The only permitted type inside the " + x + " list-of-lists is a string")

    if len(events["observable"]) != len(events["controllable"]):
        raise Exception(
            "There must be the same number of lists within both observable and controllable (one for each player in the system)")

    # 3: Transitions
    trans = automaton["transitions"]
    if not isinstance(trans, dict):
        raise Exception("The transitions subtree must be a dictionary structure")

    for x in ["all", "bad"]:
        if x not in trans:
            raise Exception("The transitions subtree must have a key for " + x)
        # Make sure it's a dict
        if not isinstance(trans[x], dict):
            raise Exception("The transitions subtree " + x + " must be a dictionary structure")
        # Make sure all entries are lists
        for key, value in trans[x].items():
            if not isinstance(value, list):
                raise Exception("The values for transitions must be lists of strings")
            for state in value:
                if not isinstance(state, str):
                    raise Exception("The values for transitions must be lists of strings")
    return True
