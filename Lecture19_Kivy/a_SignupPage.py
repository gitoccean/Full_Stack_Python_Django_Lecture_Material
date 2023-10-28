from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.lang import Builder
import pyrebase


firebaseConfig = {
  'apiKey': "AIzaSyD9N2IBF0NS-9FZMbFIW_ON1Tq94rkXZOY",
  'authDomain': "pythonauthproject-c3fc8.firebaseapp.com",
  'databaseURL': "https://pythonauthproject-c3fc8-default-rtdb.firebaseio.com/",
  'projectId': "pythonauthproject-c3fc8",
  'storageBucket': "pythonauthproject-c3fc8.appspot.com",
  'messagingSenderId': "679814430731",
  'appId': "1:679814430731:web:9790480fa660f4cc41870e"
}

firebase = pyrebase.initialize_app(firebaseConfig)
mAuth = firebase.auth()


class SignupPage(App):
    def build(self):
        Window.size = (400,600)
        return Builder.load_file('SignupPage.kv')

    def signup(self,em,ps):
        try:
            mAuth.create_user_with_email_and_password(email=em.text, password=ps.text)
            print('User created.')
        except:
            print("Email already exist.")


SignupPage().run()
