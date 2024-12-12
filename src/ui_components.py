from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.image import Image
from src.datepicker import DatePicker  # Ensure DatePicker exists in src

# Custom Button with styling
class CustomButton(Button):
    def __init__(self, **kwargs):
        super(CustomButton, self).__init__(**kwargs)
        self.background_color = (0.2, 0.5, 0.8, 1)
        self.font_size = '16sp'

# Custom Label with predefined styles
class CustomLabel(Label):
    def __init__(self, **kwargs):
        super(CustomLabel, self).__init__(**kwargs)
        self.font_size = '14sp'
        self.color = (1, 1, 1, 1)  # White color

# Text Input field with placeholder text
class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super(CustomTextInput, self).__init__(**kwargs)
        self.font_size = '16sp'
        self.multiline = False
        self.hint_text = 'Enter text'

# Custom Popup for messages and prompts
class CustomPopup(Popup):
    def __init__(self, title="Popup", content_text="Content", **kwargs):
        super(CustomPopup, self).__init__(**kwargs)
        self.title = title
        self.size_hint = (0.8, 0.8)
        content_layout = BoxLayout(orientation='vertical')
        content_label = Label(text=content_text)
        close_button = Button(text="Close", size_hint=(1, 0.2))
        close_button.bind(on_release=self.dismiss)
        content_layout.add_widget(content_label)
        content_layout.add_widget(close_button)
        self.content = content_layout

# Main layout for UI components
class UIComponents(BoxLayout):
    def __init__(self, **kwargs):
        super(UIComponents, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Adding a label
        self.add_widget(CustomLabel(text="Live Stream App UI Components"))

        # Adding a button
        start_button = CustomButton(text="Start Stream")
        self.add_widget(start_button)

        # Adding a text input
        stream_key_input = CustomTextInput(hint_text="Enter Stream Key")
        self.add_widget(stream_key_input)

        # Adding a checkbox
        enable_checkbox = CheckBox()
        self.add_widget(BoxLayout(orientation='horizontal', children=[
            Label(text="Enable Stream"), enable_checkbox]))

        # Adding a spinner (dropdown) for options
        platform_spinner = Spinner(
            text="Select Platform",
            values=("YouTube", "Facebook", "Twitch", "Custom RTMP"),
        )
        self.add_widget(platform_spinner)

        # Adding a toggle button
        record_toggle = ToggleButton(text="Record Stream", state="normal")
        self.add_widget(record_toggle)

        # Adding an image (assuming an image file exists in the 'assets' folder)
        self.image_display = Image(source='assets/example_image.png')
        self.add_widget(self.image_display)

        # Adding a date picker
        self.date_picker = DatePicker()
        self.add_widget(self.date_picker)

        # Popup for additional options or alerts
        show_popup_button = CustomButton(text="Show Info")
        show_popup_button.bind(on_release=self.show_popup)
        self.add_widget(show_popup_button)

    # Method to display a popup
    def show_popup(self, instance):
        popup = CustomPopup(
            title="Stream Information",
            content_text="Ensure your stream key is valid and platform selected."
        )
        popup.open()

# Running the UI components as a standalone app for testing
if __name__ == '__main__':
    from kivy.app import App

    class UIComponentsApp(App):
        def build(self):
            return UIComponents()

    UIComponentsApp().run()
