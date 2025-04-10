from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd

# Estados y alfabeto
states = ['q0', 'q1', 'q2', 'qf']
alphabet = ['0', '1']
initial_state = 'q0'
accepting_states = ['qf']

# Transiciones no deterministas
transition_function = {
    'q0': {'0': ['q0', 'q1'], '1': ['q0', 'q2']},
    'q1': {'1': ['qf'], '0': ['q1']},
    'q2': {'0': ['qf'], '1': ['q2']},
    'qf': {'0': ['qf'], '1': ['qf']}  
}

# Simulación del AFND
def run_afnd(input_string):
    current_states = [initial_state]

    for symbol in input_string:
        next_states = []
        for state in current_states:
            if symbol in transition_function[state]:
                next_states.extend(transition_function[state][symbol])
        current_states = list(set(next_states))  # eliminar duplicados
        if not current_states:
            break

    return any(state in accepting_states for state in current_states)

# Diagrama de estados
def draw_afnd_diagram():
    dot = Digraph(format="png")
    dot.attr(rankdir='LR')  

    dot.node('', shape="none")  # Nodo invisible para inicio

    for state in states:
        shape = 'doublecircle' if state in accepting_states else 'circle'
        dot.node(state, shape=shape)

    dot.edge('', initial_state)

    for from_state, transitions in transition_function.items():
        for symbol, to_states in transitions.items():
            for to_state in to_states:
                dot.edge(from_state, to_state, label=symbol)

    dot.render("afnd_diagrama", cleanup=True)
    print("✅ Diagrama AFND guardado como 'afnd_diagrama.png'.")

# Tabla de transición (como imagen)
def draw_transition_table():
    data = []
    for state in states:
        row = []
        for symbol in alphabet:
            to_states = transition_function[state].get(symbol, [])
            row.append(", ".join(to_states) if to_states else "-")
        data.append(row)

    df = pd.DataFrame(data, index=states, columns=alphabet)

    pretty_index = []
    for state in states:
        label = ""
        if state == initial_state:
            label += "→ "
        if state in accepting_states:
            label += "*"
        label += state
        pretty_index.append(label)
    df.index = pretty_index

    fig, ax = plt.subplots()
    ax.axis('off')
    table = ax.table(cellText=df.values,
                     rowLabels=df.index,
                     colLabels=["0", "1"],
                     cellLoc='center',
                     loc='center')

    table.scale(1, 2)
    table.auto_set_font_size(False)
    table.set_fontsize(14)
    plt.title("Tabla de Transición (AFND)", fontsize=16, pad=20)
    plt.savefig("afnd_tabla_transicion.png", bbox_inches='tight')
    print("✅ Tabla de transición guardada como 'afnd_tabla_transicion.png'.")

# ▶Ejecutar
if __name__ == "__main__":
    draw_afnd_diagram()
    draw_transition_table()

    while True:
        cadena = input("\n🔠 Ingresá una cadena binaria (0s y 1s) o 'salir': ")
        if cadena.lower() == 'salir':
            break
        elif all(c in alphabet for c in cadena):
            if run_afnd(cadena):
                print("✅ Cadena ACEPTADA (contiene '01' o '10')\n")
            else:
                print("❌ Cadena NO aceptada\n")
        else:
            print("⚠️ Solo se permiten caracteres '0' y '1'.")
