import sqlite3
import numpy as np

class DatabaseManager:
    def __init__(self, db_name="results.db"):
        # Připojení k databázi (vytvoří novou databázi, pokud neexistuje)
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        # Vytvoření tabulky 'results', pokud ještě neexistuje
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS results
                                 (id INTEGER PRIMARY KEY,
                                  text1 TEXT,
                                  text2 TEXT,
                                  matching_text TEXT,
                                  percent_match REAL)''')

    def insert_result(self, text1, text2, matching_text, percent_match):
        # Vložení výsledku do tabulky 'results'
        with self.conn:
            self.conn.execute("INSERT INTO results (text1, text2, matching_text, percent_match) VALUES (?, ?, ?, ?)",
                              (text1, text2, matching_text, percent_match))

    def get_statistics(self):
        # Získání statistických údajů z tabulky 'results'
        with self.conn:
            cursor = self.conn.cursor()
            cursor.execute("SELECT percent_match FROM results")
            rows = cursor.fetchall()
            if rows:
                # Výpočet statistických údajů z procentuální shody
                percent_matches = [row[0] for row in rows]
                count = len(percent_matches)
                mean = np.mean(percent_matches)
                median = np.median(percent_matches)
                min_val = np.min(percent_matches)
                max_val = np.max(percent_matches)
                first_quartile = np.percentile(percent_matches, 25)
                third_quartile = np.percentile(percent_matches, 75)
                return {
                    "count": count,
                    "mean": mean,
                    "median": median,
                    "min_val": min_val,
                    "max_val": max_val,
                    "first_quartile": first_quartile,
                    "third_quartile": third_quartile
                }
            else:
                return None

    def delete_all_data(self):
        # Vymazání všech dat z tabulky 'results' a optimalizace databáze
        with self.conn:
            self.conn.execute("DELETE FROM results")
        self.conn.execute("VACUUM")

    def close(self):
        # Uzavření připojení k databázi
        self.conn.close()
