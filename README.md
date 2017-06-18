# FlaskSlotMachine
Slot Machine HTML5 code

Slightly modified version of the slot machine that does three main things:
  - it is wrapped by a Flask python server
  - it has a call to remotely trigger the slot machine (a button on a raspberry pi can send a web request to cause the browser to update)
  - the browser sends the server the results of each spin so it can light up lights, and/or dispense something (no security)
  
This slot machine uses our Chocolate Coin Dispenser to dispense chocolate coins on wins, or even if you don't win:
https://github.com/alanswx/ChocolateCoinDispenser
