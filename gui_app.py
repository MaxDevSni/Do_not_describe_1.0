import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout, QTextEdit, QPushButton, QMessageBox
from PyQt5.QtCore import QSize
from text_analysis import TextAnalyzer
from database_manager import DatabaseManager

class TextComparerApp(QWidget):
    def __init__(self):
        super().__init__()
        print("Initializing TextComparerApp")  # Debug print
        self.db_manager = DatabaseManager()  # Inicializace správce databáze
        self.initUI()  # Inicializace uživatelského rozhraní

    def initUI(self):
        print("Setting up UI")  # Debug print
        layout = QVBoxLayout()

        try:
            # První textové pole pro vložení textu
            self.text1 = QTextEdit(self)
            self.text1.setPlaceholderText("Vložte první text...")
            layout.addWidget(self.text1)

            # Druhé textové pole pro vložení textu
            self.text2 = QTextEdit(self)
            self.text2.setPlaceholderText("Vložte druhý text...")
            layout.addWidget(self.text2)

            # Tlačítko pro porovnání textů
            self.compare_button = QPushButton("Porovnat texty", self)
            self.compare_button.clicked.connect(self.compare_texts)
            layout.addWidget(self.compare_button)

            # Výsledek shodných sekvencí slov
            self.result_label = QLabel("Shodné sekvence slov:", self)
            layout.addWidget(self.result_label)
            self.result_text = QTextEdit(self)
            self.result_text.setReadOnly(True)
            layout.addWidget(self.result_text)

            # Procentuální shoda
            self.percent_label = QLabel("Aktuální shoda v %:", self)
            self.percent_match = QTextEdit(self)
            self.percent_match.setReadOnly(True)
            self.percent_match.setMaximumWidth(80)  # Nastavení maximální šířky
            self.percent_match.setMaximumHeight(40)  # Nastavení maximální výšky

            # Počet zkoumaných dvojic
            self.count_label = QLabel("Počet zkoumaných dvojic:", self)
            self.count_value = QTextEdit(self)
            self.count_value.setReadOnly(True)
            self.count_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.count_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # Celková průměrná shoda
            self.mean_label = QLabel("Celková průměrná shoda v %:", self)
            self.mean_value = QTextEdit(self)
            self.mean_value.setReadOnly(True)
            self.mean_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.mean_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # První řádek statistických údajů
            stats_layout1 = QHBoxLayout()
            stats_layout1.addWidget(self.percent_label)
            stats_layout1.addWidget(self.percent_match)
            stats_layout1.addWidget(self.count_label)
            stats_layout1.addWidget(self.count_value)
            stats_layout1.addWidget(self.mean_label)
            stats_layout1.addWidget(self.mean_value)

            layout.addLayout(stats_layout1)

            # Minimální hodnota
            self.min_label = QLabel("Minimální hodnota v %:", self)
            self.min_value = QTextEdit(self)
            self.min_value.setReadOnly(True)
            self.min_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.min_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # Maximální hodnota
            self.max_label = QLabel("Maximální hodnota v %:", self)
            self.max_value = QTextEdit(self)
            self.max_value.setReadOnly(True)
            self.max_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.max_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # První kvartil
            self.first_quartile_label = QLabel("1. kvartil v %:", self)
            self.first_quartile_value = QTextEdit(self)
            self.first_quartile_value.setReadOnly(True)
            self.first_quartile_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.first_quartile_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # Medián
            self.median_label = QLabel("Medián v %:", self)
            self.median_value = QTextEdit(self)
            self.median_value.setReadOnly(True)
            self.median_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.median_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # Třetí kvartil
            self.third_quartile_label = QLabel("3. kvartil v %:", self)
            self.third_quartile_value = QTextEdit(self)
            self.third_quartile_value.setReadOnly(True)
            self.third_quartile_value.setMaximumWidth(80)  # Nastavení maximální šířky
            self.third_quartile_value.setMaximumHeight(40)  # Nastavení maximální výšky

            # Druhý řádek statistických údajů
            stats_layout2 = QHBoxLayout()
            stats_layout2.addWidget(self.min_label)
            stats_layout2.addWidget(self.min_value)
            stats_layout2.addWidget(self.max_label)
            stats_layout2.addWidget(self.max_value)
            stats_layout2.addWidget(self.first_quartile_label)
            stats_layout2.addWidget(self.first_quartile_value)
            stats_layout2.addWidget(self.median_label)
            stats_layout2.addWidget(self.median_value)
            stats_layout2.addWidget(self.third_quartile_label)
            stats_layout2.addWidget(self.third_quartile_value)

            layout.addLayout(stats_layout2)

            # Tlačítko pro vložení nového záznamu
            self.save_and_new_button = QPushButton("Vložit nový záznam", self)
            self.save_and_new_button.clicked.connect(self.save_and_new)
            layout.addWidget(self.save_and_new_button)

            # Tlačítko pro ukončení vkládání
            self.end_entry_button = QPushButton("Ukončit vkládání", self)
            self.end_entry_button.clicked.connect(self.save_and_end)
            layout.addWidget(self.end_entry_button)

            # Tlačítko pro vymazání záznamů
            self.clear_button = QPushButton("Vymazat záznamy", self)
            self.clear_button.clicked.connect(self.clear_database)
            layout.addWidget(self.clear_button)

            # Tlačítko pro ukončení programu
            self.exit_button = QPushButton("Ukončit program", self)
            self.exit_button.clicked.connect(self.exit_program)
            layout.addWidget(self.exit_button)

            self.setLayout(layout)
            self.setWindowTitle('neOpisuj_1.0')  # Nastavení nového názvu aplikace

            # Nastavení světle modré barvy pro rám aplikace
            self.setStyleSheet("""
                QWidget {
                    background-color: #f0f8ff;  # Světle modrá barva pozadí
                }
                QPushButton {
                    background-color: #ffffff;  # Bílá barva tlačítek
                    color: #000000; 
                    border: 1px solid #000000;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 14px;
                }
                QPushButton:hover {
                    background-color: #e0e0e0;  # Světle šedá při najetí
                }
                QPushButton:pressed {
                    background-color: #c0c0c0;  # Šedá při kliknutí
                }
            """)
            self.show()

        except Exception as e:
            print(f"Error during UI setup: {e}")  # Debug print

    def compare_texts(self):
        print("Comparing texts")  # Debug print
        text_OBZ = self.text1.toPlainText()
        text_R = self.text2.toPlainText()
        matching_text, percent_match = TextAnalyzer.find_matching_sequences(text_OBZ, text_R)
        self.result_text.setText(matching_text)
        self.percent_match.setText(f"{percent_match:.2f}%")

    def save_to_database(self):
        try:
            text1 = self.text1.toPlainText()
            text2 = self.text2.toPlainText()
            matching_text = self.result_text.toPlainText()
            percent_match = float(self.percent_match.toPlainText().replace('%', ''))
            print("Saving to database:", text1, text2, matching_text, percent_match)  # Debug print
            self.db_manager.insert_result(text1, text2, matching_text, percent_match)
            self.update_statistics()
        except Exception as e:
            print(f"Error during saving to database: {e}")  # Debug print

    def update_statistics(self):
        try:
            print("Updating statistics")  # Debug print
            stats = self.db_manager.get_statistics()
            if stats:
                print(
                    f"Count: {stats['count']}, Mean: {stats['mean']:.2f}%, Median: {stats['median']:.2f}%, Min: {stats['min_val']:.2f}%, Max: {stats['max_val']:.2f}%, 1st Quartile: {stats['first_quartile']:.2f}%, 3rd Quartile: {stats['third_quartile']:.2f}%")  # Debug print
                self.count_value.setText(str(stats["count"]))
                self.mean_value.setText(f"{stats['mean']:.2f}%")
                self.median_value.setText(f"{stats['median']:.2f}%")
                self.min_value.setText(f"{stats['min_val']:.2f}%")
                self.max_value.setText(f"{stats['max_val']:.2f}%")
                self.first_quartile_value.setText(f"{stats['first_quartile']:.2f}%")
                self.third_quartile_value.setText(f"{stats['third_quartile']:.2f}%")
        except Exception as e:
            print(f"Error during updating statistics: {e}")  # Debug print

    def save_and_new(self):
        print("Save and new button clicked")  # Debug print
        try:
            self.save_to_database()
            self.clear_fields()
        except Exception as e:
            print(f"Error during save and new: {e}")  # Debug print

    def save_and_end(self):
        print("Save and end button clicked")  # Debug print
        try:
            self.save_to_database()
        except Exception as e:
            print(f"Error during save and end: {e}")  # Debug print

    def exit_program(self):
        print("Exit program button clicked")  # Debug print
        try:
            reply = QMessageBox.question(self, 'Uložit údaje do tabulky',
                                         'Uložit údaje do tabulky?',
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if reply == QMessageBox.No:
                print("Deleting all data from database")  # Debug print
                self.db_manager.delete_all_data()
            print("Closing database connection")  # Debug print
            self.db_manager.close()
            print("Closing application")  # Debug print
            self.close()
        except Exception as e:
            print(f"Error during exit program: {e}")  # Debug print

    def clear_fields(self):
        print("Clearing fields")  # Debug print
        try:
            self.text1.clear()
            self.text2.clear()
            self.result_text.clear()
            self.percent_match.clear()
        except Exception as e:
            print(f"Error during clearing fields: {e}")  # Debug print

    def clear_database(self):
        print("Clear database button clicked")  # Debug print
        try:
            self.db_manager.delete_all_data()
            print("All data cleared from database")  # Debug print
            self.update_statistics()
        except Exception as e:
            print(f"Error during clearing database: {e}")  # Debug print


if __name__ == '__main__':
    try:
        print("Starting application")  # Debug print
        app = QApplication(sys.argv)
        ex = TextComparerApp()
        ret = app.exec_()
        print("Application exited, closing database connection")  # Debug print
        ex.db_manager.close()  # Explicitní uzavření databáze
        sys.exit(ret)
    except Exception as e:
        print(f"Error during main application run: {e}")  # Debug print
