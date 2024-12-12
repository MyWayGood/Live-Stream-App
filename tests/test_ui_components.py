import unittest
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from ui_components import CustomButton, CustomTextInput, CustomLabel

class LiveStreamApp(App):
    def build(self):
        # Dummy app build for testing
        self.screen_manager = ScreenManager()

        # Create test screens for navigation
        self.screen_manager.add_widget(Screen(name="main_menu"))
        self.screen_manager.add_widget(Screen(name="stream_key"))
        self.screen_manager.add_widget(Screen(name="schedule"))
        self.screen_manager.add_widget(Screen(name="videos"))

        # Create dummy buttons and inputs
        self.button = CustomButton(text="Click Me")
        self.text_input = CustomTextInput()

        return self.screen_manager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        # Set up the Kivy app environment
        self.app = LiveStreamApp()
        self.app.build()

    def test_button_click(self):
        # Simulate button click and verify expected action
        def on_button_click(instance):
            self.button_clicked = True

        self.app.button.bind(on_press=on_button_click)
        self.app.button.trigger_action()
        
        self.assertTrue(hasattr(self, 'button_clicked'), "Button click did not trigger the expected action.")
    
    def test_input_validation(self):
        # Test input field validation (dummy validation logic for example)
        self.app.text_input.text = "Valid input"
        is_valid = self.app.text_input.text.isalnum()  # Example validation: alphanumeric check
        self.assertTrue(is_valid, "Input validation failed for valid input.")
        
        self.app.text_input.text = "Invalid!@#"
        is_valid = self.app.text_input.text.isalnum()
        self.assertFalse(is_valid, "Input validation did not catch invalid input.")

    def test_screen_navigation(self):
        # Test smooth navigation between different screens
        self.app.screen_manager.current = "main_menu"
        self.assertEqual(self.app.screen_manager.current, "main_menu", "Failed to start at main_menu screen.")
        
        # Simulate navigation to 'schedule' screen
        self.app.screen_manager.current = "schedule"
        self.assertEqual(self.app.screen_manager.current, "schedule", "Navigation to schedule screen failed.")
        
        # Simulate navigation to 'videos' screen
        self.app.screen_manager.current = "videos"
        self.assertEqual(self.app.screen_manager.current, "videos", "Navigation to videos screen failed.")
    
    def tearDown(self):
        self.app.stop()

if __name__ == '__main__':
    unittest.main()
