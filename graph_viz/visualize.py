from graphviz import Digraph
from graph_viz.event_legend import generate_event_legend
from basic_ops.helpers.string_helpers import extract_state, extract_event
import global_settings

from structure_validation.automaton_validator import Automaton

def __identify_secret(automaton: Automaton, state: str):
    """Identifies the observers for which the state is a secret state and
    returns a string describing the indexes of those observers.

    Parameters
    ----------
    automaton : dict
        The automaton for which to find secret states
    state : str
        The string representing the current (possibly secret) state

    Returns
    -------
    str
        String representing all observers for which the state is secret
    """
    # First, check if the automaton has a special "secrets" section which
    # specifies what states have what secrets
    if "secrets" in automaton["states"]:
        secrets = automaton["states"]["secrets"]
        if state in secrets:
            return "\n" + secrets[state]
        else:
            return ""
    # Otherwise, just figure out which agents marked the state.
    else:
        marked = ""
        marked_list = automaton["states"]["marked"]
        for i in range(len(marked_list)):
            if state in marked_list[i]:
                marked += str(i) + ", "

        if len(marked) == 0:
            return marked
        return "\nSecret for agent(s): " + marked[:-2]


def visualize(automaton: Automaton, location: str=None, view: bool=True):
    """Turns an automaton into a viewable PDF and saves it to the location.
    It also opens the default PDF viewer.

    Parameters
    ----------
    automaton : dict
        The dictionary representing the automaton
    location : str
        The path with which to save the automaton's image
    view : bool
        Whether or not to show the visualized image

    Returns
    -------
    None
    """
    dot = Digraph(automaton["name"])

    # Add all states
    for state in automaton["states"]["all"]:
        secret = __identify_secret(automaton, state)
        num_circles = "1"
        if len(secret) > 0:
            num_circles = "2"

        if "v2" in automaton["states"] and state in automaton["states"]["v2"]:
            if state in automaton["states"]["bad"]:
                dot.node(state, label=state+secret, shape="box", color="red", peripheries=num_circles)
            else:
                dot.node(state, label=state+secret, shape="box", color="black", peripheries=num_circles)
        else:
            if state in automaton["states"]["bad"]:
                dot.node(state, label=state+secret, shape="ellipse", color="red", peripheries=num_circles)
            else:
                dot.node(state, label=state+secret, shape="ellipse", color="black", peripheries=num_circles)

    for state in automaton["states"]["initial"]:
        invisible = state + "-invisible"
        dot.node(invisible, style="invis")
        dot.edge(invisible, state)

    for k, v in automaton["transitions"]["all"].items():
        from_state = extract_state(k)
        event = extract_event(k)
        for to_state in v:
            dot.edge(from_state, to_state, label=event)

    dot.body.append(generate_event_legend(automaton["events"]))
    file_type = global_settings.settings["graphviz_file_type"]
    if location is not None:
        dot.render(location, view=view, format=file_type)
    else:
        dot.render(view=view, format=file_type)
