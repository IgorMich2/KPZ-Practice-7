from logic import choicer, settings, commands
from logic.graphic import display_messages

display_messages.greeting()
display_messages.log_or_create()
choicer.log_or_create()

display_messages.greeting_main_menu()

while True:
    commands.main_menu(settings.CURRENT_USER)
