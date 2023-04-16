# Goblin Crypt

[Please visit the game here.](https://goblin-crypt.herokuapp.com/)

![An image showing the game on different devices.](assets/docs/mock.png)

I created this text adventure game to demonstrate my understanding of Python. I have played a lot of fantasy based games like Dungeons and Dragons. Text adventure games were a bit before my time, so creating one sounded like a lot of fun and a good way to learn Python. It is certainly not a typical use for Python, but I think it still contains the same techniques found in a more typical use of Python.

Goblin Crypt is a text adventure game played through a hosting app called Heroku. It is made up of these sections:

1. Start screen / title screen.
2. Past adventures screen / score screen.
3. Main game sections.
4. Death screen / play again screen.
5. Winning screen.

Game owner's goals:

1. Create a fun game loop that keeps the player coming back.
2. Allow the player to make choices on which path they want to take.
3. Have multiple ways of achieving victory in the game.
4. Create a reasonably difficult game to promote replayability.
5. Record player names, classes and deaths to show where people failed to win.

User goal's

1. As a first-time user: I want to view past players adventures.
2. As a first-time user: I want to play an adventure game that allows me to make my own choices.
3. As a first-time user: I want to be able to choose my own class, which effects gameplay.
4. As a recurring or first-time user: I want to be able to play the game over and over to see all outcomes.
5. As a recurring or first-time user: I want to be able to have a custom name for my adventurer.

# UX / UI

## Strategy

After thinking about the strategy for my game. I came up with a target audience, which would influence the features included.

### Target users:

1. 18-40 years old.
2. Interested in fantasy adventure games.
3. People interested in probability.
4. People interested in Dungeons and Dragons.
5. People interested in humorous game settings.

### What the user would look for:

* Easy to understand and clear text prompts.
* Clear explanations for what input the game looks for.
* An addictive game loop.
* An ability to play the game again if I die.
* A fun game based on probability.

Since the game is entirely based around text, I did not have to worry about artwork for the game. I wanted to include more ascii art for it, however I had a lot of trouble getting it to display correctly in Heroku. I did my best to make sure that all text was formatted in the best way for the user to understand and read it.

## Scope

To help the user achieve their desired experience, these features were included:

* Descriptive and interesting text was created to keep the user entertained.
* Upon death, the player is able to make a choice to play again.
* A 'Tombstone' section was made to let players look at past adventures.
* A vast game logic map was created to allow many outcomes for the player to choose from.
* A series of choices allowing the user to rely on probability.
* The game can be quite difficult, which promotes the player to keep playing to learn the best tactics.

## Structure 

This is purely a text adventure game viewed through a custom terminal. It contains a start screen to allow the player to either start the game or view the 'Tombstone' section. This contains all of the past players failures. The main game is made up of scenarios and sections. These can be better visuallised by the logic map which will be included below. The game also contains a 'Gameover' section where they can choose to quit which will shut down the game, or play again and allow them to start a new game.

### Skeleton 

#### Logic maps

[Logic maps for text adventure game](assets/docs/logicChart.pdf)

Please be aware, the logic map may not contain every option in the final game. As it was being created, more creative options would come to me. So it may not represent the final game accurately. There is a lot of logic in the game, so having these maps was very important to keep track of it all. It can also be useful for someone to use to see what the correct options are.

## Surface

Since it is just a text adventure game, there is not much to it's surface. If I had more time I would have liked to have included more ascii art and some basic uses of colour. However since there was a vast ocean of options to code, I made the logic of the game my main focus. I think the games setting and theme makes up for its lack of style.

## Features

When creating this game, I wanted to make sure that it included real life uses of Python code. Where I could show how it would be used in a more typical situation for Python. 

### Start screen

This screen lets the user initiate the game when they want. Also it allows them to view the past adventures.

### Tombstone screen

This screen holds all of the past adventurers that did not make it. When a player dies, the game takes their name, class and death reason and uploads it to a spreadsheet. The information is then pulled and displayed for the user.

### Main game sections

The game is made up of sections where the player is given choices to forge their own path. Most sections will contain puzzles or scenarios where the player will need to think about their best approach.

### Death screen

It is quite easy to die in this game. So a death screen was needed, it allows the player to start a new game. Or they can quit the game if they are feeling too frustrated. 

### Outro screen

This screen is shown when the player manages to fight their way through the dungeon.

### Class choices

To include more complicated logic, I added a class choice at the start of the game. Certain options in the game can only be successfully executed by certain classes. For example, rogues are sneaky so they should go with any sneaking options. I was inpsired by the fallout game series to include a feature like this. It also promotes the player to play again to try different classes and options.

### Player name

Lastly the player is able to name themselves, so that they feel more invested in their character.

# Technologies

1. [Python](https://www.python.org/)
Used to create the entire game.

2. [Python text adventure tutorial](https://www.youtube.com/watch?v=DEcFCn2ubSg&t=619s)
I used this tutorial to see how I would go about making my own game.

3. [Delayed text Python](https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing)
I used this code to print the text slower for the game.

4. [GitHub](https://github.com/)
This was used to store all of my code safely.

5. [Heroku](https://www.heroku.com/home?)
Heroku was the hosting site for my game.

6. [Git](https://git-scm.com/)
This allowed me to version control my code. As well as push and commit pieces to Github when I needed.

7. [Gitpod](https://www.gitpod.io/)
I used gitpod as my development environment.

8. [Illustrator](https://en.wikipedia.org/wiki/Adobe_Illustrator)
I used illustrator to create the logic maps for my game.

9. [Code Institute Python Linter](https://pep8ci.herokuapp.com/)
The Code Institute Python Linter allowed me to check my code for any errors or issues.

10. [Code Institute](https://codeinstitute.net/ie/)
The code institute lessons were used many times to troubleshoot.

11. [Slack](https://slack.com/intl/en-ie/)
Code institute slack channels were very important during this project.

## Testing

1. As a first-time user: I want to view past players adventures.

I wanted to show Pythons usefullness when it came to formating and uploading data. I thought having a 'Tombstone' where others had failed would be a fun and strong way of showing this.

2. As a first-time user: I want to play an adventure game that allows me to make my own choices.

I personally always enjoyed video games that gave you a lot of control when it came to the story. So I wanted to give the user as many options as possible, all while making sure not to over-scope my project.

3. As a first-time user: I want to be able to choose my own class, which effects gameplay.

A way I came up with to include more complicated logic to the game was to add classes to the game. Certain outcomes and options can only happen if you have the correct class in this game.

4. As a recurring or first-time user: I want to be able to play the game over and over to see all outcomes.

This game can be quite punishing, so I included an option to let the player start a new game when they die. With this they can choose new classes and options to learn the best approaches in the game. Also perhaps get to areas they were not able to get to in other play throughs.

5. As a recurring or first-time user: I want to be able to have a custom name for my adventurer.

Being able to name a character is always important. It keeps the player invested in their character, also makes for a funny scenario when the name is etched into the tombstone for other players to see.

### Testing check list

As there is a lot of outcomes and options in my game. I needed a way to make sure each section was being tested properly and being held to good standards. So I created a simple checklist to go through each section.

![An image showing my testing check list.](assets/images/checkList.png)

## Python Validation

I validated my Python code frequently throughout the development process. I was quite lucky as once I had created a template for each scenario in the game, it was easier to avoid bad code. The only issue that came up sometimes was trailing whitespace.

## Bugs

Bug 1.

![An image showing my testing check list.](assets/images/bug1.png)

## Deployment

I deployed my game to Heroku using these steps:

1. Type 'pip3 freeze > requirements.txt' into your terminal. This makes sure Heroku has up to date dependencies before you deploy.
1. Sign into Heroku.
2. Select create a new app, name your app and select your region. (You will have to have your payment option set up to do this)

![Creating a new Heroku app screen.](assets/images/newApp.png)

3. Navigate to the settings tab, 
4. Navigate your way to the pages section of settings. Scroll to 'Config Vars' and then select reveal configs.

![Creating a new Heroku app screen.](assets/images/revealConfig.png)

5. In the key field enter 'CREDS' (Case sensitive) Then in the value field, paste the contents of your creds.json file.

![Creating a new Heroku app screen.](assets/images/credsJson.png)

![Creating a new Heroku app screen.](assets/images/creds.png)

![Creating a new Heroku app screen.](assets/images/paste.png)

Once you have done this, click add.

6. Next scroll to buildpacks, add Python and nodejs. It is important that Python is placed on top of nodejs.

![Creating a new Heroku app screen.](assets/images/buildpack.png)

7. Navigate to the deploy section and select Github. Confirm that you want to connect your Github, then search for your repository code and click connect.

![Creating a new Heroku app screen.](assets/images/deployment.png)

8. Scroll to automatic deploys and select enable automatic deploys. This means Heroku will keep up to date with any changes you push on Github. Heroku will then begin building your app.

9. Once finished navigate to the top of the screen and click on app to view your working app.

![Creating a new Heroku app screen.](assets/images/deployed.png)

## Credits

These are the sources that helped me make my way through this project. I used many pages for troubleshooting and wisdom when it came to creating my game.

### Researching and inspiration:

* [Trinket](https://trinket.io/python/e5a03e7cbc)

* [Ask Python](https://www.askpython.com/python/text-based-adventure-game)

* [PythonCode](https://www.thepythoncode.com/article/make-a-text-adventure-game-with-python)

* [Ascii Art](https://www.asciiart.eu/)

### Code sources and tutorials:

* [Kevin Powell Tutorials](https://www.youtube.com/channel/UCJZv4d5rbIKd4QHMPkcABCw)

* [Bro Code](https://www.youtube.com/channel/UC4SVo0Ue36XCfOyb5Lh1viQ)

* [Programming with Mosh](https://www.youtube.com/@programmingwithmosh)

* [Clear Code](https://www.youtube.com/@ClearCode)

### Content 

All of the content was written by me or was taken from of my favourite fantasy movies.

## Acknowledgements

I would like to pass on a massive thank you to my mentor Harry Dhillon. He provided excellent adivce and was very supportive throughout the whole process. My good friend Daniel Roberts, he is a seasoned front end developer and also provided amazing tips. As well to all my family and friends who had a look at the game at my request. Lastly a huge thank you to Ed at the Code Institute mentors. He always seemed to end up picking up my tickets. He was an enormous help throughout all of this. 

