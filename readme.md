# Autómatas - Teoría de la Computación 👩‍💻

Este repositorio contiene la implementación **programada** de distintos tipos de autómatas desarrollados para el trabajo práctico de la materia **Teoría de la Computación** (Ingeniería en Sistemas). Se incluyen:

- AFD (Autómata Finito Determinista)
- AFND (Autómata Finito No Determinista)
- AP (Autómata a Pila - No determinista)

---

## 📂 Estructura del proyecto

```
.
├── AFD
│   ├── AFD.py
│   ├── afd_diagrama.png
│   └── afd_table_transicion.png
│
├── AFND dificil
│   ├── afndDificil.py
│   ├── afnd_diagrama.png
│   └── afnd_tabla_transicion.png
│
├── AFND facil
│   ├── afndFacil.py
│   ├── afnd_termina_en_1.png
│   └── afnd_tabla_termina_en_1.png
│
├── PDA1
│   ├── pda.py
│   ├── apnd_grafo_fiel.png
│   └── apnd_tabla_fiel.png
│
└── PDA2
    ├── pda2.py
    ├── pda_palindromo_c.png
    └── pda_tabla_palindromo_c.png
```

---

## 📘 Descripción de cada autómata

### ✅ AFD - Reconocimiento de cadenas que terminan en `11`
- Carpeta: `AFD/`
- Lógica: acepta si la cadena binaria termina en `11`.
- Incluye simulador interactivo y generación automática de diagrama y tabla de transición.

---

### ✅ AFND difícil - Lenguaje con no determinismo real
- Carpeta: `AFND dificil/`
- Lógica: acepta cadenas con ciertos patrones como `"01"` o `"10"` usando caminos paralelos no deterministas.

---

### ✅ AFND fácil - Cadenas que terminan en `1`
- Carpeta: `AFND facil/`
- Lógica: acepta cualquier cadena binaria que finalice en `1`.
- Implementación sencilla y clara de no determinismo.

---

### ✅ PDA1 - Lenguaje `aⁿbⁿ`, usando pila
- Carpeta: `PDA1/`
- Lógica: apila `A` por cada `a` y desapila por cada `b`.
- Acepta si la pila queda vacía en estado de aceptación `q3`.
- Diseño 100% fiel al grafo dado por el estudiante.

---

### ✅ PDA2 - Palíndromos del tipo `w c wᴿ`
- Carpeta: `PDA2/`
- Lógica: apila `a/b`, cambia de estado al leer `c`, y desapila en orden inverso.
- Acepta cadenas simétricas como `aca`, `aabcbaa`, etc.

---

## 🛠 Cómo ejecutar

1. Asegurate de tener Python instalado.
2. Ejecutá cualquier archivo `.py` con:

```bash
python nombreDelArchivo.py
```

3. Se generarán automáticamente:
   - El **diagrama** del autómata (`.png`)
   - La **tabla de transición** (`.png`)
   - Una interfaz para ingresar cadenas e interactuar

---

## 📚 Bibliografía de referencia

- Hopcroft, J. E., Motwani, R., Ullman, J. D. (2007). *Introduction to Automata Theory, Languages and Computation*.
- Libros PDF provistos por la cátedra.

---
