<p align="center">
  <img width="500" height="100" src="https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/plastilecorLogo.jpg" alt="PlastilecorLogo">
</p>

# Plastilecor Price List Portal

Plastilecor is a small business without too much digitalization and a B2B line where it becomes handy to provide distributors with an online price list that they can check anytime with an assigned user access. Furthermore, if there are any needed modifications from the plastilecor admin, they can be applied online with an admin user and retrieved to all the other users with a valid access.

![Responsive Mockup](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/am-i-responsive.png)

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

![Login](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/login-wireframe.png)

__Home__  

![Home](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/home-wireframe.png)

__Price List__  

![PriceList](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/price-list-wireframe.png)



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

__Register__

![Register](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/register-feature.png)

__Contact Us__

![ContactUs](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/Contact-us-feature.png)

__Price List Details__

  - The time counter, the name of the schenario, pumpkins (lives) counter and how many ghosts you have hunt are part of the visual tools for the user/player. 

![PriceListDetails](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/price-list-details-feature.png)

__Admin Panel__ 

![AdminPanel](https://github.com/diegocardenast/pp4-plastilecor-price-list-portal/blob/main/assets/images/admin-panel-feature.png)


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

The live link can be found [HERE](MISSING LINK)

--- 

## Credits

### Content 

- Good/Best practice on the readme were shared by Lauren-Nicole Popich in her [mentoring](https://github.com/CluelessBiker/mentoring/tree/main) GitHub repositry
- User Stories and tasks creation was implemented following this [publication](https://boosthigh.com/software-requirements-specification/)
- Use of Google to import [Google fonts](https://fonts.google.com/?classification=Display) 
- Inspiration of the [institutional color](MISSING LINK)
- The use of GitHub to collaborate and apply good practices was implemented following this [Slack post](https://code-institute-room.slack.com/archives/C05UQAPDNCT/p1697457705802579) and this [GitHub post](https://github.com/auxfuse/hackathon-git-labs/blob/main/basic.md)

### Media

- The wireframes were created using [Balsamiq Cloud](https://balsamiq.cloud/)




Thank You!

Diego Cárdenas 
