"""
In-memory collection of famous quotes used by the remote MCP server.

Each quote is a dict with 'autor' and 'frase' keys.  The helper
functions keep the MCP tool layer (server.py) clean.
"""

import random
from typing import Any

FRASES: list[dict[str, str]] = [
    {"autor": "Albert Einstein", "frase": "La imaginación es más importante que el conocimiento."},
    {"autor": "Albert Einstein", "frase": "La vida es como andar en bicicleta. Para mantener el equilibrio, debes seguir adelante."},
    {"autor": "Mahatma Gandhi", "frase": "Sé el cambio que quieres ver en el mundo."},
    {"autor": "Mahatma Gandhi", "frase": "La fuerza no proviene de la capacidad física, sino de una voluntad indomable."},
    {"autor": "Martin Luther King Jr.", "frase": "Tengo un sueño: que mis cuatro hijos pequeños vivirán un día en una nación donde no serán juzgados por el color de su piel."},
    {"autor": "Nelson Mandela", "frase": "La educación es el arma más poderosa que puedes usar para cambiar el mundo."},
    {"autor": "Nelson Mandela", "frase": "Siempre parece imposible hasta que se hace."},
    {"autor": "Steve Jobs", "frase": "Tu tiempo es limitado, no lo desperdicies viviendo la vida de alguien más."},
    {"autor": "Steve Jobs", "frase": "Mantente hambriento. Mantente alocado."},
    {"autor": "Frida Kahlo", "frase": "Pies, ¿para qué los quiero si tengo alas para volar?"},
    {"autor": "Gabriel García Márquez", "frase": "No llores porque ya se terminó, sonríe porque sucedió."},
    {"autor": "Gabriel García Márquez", "frase": "La vida no es la que uno vivió, sino la que uno recuerda y cómo la recuerda para contarla."},
    {"autor": "Mario Benedetti", "frase": "De vez en cuando hay que hacer una pausa, contemplarse a sí mismo sin la fruición cotidiana."},
    {"autor": "Pablo Neruda", "frase": "Puedes cortar todas las flores, pero no puedes impedir que llegue la primavera."},
    {"autor": "Sócrates", "frase": "Solo sé que no sé nada."},
    {"autor": "Aristóteles", "frase": "Somos lo que hacemos repetidamente. La excelencia, entonces, no es un acto, sino un hábito."},
    {"autor": "Confucio", "frase": "No importa lo lento que vayas, siempre y cuando no te detengas."},
    {"autor": "Oscar Wilde", "frase": "Sé tú mismo; todos los demás ya están ocupados."},
    {"autor": "Mark Twain", "frase": "El secreto de progresar es empezar."},
    {"autor": "Walt Disney", "frase": "Si puedes soñarlo, puedes hacerlo."},
]


def frase_aleatoria() -> dict[str, str]:
    """Return a single random quote."""
    return random.choice(FRASES)


def buscar(texto: str) -> list[dict[str, str]]:
    """Search quotes by author name or keyword (case-insensitive)."""
    texto_lower = texto.lower()
    return [
        f for f in FRASES
        if texto_lower in f["autor"].lower() or texto_lower in f["frase"].lower()
    ]
