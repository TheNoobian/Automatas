from graphviz import Digraph
import matplotlib.pyplot as plt
import pandas as pd

states = ['q0', 'q1']
input_alphabet = ['a', 'b', 'c']
stack_alphabet = ['#', 'a', 'b']
initial_state = 'q0'
accepting_states = ['q1']
initial_stack_symbol = '#'

transition_function = {
    ('->q0', 'a', 'λ'): [('q0', ['a'])],     # apilar a
    ('q0', 'b', 'λ'): [('q0', ['b'])],     # apilar b
    ('q0', 'c', 'λ'): [('q1', [])],        # cambio de estado sin tocar pila
    ('q1', 'a', 'a'): [('q1', [])],        # desapilar a
    ('q1', 'b', 'b'): [('q1', [])],        # desapilar b
}

def run_pda(input_string):
    stack = []
    configs = [(0, initial_state, stack[:])]

    while configs:
        pos, state, stack = configs.pop()

        # Acepta si terminó la entrada y la pila está vacía en estado final
        if pos == len(input_string) and not stack and state in accepting_states:
            return True

        if pos >= len(input_string):
            continue

        symbol = input_string[pos]
        top = stack[-1] if stack else 'λ'

        for (s, a, t), nexts in transition_function.items():
            if s == state and a == symbol and (t == top or t == 'λ'):
                for (new_state, push_stack) in nexts:
                    new_stack = stack[:]
                    if t != 'λ':
                        new_stack.pop()
                    new_stack += push_stack
                    configs.append((pos + 1, new_state, new_stack))

    return False

def draw_pda_diagram():
    dot = Digraph(format="png")
    dot.attr(rankdir='LR')

    dot.node('', shape="none")
    for state in states:
        shape = 'doublecircle' if state in accepting_states else 'circle'
        dot.node(state, shape=shape)
    dot.edge('', initial_state)

    for (from_state, symbol, stack_top), targets in transition_function.items():
        for (to_state, push_stack) in targets:
            action = ''.join(push_stack) if push_stack else 'λ'
            label = f"{symbol}, {stack_top} / {action}"
            dot.edge(from_state, to_state, label=label)

    dot.render("pda_palindromo_c.png", cleanup=True)
    print("✅ Diagrama guardado como 'pda_palindromo_c.png'.")

# Tabla de transición
def draw_transition_table():
    rows = []
    for (state, symbol, stack_top), targets in transition_function.items():
        for (to_state, push_stack) in targets:
            action = ''.join(push_stack) if push_stack else 'λ'
            rows.append([state, symbol, stack_top, to_state, action])

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
    plt.title("Tabla de Transición (AP - w c wᴿ)", fontsize=14, pad=20)
    plt.savefig("pda_tabla_palindromo_c.png", bbox_inches='tight')
    print("✅ Tabla guardada como 'pda_tabla_palindromo_c.png'.")

if __name__ == "__main__":
    draw_pda_diagram()
    draw_transition_table()

    while True:
        cadena = input("\n🔠 Ingresá una cadena con a/b/c (o 'salir'): ")
        if cadena.lower() == 'salir':
            break
        elif all(c in input_alphabet for c in cadena):
            if run_pda(cadena):
                print("✅ Cadena ACEPTADA (forma w c wᴿ)\n")
            else:
                print("❌ Cadena NO aceptada\n")
        else:
            print("⚠️ Solo se permiten letras 'a', 'b' y 'c'.")
