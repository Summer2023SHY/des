def get_initial(automata, initial_so_far = []):
    '''Gets all possible combinations of intitial states for two the
    automata. It does this recursively to find all combinations.

    Note
    ----
    Assumes that all automata have at least one initial state.

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Yields
    ------
    list
        A list of all possible initial state combinations

    Examples
    --------
    >>> initial = get_initial([automaton1, automaton2])
    >>> print(initial)
    [
        "(q1, q3)", "(q1, q4)", "(q2, q3)", "(q2, q4)"
    ]
    '''
    # If we already have a fully defined initial state, format and return
    if len(initial_so_far) == len(automata):
        return [initial_so_far.copy()]

    # Otherwise, recursively choose all combinations of initial states
    result = []
    index = len(initial_so_far)
    initial_so_far.append("")

    # Go through every possible initial state
    for state in automata[index]["states"]["initial"]:
        initial_so_far[index] = state
        # Add on to the list of possible initial states
        result += get_initial(automata, initial_so_far)
    initial_so_far.pop() # Remove the element we added
    return result

def check_marked(automata, state):
    '''Checks if a state should be marked, where the state is a macro-state
    composed of states from the automata passed as a parameter. If at least one
    automaton has the state marked, returns true.

    Parameters
    ----------
    automata : array of dictionaries
        Array of all of the automata which should be composed

    Yields
    ------
    boolean
        If the state should be marked, true; else, false

    Examples
    --------
    >>> check_marked([automaton1, automaton2], ["q1", "q2"])
    True
    '''
    for i in range(len(automata)):
        if state[i] in automata[i]["states"]["marked"]:
            return True
    return False

def check_marked_inverse(automaton, state):
    '''Checks if a state should be marked, where the state is a macro-state
    composed of states from the SINGLE automaton passed as a parameter. If at
    least one component state is NOT marked, returns false.
    This function exists for checking for opacity, since opacity is maintained
    when there is at least one state which does not give away the secret (i.e.,
    there is at least one state which is not marked).

    Parameters
    ----------
    automata : dictionary
        The automaton to check

    Yields
    ------
    boolean
        If the state should be marked, true; else, false

    Examples
    --------
    >>> check_marked([automaton1, automaton2], ["q1", "q2"])
    True
    '''
    for s in state:
        if s not in automaton["states"]["marked"]:
            return False
    return True
