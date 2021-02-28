# Rasa-Vs-Code-Debugging
My solution to debug the rasa framework in vs code.
You can debug for example policies, classifiers, default actions,....

# How To use:
Copy my_rasa_run.py in your folder where you have all the files to customize your bot.
(This is the folder where also your config.yml, credentials.yml, domain.yml, ... is in).
Add in the 7th line the path where you start your bot. (This is again the folder where also your config.yml, credentials.yml, domain.yml,... is in).

Klick on VS Code on the debug symbol or press Ctrl+Shift+D.
If you have not configured running and debugging klick on "create a launch.json file".
Copy into the launch.json the settings I made in my launch.json file.

Now add wherever you need the breakpoints (the points where you want the program to stopp to watch the variables).

Klick in VS Code in the top bar on "Run" and then on "Start Debugging" or press F5.


