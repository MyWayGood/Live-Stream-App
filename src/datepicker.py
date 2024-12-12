from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from datetime import datetime


class DatePicker(Popup):
    def __init__(self, **kwargs):
        super(DatePicker, self).__init__(**kwargs)
        self.title = 'Select Date'
        self.size_hint = (None, None)
        self.size = (400, 400)

        # Create layout for DatePicker
        layout = BoxLayout(orientation='vertical')

        # Date display
        self.date_label = Label(text='Selected Date:')
        layout.add_widget(self.date_label)

        # Input field for manual date entry
        self.date_input = TextInput(hint_text='Enter date (dd/mm/yyyy)', multiline=False)
        layout.add_widget(self.date_input)

        # Buttons for selecting today's date and confirming selection
        btn_layout = GridLayout(cols=2)

        self.today_btn = Button(text='Today')
        self.today_btn.bind(on_press=self.set_today)
        btn_layout.add_widget(self.today_btn)

        self.confirm_btn = Button(text='Confirm')
        self.confirm_btn.bind(on_press=self.confirm_date)
        btn_layout.add_widget(self.confirm_btn)

        layout.add_widget(btn_layout)

        # Add layout to popup
        self.add_widget(layout)

    def set_today(self, instance):
        """Set the date to today's date."""
        today = datetime.today().strftime('%d/%m/%Y')
        self.date_input.text = today

    def confirm_date(self, instance):
        """Confirm the selected or entered date."""
        selected_date = self.date_input.text
        try:
            # Validate the date format
            datetime.strptime(selected_date, '%d/%m/%Y')
            self.date_label.text = f'Selected Date: {selected_date}'
        except ValueError:
            self.date_label.text = 'Invalid date format, please use dd/mm/yyyy.'
        self.dismiss()  # Close the popup after confirming the date
