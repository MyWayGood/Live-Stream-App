# quit.py

import sys
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class QuitApp:
    def __init__(self, app):
        self.app = app

    def confirm_exit(self):
        """
        Prompts the user to confirm before exiting the app.
        """
        layout = BoxLayout(orientation='vertical')
        confirm_label = Label(text="Are you sure you want to exit?")
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=0.3)

        confirm_button = Button(text='Yes', on_press=self.save_and_exit)
        cancel_button = Button(text='No', on_press=self.close_popup)

        button_layout.add_widget(confirm_button)
        button_layout.add_widget(cancel_button)

        layout.add_widget(confirm_label)
        layout.add_widget(button_layout)

        self.popup = Popup(title='Confirm Exit',
                           content=layout,
                           size_hint=(None, None),
                           size=(400, 200),
                           auto_dismiss=False)
        self.popup.open()

    def save_and_exit(self, instance):
        """
        Saves any unsaved data and then closes the application.
        """
        # Placeholder for saving data logic, e.g. save settings or video schedules
        self.save_data()

        # Close the app
        self.popup.dismiss()
        sys.exit(0)

    def save_data(self):
        """
        Logic to save any unsaved data (e.g., settings or schedules).
        """
        # Implement your data-saving logic here
        print("Saving any unsaved data before exit...")

    def close_popup(self, instance):
        """
        Closes the confirmation popup without exiting.
        """
        self.popup.dismiss()
