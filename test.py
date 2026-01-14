"""
Progetto Python di esempio per testare SonarQube
Contiene vari pattern di codice per verificare le capacità di analisi
"""

import os
import json
from typing import List, Optional


class Calculator:
    """Calcolatrice con vari metodi per test"""
    
    def add(self, a: int, b: int) -> int:
        """Somma due numeri"""
        return a + b
    
    def divide(self, a: int, b: int) -> float:
        """Divide due numeri - contiene bug potenziale"""
        # Bug: nessun controllo divisione per zero
        return a / b
    
    def complex_method(self, x, y, z):
        """Metodo con alta complessità ciclomatica"""
        if x > 0:
            if y > 0:
                if z > 0:
                    return x + y + z
                else:
                    return x + y
            else:
                if z > 0:
                    return x + z
                else:
                    return x
        else:
            if y > 0:
                if z > 0:
                    return y + z
                else:
                    return y
            else:
                if z > 0:
                    return z
                else:
                    return 0


class UserManager:
    """Gestione utenti con problemi di sicurezza"""
    
    def __init__(self):
        self.users = {}
        self.password = "admin123"  # Hardcoded password - security issue
    
    def add_user(self, username, password):
        """Aggiunge utente - problemi di sicurezza"""
        # Nessun hashing della password
        self.users[username] = password
        return True
    
    def authenticate(self, username, password):
        """Autentica utente"""
        if username in self.users:
            # Comparazione diretta - no constant-time comparison
            return self.users[username] == password
        return False
    
    def sql_query(self, user_input):
        """Query SQL non sicura - SQL injection vulnerability"""
        query = f"SELECT * FROM users WHERE name = '{user_input}'"
        return query


def unused_function():
    """Funzione non utilizzata - dead code"""
    x = 10
    y = 20
    return x + y


def duplicate_code_1(items):
    """Codice duplicato - esempio 1"""
    total = 0
    for item in items:
        if item > 0:
            total += item
    return total


def duplicate_code_2(values):
    """Codice duplicato - esempio 2"""
    total = 0
    for value in values:
        if value > 0:
            total += value
    return total


class FileHandler:
    """Gestione file con problemi"""
    
    def read_file(self, filepath):
        """Legge file senza gestione eccezioni"""
        # Nessun try-except
        f = open(filepath, 'r')  # File handle non chiuso
        content = f.read()
        return content
    
    def write_file(self, filepath, content):
        """Scrive file"""
        with open(filepath, 'w') as f:
            f.write(content)


def magic_numbers_example(value):
    """Funzione con magic numbers"""
    if value > 100:  # Magic number
        return value * 1.5  # Magic number
    elif value > 50:  # Magic number
        return value * 1.2  # Magic number
    else:
        return value


class TodoItem:
    """Classe con TODO e FIXME"""
    
    def __init__(self, title, description):
        self.title = title
        self.description = description
        # TODO: Aggiungere validazione
        # FIXME: Questo metodo non gestisce descrizioni vuote
    
    def process(self):
        """Processa l'item"""
        # XXX: Implementare correttamente
        pass


def print_debug_info(data):
    """Funzione con print statements - code smell"""
    print("Debug: processing data")  # Non usare print in produzione
    print(f"Data received: {data}")
    result = len(data)
    print(f"Result: {result}")
    return result


def main():
    """Funzione principale per testare il codice"""
    calc = Calculator()
    
    # Test normali
    print(f"Add: {calc.add(5, 3)}")
    
    # Test che causa errore
    try:
        print(f"Divide: {calc.divide(10, 0)}")
    except ZeroDivisionError:
        print("Errore: divisione per zero")
    
    # Test UserManager
    um = UserManager()
    um.add_user("admin", "password123")
    
    # Test SQL injection vulnerability
    malicious_input = "admin' OR '1'='1"
    query = um.sql_query(malicious_input)
    print(f"Query: {query}")
    
    # Test duplicate code
    numbers = [1, 2, 3, -1, 4, -2]
    print(f"Total 1: {duplicate_code_1(numbers)}")
    print(f"Total 2: {duplicate_code_2(numbers)}")


if __name__ == "__main__":
    main()
