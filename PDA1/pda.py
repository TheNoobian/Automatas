from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd

# Estados y símbolos
states = ['q0', 'q1', 'q2', 'q3']
input_alphabet = ['a', 'b']
stack_alphabet = ['A']
initial_state = 'q0'
accepting_states = ['q3']

# Transiciones exactas como el grafo
transition_function = {
    ('q0', 'a', ''): [('q1', ['A'])],
    ('q1', 'a', ''): [('q1', ['A'])],
    ('q1', 'b', 'A'): [('q2', []), ('q3', [])],
    ('q2', 'b', 'A'): [('q2', []), ('q3', [])],
}

# Simulación (no determinista)
def run_pda(input_string):
    configs = [(0, initial_state, [])]  # posición, estado, pila

    while configs:
        pos, state, stack = configs.pop()

        if pos == len(input_string) and state in accepting_states:
            return True

        symbol = input_string[pos] if pos < len(input_string) else ''
        top = stack[-1] if stack else ''

        for (s, a, t), nexts in transition_function.items():
            if s == state and a == symbol and (t == top or t == ''):
                for (new_state, push_stack) in nexts:
                    new_stack = stack[:]
                    if t != '':
                        new_stack.pop()
                    new_stack += push_stack
                    configs.append((pos + 1, new_state, new_stack))

    return False

# Diagrama visual del AP
def draw_pda_diagram():
    dot = Digraph(format="png")
    dot.attr(rankdir='LR')
    dot.node('', shape="none")

    for state in states:
        shape = 'doublecircle' if state in accepting_states else 'circle'
        dot.node(state, shape=shape)
    dot.edge('', initial_state)

    for (from_state, symbol, top), targets in transition_function.items():
        for (to_state, push_stack) in targets:
            label = f"{symbol}, {top if top else 'λ'} ; {''.join(push_stack) if push_stack else 'λ'}"
            dot.edge(from_state, to_state, label=label)

    dot.render("apnd_grafo_fiel.png", cleanup=True)
    print("✅ Diagrama guardado como 'apnd_grafo_fiel.png'.")

# Tabla tipo informe
def draw_transition_table():
    rows = []
    for (state, symbol, top), targets in transition_function.items():
        for (to_state, push_stack) in targets:
            action = ''.join(push_stack) if push_stack else 'λ'
            rows.append([state, symbol, top if top else 'λ', to_state, action])

    df = pd.DataFrame(rows, columns=['Estado', 'Símbolo', 'Tope pila', 'Nuevo estado', 'Acción'])

    fig, ax = plt.subplots()
    ax.axis('off')
    table = ax.table(cellText=df.values,
                     colLabels=df.columns,
                     cellLoc='center',
                     loc='center')
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1.2, 1.5)
    plt.title("Tabla de Transición (APND - aⁿbⁿ)", fontsize=14, pad=20)
    plt.savefig("apnd_tabla_fiel.png", bbox_inches='tight')
    print("✅ Tabla guardada como 'apnd_tabla_fiel.png'.")

# Ejecutar
if __name__ == "__main__":
    draw_pda_diagram()
    draw_transition_table()

    while True:
        cadena = input("\n🔠 Ingresá una cadena con a/b (o 'salir'): ")
        if cadena.lower() == 'salir':
            break
        elif all(c in input_alphabet for c in cadena):
            if run_pda(cadena):
                print("✅ Cadena ACEPTADA por el APND\n")
            else:
                print("❌ Cadena NO aceptada\n")
        else:
            print("⚠️ Solo se permiten letras 'a' y 'b'.")
