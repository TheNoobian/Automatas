from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd

# AFD: acepta cadenas que terminan en '11'
states = ['q0', 'q1', 'q2']
alphabet = ['0', '1']
initial_state = 'q0'
accepting_states = ['q2']
transition_function = {
    'q0': {'0': 'q0', '1': 'q1'},
    'q1': {'0': 'q0', '1': 'q2'},
    'q2': {'0': 'q0', '1': 'q2'}
}

# Verifica si una cadena es aceptada
def run_afd(input_string):
    state = initial_state
    for symbol in input_string:
        if symbol not in alphabet:
            return False
        state = transition_function[state][symbol]
    return state in accepting_states

# Genera diagrama de estados (horizontal)
def draw_afd_diagram():
    dot = Digraph(format="png")
    dot.attr(rankdir='LR')  

    # Nodo invisible para la flecha de inicio
    dot.node('', shape="none")

    for state in states:
        shape = 'doublecircle' if state in accepting_states else 'circle'
        dot.node(state, shape=shape)

    dot.edge('', initial_state)

    for from_state, transitions in transition_function.items():
        for symbol, to_state in transitions.items():
            dot.edge(from_state, to_state, label=symbol)

    dot.render("afd_diagrama", cleanup=True)
    print("✅ Diagrama de estados guardado como 'afd_diagrama.png'.")

# Genera imagen con tabla de transición
def draw_transition_table():
    data = []
    for state in states:
        row = []
        for symbol in alphabet:
            row.append(transition_function[state][symbol])
        data.append(row)

    df = pd.DataFrame(data, index=states, columns=alphabet)

    # Agrega símbolos a estados (flecha en inicial, asterisco en aceptación)
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
    plt.title("Tabla de Transición", fontsize=16, pad=20)
    plt.savefig("afd_tabla_transicion.png", bbox_inches='tight')
    print("✅ Tabla de transición guardada como 'afd_tabla_transicion.png'.")

# ▶️ Ejecutar todo
if __name__ == "__main__":
    draw_afd_diagram()
    draw_transition_table()

    while True:
        cadena = input("\n🔠 Ingresá una cadena binaria (0s y 1s) o 'salir': ")
        if cadena.lower() == 'salir':
            break
        elif all(c in alphabet for c in cadena):
            if run_afd(cadena):
                print("✅ Cadena ACEPTADA (termina en '11')\n")
            else:
                print("❌ Cadena NO aceptada\n")
        else:
            print("⚠️ Solo se permiten caracteres '0' y '1'.")
