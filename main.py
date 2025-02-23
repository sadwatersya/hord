from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import math

# Функция для расчета "Шаблон"
def calculate_template(radius, arc, edge):
    results = []
    for i in range(1, 21):  # 20 расчетов
        current_arc = arc * i
        result = 2 * (radius - edge) * math.sin(((current_arc * 180) / (3.1415 * radius) / 57.296) / 2)
        results.append(f"{round(result, 1)}")  # Округляем до одного знака
    return results

# Функция для расчета "Разгон шаблона"
def calculate_template_run(tolerance, passes):
    step = tolerance / passes
    results = []
    for i in range(1, int(passes) + 1):  # Преобразуем passes в int для цикла
        value = step * i
        results.append(f"{round(value, 1)}")  # Округляем до одного знака
    return results

# Функция для расчета "Шаги шаблона"
def calculate_template_steps(holes_on_tape, holes_in_template):
    results = []
    current_value = holes_in_template
    while current_value <= holes_on_tape:
        results.append(str(current_value))
        current_value += (holes_in_template - 1)
    ratio = round(holes_on_tape / holes_in_template, 1)
    results.append(f"({ratio})")
    return results

# Функция для форматирования результатов в столбцы по 5 чисел
def format_results_in_columns(results, numbers_per_column=5):
    # Разделяем результаты на группы по 5 чисел
    chunks = [results[i:i + numbers_per_column] for i in range(0, len(results), numbers_per_column)]
    
    # Формируем строки для каждого столбца
    formatted_results = []
    for i in range(numbers_per_column):
        column = []
        for chunk in chunks:
            if i < len(chunk):  # Проверяем, чтобы не выйти за пределы списка
                column.append(chunk[i])
        formatted_results.append("   ".join(column))  # Разделяем числа тремя пробелами
    
    # Объединяем строки с переносами
    return "\n".join(formatted_results)

# Основной интерфейс
class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # Кнопки для выбора функции
        self.template_button = Button(text="Шаблон", size_hint=(1, 0.2))
        self.template_steps_button = Button(text="Шаги шаблона", size_hint=(1, 0.2))
        self.template_run_button = Button(text="Разгон шаблона", size_hint=(1, 0.2))

        # Привязка кнопок к функциям
        self.template_button.bind(on_press=self.show_template_inputs)
        self.template_steps_button.bind(on_press=self.show_template_steps_inputs)
        self.template_run_button.bind(on_press=self.show_template_run_inputs)

        # Добавляем кнопки в интерфейс
        self.layout.add_widget(self.template_button)
        self.layout.add_widget(self.template_steps_button)
        self.layout.add_widget(self.template_run_button)

        return self.layout

    # Функция для отображения полей ввода для "Шаблон"
    def show_template_inputs(self, instance):
        self.clear_layout()

        # Поля ввода
        self.radius_input = TextInput(hint_text="Внешний радиус", size_hint=(1, 0.1))
        self.arc_input = TextInput(hint_text="Расстояние между креплениями", size_hint=(1, 0.1))
        self.edge_input = TextInput(hint_text="Отступ крепления от края", size_hint=(1, 0.1))

        # Кнопка для расчета
        self.calculate_button = Button(text="Рассчитать", size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate_template)

        # Поле для вывода результатов
        self.result_label = Label(text="Результаты будут здесь", size_hint=(1, 0.5))

        # Добавляем элементы в интерфейс
        self.layout.add_widget(self.radius_input)
        self.layout.add_widget(self.arc_input)
        self.layout.add_widget(self.edge_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

    # Функция для расчета "Шаблон"
    def calculate_template(self, instance):
        try:
            radius = float(self.radius_input.text)
            arc = float(self.arc_input.text)
            edge = float(self.edge_input.text)

            results = calculate_template(radius, arc, edge)
            # Форматируем результаты в столбцы по 5 чисел
            formatted_results = format_results_in_columns(results, numbers_per_column=5)
            self.result_label.text = formatted_results
        except ValueError:
            self.result_label.text = "Ошибка: введите числа"

    # Функция для отображения полей ввода для "Разгон шаблона"
    def show_template_run_inputs(self, instance):
        self.clear_layout()

        # Поля ввода
        self.tolerance_input = TextInput(hint_text="Погрешность", size_hint=(1, 0.1))
        self.passes_input = TextInput(hint_text="Количество проходов", size_hint=(1, 0.1))

        # Кнопка для расчета
        self.calculate_button = Button(text="Рассчитать", size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate_template_run)

        # Поле для вывода результатов
        self.result_label = Label(text="Результаты будут здесь", size_hint=(1, 0.5))

        # Добавляем элементы в интерфейс
        self.layout.add_widget(self.tolerance_input)
        self.layout.add_widget(self.passes_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

    # Функция для расчета "Разгон шаблона"
    def calculate_template_run(self, instance):
        try:
            tolerance = float(self.tolerance_input.text)
            passes = float(self.passes_input.text)

            results = calculate_template_run(tolerance, passes)
            self.result_label.text = "   ".join(results)
        except ValueError:
            self.result_label.text = "Ошибка: введите числа"

    # Функция для отображения полей ввода для "Шаги шаблона"
    def show_template_steps_inputs(self, instance):
        self.clear_layout()

        # Поля ввода
        self.holes_on_tape_input = TextInput(hint_text="Количество отверстий на ленте", size_hint=(1, 0.1))
        self.holes_in_template_input = TextInput(hint_text="Количество отверстий в шаблоне", size_hint=(1, 0.1))

        # Кнопка для расчета
        self.calculate_button = Button(text="Рассчитать", size_hint=(1, 0.2))
        self.calculate_button.bind(on_press=self.calculate_template_steps)

        # Поле для вывода результатов
        self.result_label = Label(text="Результаты будут здесь", size_hint=(1, 0.5))

        # Добавляем элементы в интерфейс
        self.layout.add_widget(self.holes_on_tape_input)
        self.layout.add_widget(self.holes_in_template_input)
        self.layout.add_widget(self.calculate_button)
        self.layout.add_widget(self.result_label)

    # Функция для расчета "Шаги шаблона"
    def calculate_template_steps(self, instance):
        try:
            holes_on_tape = int(self.holes_on_tape_input.text)
            holes_in_template = int(self.holes_in_template_input.text)

            results = calculate_template_steps(holes_on_tape, holes_in_template)
            self.result_label.text = "  ".join(results)
        except ValueError:
            self.result_label.text = "Ошибка: введите целые числа"

    # Очистка интерфейса
    def clear_layout(self):
        self.layout.clear_widgets()
        self.layout.add_widget(self.template_button)
        self.layout.add_widget(self.template_steps_button)
        self.layout.add_widget(self.template_run_button)

if __name__ == "__main__":
    MyApp().run()
