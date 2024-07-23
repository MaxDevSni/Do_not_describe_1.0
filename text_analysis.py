# Kód pro vlastní textovou analýzu

import re


class TextAnalyzer:
    @staticmethod
    def find_matching_sequences(text_OBZ, text_R):
        # Normalizace textů: odstranění interpunkce a změna na malá písmena
        text_OBZ_normalized = re.sub(r'[^\w\s]', '', text_OBZ).lower()
        text_R_normalized = re.sub(r'[^\w\s]', '', text_R).lower()

        # Rozdělení normalizovaných textů na slova
        words_OBZ = text_OBZ_normalized.split()
        words_R = text_R_normalized.split()

        # Inicializace seznamu pro shodné sekvence slov
        matches = []

        # Procházení slov v prvním textu
        for word1 in words_OBZ:
            # Procházení slov ve druhém textu
            for word2 in words_R:
                # Kontrola shody slov
                if word1 == word2:
                    matches.append(word1)  # Přidání shodného slova do seznamu
                    break  # Přerušení vnitřní smyčky pro zrychlení vyhledávání

        # Vytvoření souvislého textu ze shodných sekvencí slov
        matching_text = ' '.join(matches)

        # Výpočet procentuální shody
        percent_match = len(matches) / max(len(words_OBZ), len(words_R)) * 100

        # Vrácení výsledků
        return matching_text, percent_match
