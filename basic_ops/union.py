import basic_ops.helpers.union_helpers as helper
from structure_validation.automaton_validator import Automaton


def union(automata: list[Automaton]) -> Automaton:
    """Composes two or more finite state automata.

    Specifically, the union operation synchronizes all of the automata on their
    common events, allowing private events regardless.

    Note
    ----
    Any data on bad states or transitions will be not be included in the
    resulting automaton.
    Also, all automata must have the same number of players in the system which
    have sets of controllable and observable events.
    TODO: add a verifier to ensure correct input.

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Returns
    -------
    dict
        The resulting composed automaton

    Examples
    --------
    Assume a list of file names of JSON automata exists, called filenames.

    >>> import json
    >>> automata = [{}] * len(filenames)
    >>> if filenames:
    >>>     for i in range(len(filenames)):
    >>>         with open(filenames[i], 'r') as f:
    >>>             automata[i] = json.load(f)
    >>> new_automaton = union(automata)
    >>> print(new_automaton)
    {
        # Dictionary for an automaton
    }
    """
    new_automaton = {}
    # First, get all events in the new automaton by unioning sets
    new_automaton["events"] = helper.union_events(automata)
    # Then, update the transition function and add all of the states
    new_automaton.update(helper.union_transitions(automata, new_automaton["events"]["all"]))

    return new_automaton
