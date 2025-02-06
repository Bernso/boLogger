# What is this package?

This package is an advanced logging system that allows the user to create custom and preset logs, with colour.

# <strong>Installation</strong>

```bash
pip install boLogger --upgrade
```

# Features

- Colour
- Create your own custom logger
- Text wrapping
  - the text will never be on the same level as the logger info
  - "\n" will now triiger a text wrap aswell now, before they where mysteriously removed from existence
- Easy use

# Options

## Colours

- Black
- Red
- Green
- Yellow
- Blue
- Purple
- Cyan
- White
- BBlack
- BRed
- BGree
- BYellow
- BBlue
- BPurple
- BCyan
- BWhite

<br>
<strong>
B stands for bright
</strong>

## Options for Logging()

```py
#each of these have 3 args:
#- text (str)
#- bold (bool)
#- unnderlined (bool)

.header(text)

.info(text)

.warning(text)

.error(text)

.success(text)

.starting(text)

.input(text)

.set_colour(
  method, # one of the basic logging names  e.g. 'info'
  colour # a valid colour code or colour name
)
```

## Options for CustomLog()

CustomLog() includes everything in the Logging() class and more

```py
.set_default_custom(
    title: str, 
    color: str, 
    bold: bool, 
    underlined: bool
) # This is used to create deafults for the custom_log() method
  # Meaning if the user wants to use the cutom_log() method 
  # They only need to use the text parameter 

.custom_log(
    text: str,  
    title: str, 
    color: str, 
    bold: bool, 
    underlined: bool
) # If you already have a deafult set you will only need to enter the text param
  # But if you have not, you will need to enter all params
        
# Method to view the current deafult settings
# It returns it, not printing
.view_deafult() 

.add_color(colour) # your own colour code (must start with '\033[')
```

# Example Usage

```py
### Logging()

myLogger = Logging()

# Explains the module
print(myLogger) 

myLogger.header("Header")

myLogger.info("Info")

myLogger.warning("Warning")

myLogger.error("Error")

myLogger.success("Success")

myLogger.starting("Starting")

myLogger.info("This is a very long log message that is going to spill over to the next line and needs to be properly indented for better readability.")

# Functions as a normal input but has the logging decorations
user_choice = myLogger.input("This is a re-designed input") 
myLogger.info(f"The user inputted: {user_choice}")


### CustomLog()

myLogger = CustomLog()

# Explains the module
print(myLogger) 

# Bold and underlined are automatically set to false
myLogger.set_default(title="beansareyummy", color='Blue') 

myLogger.view_deafult()

myLogger.custom_log("custom")

myLogger.info("custom")
```

## Example
![Example Output]([http://url/to/img.png](https://raw.githubusercontent.com/Bernso/boLogger/refs/heads/main/images/exampleUse.png))

# Code
```py
# Make sure to define the class
mylogger = Logging()
print(mylogger)
    
mylogger.header("Header")
mylogger.info("Info")
mylogger.warning("Warning")
mylogger.error("Error")
mylogger.success("Success")
mylogger.info("This is a very long log message that is going to spill over to the next line and needs to be properly indented for better readability.")
mylogger.info("This is info")
mylogger.set_colour('info', 'BBlack')
mylogger.info("This is the new info")
mylogger.starting("This is a new proccess starting")
num = mylogger.input("This is an input, please enter a number: ")
mylogger.info(f"The user has entered: {num}")


customLogger = CustomLog()
print(customLogger)

customLogger.set_default_custom(title="beansareyummy", color='Blue')
customLogger.view_deafult()
customLogger.custom_log("This is a custom log")
customLogger.info("The deafult length has been adjusted to suit the longest log")
```
