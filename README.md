<p align="center">
  <img width="500" height="100" src="https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/plastilecorLogo.jpg" alt="PlastilecorLogo">
</p>

# Plastilecor Price List Portal

Plastilecor is a small business without too much digitalization and a B2B line where it becomes handy to provide distributors with an online price list that they can check anytime with an assigned user access. Furthermore, if there are any needed modifications from the plastilecor admin, they can be applied online with an admin user and retrieved to all the other users with a valid access.

![Responsive Mockup](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/am-I-responsive-plastilecor-price-list-portal.png)

## User Experience

### User Stories
- As a **user** I want to **login into the portal** so that I can **see the updated price list of products**
- As a **user** I want to **logout from the portal** so that I can **keep my user credentials safe**
- As a **user** I want to **register in the portal** so that I can **have my own user access**
- As a **user** I want to **have a landing page with a link to the products list** so that I can **always watch the most updated version of the list**
- As a **user** I want to **have a landing page with a link to the the contact form** so that I can **contact plastilecor support in case of any doubt**
- As a **user** I want to **have a landing page with a link to the official Plastilecor website** so that I can **check more information of the company if I need to**
- As an **admin user** I want to **login into the portal** so that I can **CRUD user accounts and price list of products**
- As an **admin user** I want to **logout from the portal** so that I can **keep users credentials and the product list safe**
- As an **admin user** I want to **CRUD user accounts** so that I can **make sure who has access into the portal**
- As an **admin user** I want to **CRUD the product list inside the website** so that I can **make sure we always have the most updated version inside the portal**
- As an **admin user and user** I want to **check the documentation of the website** so that I can **better understand the functionalities, quality and features of it**


### Tasks and Planning

Tasks and planning can be seen in the [Plastilecor Price List Portal - GitHub Project](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal).

### Colour
The colour selection was generated from the company logo: [Plastilecor logo](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/plastilecorLogo.jpg). The main HEX code is [#004F1F](https://g.co/kgs/ZfFH1aA).


## Wireframes

__Login__  

![Login](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/readme/wireframe.png)

__Register__  

![Register](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/readme/wireframe1.png)

__Register__  

![Gameplay2](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/readme/wireframe2.png)



## Features

__Price list model__

  - Description
  
**Key** | **Name** | **Type** 
----------|----------|----------
-- | ProductCode	| Char(200)
-- | ProductName | Char(200)
-- | Dimensions | Char(200)
-- | Price	| Integer
ForeignKey  | Author | User model
-- | CreatedOn | DateTime
-- | LastModifiedOn | DateTime

![Price list model](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/sound-on-off.png)

__Index__

  - The full responsive navigation bar includes links to the Game page, Instructions and Contact page, and is identical in each page to allow for easy navigation. 

![Index](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/index_image.png)

__Art Content__

- Some ghosts were created by the team as well as the team and game logo. 

![Game Logo](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/ghostHuntersLogo.png)

![Ghosts](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/naughty_ghost.png)

__In-game Information__

  - The time counter, the name of the schenario, pumpkins (lives) counter and how many ghosts you have hunt are part of the visual tools for the user/player. 

![inGameInfo](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/gameInfo.png)

__Game Story & Instructions__

  - The descriptions of the characters and how to play. 

![gameStory](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/characters.png)
![Instructions](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/instructions.png)

__Scoreboard__

  - It saves the scores of the players. 

![scoreboard](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/readme/scoreboard.png)

## Testing

### Validator Testing
- Python
  - No errors were returned when passing through the official [pep8ci validator](https://pep8ci.herokuapp.com/)  
- JavaScript
  - No errors were returned when passing through the official [JSHint validator](https://jshint.com/)
- HTML
  - One error related to invalid attributes for an img element was returned when passing the first time through the official [W3C validator](https://validator.w3.org/)
  - No errors were returned when passing the second time through the official [W3C validator](https://validator.w3.org/)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?)
- Lighthouse
  - The result given by the system for the lighthouse assessment is the following:
![Lighthouse results](https://github.com/diegocardenast/CodeBusters/blob/main/assets/images/lighthouse-test.png)

### Manual Testing
**TEST** | **ACTION** | **EXPECTATION** | **RESULT** 
----------|----------|----------|----------
Index | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Index | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Game | Size to 320px using Chrome Dev Tools	| Elements look good @ 320px | Works as expected
Game | Size to 1920px using Chrome Dev Tools | Elements look good 1920px | Works as expected
Index page test | All phone sizes checked using Chrome Dev Tools | Elements look good | Works at expected
Game page test | All phone sizes checked using Chrome Dev Tools | Elements overlap and game runs faster at lower resolutions | Does not work as expected 



### Unfixed Bugs

- NA

## Deployment 

- The site was deployed in the Heroku. The steps to deploy are as follows: 
  - Install the **Django Python package** by running in the Gitpod terminal **"pip3 install Django~=4.2.1"**
  - Update the requirements file by running in the Gitpod terminal **"pip3 freeze > requirements.txt"**
  - Push the latest changes to the GitHub repository 
  - Run in the Gitpod terminal **"django-admin startproject my_project ."** to create a Django project. In this case, my_project is called **plastilecor_portal**
  - Add the **ALLOWED_HOSTS** (in this case '8000-diegocarden-pp4plastile-dl4pq8wxrog.ws-eu108.gitpod.io') into **plastilecor_portal/settings.py** file
  - Push the latest changes to the GitHub repository
  - Create Django Apps and Views, as well as configure settings.py
  - Push the latest changes to the GitHub repository
  - Inside the Heroku account, create a new app with a unique name (in this case **project-plastilecor-portal**)
  - Inside the Heroku app settings tab, reveal the **config vars** and Add a key of **DISABLE_COLLECTSTATIC** and a value of **1**
  - Install a production-ready webserver for Heroku running this command inside the gitpod terminal **pip3 install gunicorn~=20.1**
  - Add **gunicorn==20.1.0** to the **requirements.txt** file with the following command **pip3 freeze --local > requirements.txt**


  - Inside the Heroku app settings tab, create a _Config Var_ called `PORT`. Set this to `8000`
  - Inside the Heroku app settings tab, add two buildpacks:
    - `heroku/python`
    - `heroku/nodejs`
  - Inside the Heroku app deploy tab, select GitHub as deployment method and connect the GitHub repository to the Heroku app
  - Inside the Heroku app deploy tab, click on deploy branch
  - Click on View App
  - Done!

  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

- The game code is stored in a GitHub repository and was deployed in the Heroku app. The steps to deploy are as follows: 

The live link can be found [HERE](https://hangman-game-diego-dd66cfc0fedc.herokuapp.com/)

The live link can be found [HERE](https://diegocardenast.github.io/CodeBusters/)

--- 

## Credits

### Content 

- Good/Best practice on the readme were shared by Lauren-Nicole Popich in her [mentoring](https://github.com/CluelessBiker/mentoring/tree/main) GitHub repositry
- User Stories and tasks creation was implemented following this [publication](https://boosthigh.com/software-requirements-specification/)
- Use of Google to import [Google fonts](https://fonts.google.com/?classification=Display) 
- Inspiration of our [game color palette](https://tools.picsart.com/color/palette-generator/?colors=D8A56C-2D244C-955637-6C4346-697986-3D5980-394D71-6B89A4) and were based on the selected game background that comes from [themeforest.net](https://themeforest.net/)
- The animation and use of canvas in JavaScript was implemented following this [tutorial](https://youtu.be/GFO_txvwK_c?si=l2RwIYNxn0n712Ew)
- The use of GitHub to collaborate and apply good practices was implemented following this [Slack post](https://code-institute-room.slack.com/archives/C05UQAPDNCT/p1697457705802579) and this [GitHub post](https://github.com/auxfuse/hackathon-git-labs/blob/main/basic.md)
- The [team availability](https://docs.google.com/spreadsheets/d/1dMP_YxtveAuA8vppXYU1i1a0LoCAVq37If_BdVpL-fg/edit?usp=sharing) was organized using [Google sheets](https://www.google.com/sheets/about/)

### Media

- The creation of the team banner and game logo was implemented using [Canva](https://www.canva.com/)
- The wireframes were created using [Balsamiq Cloud](https://balsamiq.cloud/)
- The icons along the web app were taken from [Font Awesome](https://fontawesome.com/)
- The use of the icons was provided by [Flaticon](https://www.flaticon.com/free-icon/planet-earth_1598431?related_id=1598196&origin=search)
- The ghosts own art were created with [Procreate](https://procreate.com/) and [Photoshop](https://www.adobe.com/products/photoshop.html)
- The improvement/change of sprites (sequence of images for animation) were implemented using [GIMP](https://www.gimp.org/)
- The game background music was selected from opengameart.org and created by [Alexandr Zhelanov](https://opengameart.org/content/wtf-ghost)
- The game background image was selected from [themeforest.net](https://themeforest.net/)



Thank You!

Diego Cárdenas 
