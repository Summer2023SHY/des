from json import dumps

from structure_validation.automaton_validator import Automaton


def get_states(states: list[str], chosen_so_far: list = []) -> list[str]:
    """A list of current states for multiple automata in a composed system (i.e.,
    a "macro-state") has some states which are non-deterministic: that is, the
    state might be ["q1", ["q2", "q3"]]. We want to find all distinct states,
    so we want ["q1", "q2"] and ["q1", "q3"]. This becomes a major task when
    there are many options for many automata, leading to a combinatorial
    explosion.

    Parameters
    ----------
    states : array of strings, or array of arrays of strings
        Array of all states (or possible states)

    Returns
    -------
    Array of arrays of strings
        All possible macro-states

    Examples
    --------
    >>> print(get_states(["q1", ["q2", "q3"]]))
    [["q1", "q2"], ["q1", "q3"]]
    """
    index = len(chosen_so_far)

    # Base case
    if index == len(states):
        return [chosen_so_far.copy()]

    macro_states = []
    for option in states[index]:
        chosen_so_far.append(option)
        macro_states.extend(get_states(states, chosen_so_far))
        chosen_so_far.pop()
    return macro_states


def format_state(states: list[str]) -> str:
    """Creates a macro-state string containing all of the states passed in.

    Parameters
    ----------
    states : array of strings
        Array of all the states to put together

    Returns
    -------
    string
        The string representing the macro-state

    Examples
    --------
    >>> print(format_state(["q1"]))
    "(q1)"
    >>> print(format_state(["q1", "q2", "(q3, q4)"]))
    "(q1, q2, (q3, q4))"
    """
    str = "("
    for state in states:
        str += state + ", "
    str = str[0:-2]  # take off last comma
    str += ")"
    return str


def format_state_set(states: list[str]) -> str:
    """Creates a macro-state string containing all of the states passed in as a
    set.

    Parameters
    ----------
    states : array of strings
        Array of all the states to put together

    Returns
    -------
    string
        The string representing the macro-state

    Examples
    --------
    >>> print(format_state(["q1"]))
    "(q1)"
    >>> print(format_state(["q1", "q2", "(q3, q4)"]))
    "{q1, q2, (q3, q4)}"
    """
    states.sort()
    str = "{"
    for state in states:
        str += state + ", "
    str = str[0:-2]  # take off last comma
    str += "}"
    return str


def format_event_vector(events: list[str]) -> str:
    """Formats an event vector into a format with angle brackets.

    Parameters
    ----------
    events : list
            List of strings representing the events to put together

    Returns
    -------
    str
            The string representing the event
    """
    s = "["
    for e in events:
        s += e + ", "
    s = s[:-2]
    s += "]"
    return s


def format_transition(state: str, event: str) -> str:
    """Formats a state and event into the proper format for a transition,
    which is used as a key in the transition dictionary.

    Parameters
    ----------
    state : string
        The state the transition originates from
    event : string
        The event prompting the state change

    Returns
    -------
    string
        The string representing the transition's key for the dictionary

    Examples
    --------
    >>> print(format_transition("q1", "a"))
    "q1->a"
    >>> print(format_transition("(q1, q5)", "c"))
    "(q1, q5)->c"
    """
    return state + "->" + event


def format_observed_secrets(observer: str, observed_secrets: list) -> str:
    """Formats an observer's observation of other agents' secrets

    Parameters
    ----------
    observer : str
        The observer that has identified secrets
    observed_secrets : list
        List of identified secrets

    Returns
    -------
    str
        The string representing the agent's observations
    """
    lst = ""
    for x in observed_secrets:
        lst += ", " + str(x)
    if len(lst) > 2:
        lst = lst[2:]
    return str(observer) + "->" + "{" + lst + "}"


def format_all_observed_secrets(lst: list) -> str:
    """Formats all observers' observations of other agents' secrets

    Parameters
    ----------
    lst : list
        List of observations (see format_observed_secrets).

    Returns
    -------
    str
        The string representing all agents' observations
    """
    secrets = [format_observed_secrets(*x) for x in lst]
    secrets.sort()
    result = ""
    for s in secrets:
        result += ", " + s
    if len(result) > 2:
        result = result[2:]
    return result


def extract_state(transition: str) -> str:
    """Extracts the name of the origin state given a string representing a
    transition.

    Parameters
    ----------
    transition : str
        A transition

    Returns
    -------
    str
        The corresponding state from the transition
    """
    return transition.split("->", 1)[0]


def extract_event(transition: str) -> str:
    """Extracts the name of the event given a string representing a
    transition.

    Parameters
    ----------
    transition : str
        A transition

    Returns
    -------
    str
        The corresponding event from the transition
    """
    return transition.split("->", 1)[1]


def pretty_print(automaton: Automaton) -> None:
    """
    Formats an automaton in an attractive way and prints as text.

    Parameters
    ----------
    automaton : dict
        The automaton to print

    Returns
    -------
    None
    """
    print(dumps(automaton, sort_keys=True, indent=4))
