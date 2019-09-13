# Good Food

## What is it about?

I have developed this project using the skills learnt to build a Flask Website, using MongoDB. The application includes a database of recipes that can be searched and viewed by any user. When a user has registered and logged in to the application the user is able to create, update and delete their own recipes. This project can be viewed at https://supreme-food.herokuapp.com.

## UX

The project it is a web application where the user can log into the Good Food and create, store, edit and delete the recipes. The user has access to other people recipes stored in the database to edit or delete them. The user can search by category and allergen.


## Features

The application is fully responsive. Any user can search and view all of the recipes on every device. The user can register an account which will let them to create, edit(update) and delete their own recipes when logged in.

### Existing Features

Every recipe card has a smooth ease in ease out when hovering with the mouse.
Search bar which is located in the navbar.
The home page blur. When accessing the website, the home page will create a blur with the logo in focus, when scrolling down the background will get in focus.
On the front page there is a list of the most 6 popular recipes in descending order. The full recipes list can also be viewed in the "All recipes" page.
Each recipe can be clicked on to view the full recipe as a single recipe. If the user submitted this recipe they are able to edit or delete it if they wish.

## wireframes 

The wireframe was created in AdobeXD
![wireframes](https://user-images.githubusercontent.com/44336390/64869490-c4885c80-d641-11e9-96a5-7ce8bebec343.png)

## Technologies Used

Throughout this project I have used

* HTML5
* CSS / Materialise / Fontawesome
* Python
* PyMongo
* Flask
* JavaScript / JQuery
* WTForms

## Testing

I tested the application manually as follows:

1. Home page
    1. Ensure loads correctly
    2. The blur works perfectly
    3. recipe cards load as required

2.  Recipes Page
    1. Ensure that each recipe card load fully and are all following the same form.

3. Sign In
    1. Enter a username that already exists
    2. Verify an error flashes up and they are asked to choose an alternative username.
    3. Register an account successfully verify that the username and password is saved in MongoDB. The user's password is encoded.

4. Login page
    1. Enter a correct username and an incorrect password combination and verify an error message appears.
    2. Once the user is logged in I verify that they are able to create, edit and delete their own recipes.
    3. If the user views another user's recipe I verify that the user will not see the edit and delete buttons.

5. Create Recipe page
    1. Click on create recipe
    2. Add a test recipe and ensure that this recipe and submit.
    3. I verified that the recipe can be viewed from the Home page, All Recipes page, searched for and the full recipe is loaded.
    4. I also verified that the test recipe was saved in MongoDB.

6. Search
    1. Enter any word from any part of a recipe, eg. Title, ingredient, allergen, category, username, eg. Cheesecake
    2. Verify that the recipe and any other recipe which includes that word is displayed.
    3. I also entered a random string of characters.

7. Filter
    1. By adding a few test recipes from different category and allergens I tested the filter. It works perfectly.

9. Delete Recipe page
    1. Log in
    2. Click on view ensuring that it was originally submitted by that user.
    3. Click on Delete
    4. This then redirects the user to the Home page.
    5. I then verified that the deleted recipe does not appear on the list.
    6. I also searched for this recipe to check it had been deleted.

10. As the application is fully responsive I checked it works fully for mobiles, desktop. I checked on:
* iPhones 5 to X
* Desktop

11. I verified that the application works over different web browsers. I checked on:
* Safari
* Edge
* iOS
* Chrome

12. I verified my JavaScript on https://jshint.com and the Python code on http://pep8online.com/ and then fixed the code accordingly.

## Deployment

The application was coded on Atom Code Editor and with GItBash Terminal.

1. Make a `requirements.txt` file utilizing the terminal command 'pip freeze > `requirements.txt`

2. Make a `Procfile` with the terminal command `echo web: python app.py > Procfile`

3. `git add` and `git commit` the new prerequisites from the requirements.txt file and Procfile, then 'git push' the undertaking to GitHub.

4. Go to [Heroku](https://dashboard.heroku.com/) website.

5. Make another application (app) on the [Heroku](https://dashboard.heroku.com/) website by tapping the "New" button on your dashboard. Name your app, followed by selecting Europe as your region.

6. Select application

7. In the "Deployment Method" section, check to see if the application is already connected to GitHub. If not connected then click the relevant button to link the Heroku website to the dashboard.

8. Affirm the connecting of the Heroku application to the right GitHub repository.

9. In the application dashboard, click on "Settings" > "Reveal Config Vars".

10. Set the accompanying config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 2.8.0.1.7
MONGO_URI | `mongodb+srv://root:<password>@myfirstcluster-np4or.mongodb.net/test?retryWrites=true&w=majority`

PORT | 28017
SECRET_KEY | `<your_secret_key>`

- To retrieve your MONGO_URI please reference the official MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

11. On the dashboard click "Deploy or alternatively in the "Automatic Deployment" section enable "Automatic Deploys" (optional).

12. In the "Manual Deploy" section, set the branch to "master" then click "Deploy Branch."

13. Enjoy

#### Cloning the repository

1. Open in terminal
2. Change the present working directory to the area where you wish to place the cloned directory.
3. Clone the repository or use the link below.

```console
git clone https://github.com/DavidColds/food_app
```

Deploy your changes, make some changes to the code you just cloned and deploy them to Heroku using Git.

#### How to access the live application

- A live demonstration is accessible by clicking [here](http://supreme-food.herokuapp.com/).

#### How to run things locally


1. Download the project onto a PC and open with a source-code editor.

2. In the app.py file set the IP address and the PORT to the following:

```console
'IP', '127.0.0.1'
```

```console
'PORT', '28017'
```

3. Install all of the prerequisites shown in the requirements.txt file via opening a Command-line interface (CLI) and navigating to the project root or by opening an integrated terminal and entering the following command:

> Please Note: The CLI method for interacting with a computer may vary dependant upon the operating system in use.

```console
pip install -r requirements.txt
```

4. Initiate the app by entering the following command into a relevant terminal:

```console
export PORT=28017
and then
python app.py
```

5. A message in your terminal will inform you that the project is now running with the following message:

```console
Running on http://127.0.0.1:28017/ (Press CTRL+C to quit)
```

6. To display the project, open the above URL (localhost:28017)


## Credits

### Special thanks to

My Tutor and Mentor, Anthony Ngene for helping me Throughout this project.

### Media

Font Awesome for icons
For the blurred landing page I visited Brad Traversy on https://codepen.io/ and then https://codepen.io/bradtraversy/pen/jvKmjB?editors=1100. I copied most of the code from there.

### Design

For my cards design I looked at the : http://www.mojomarketplace.com/item/elara-pro-beautiful-wordpress-food-blog-theme/demo and then tried to make it.

### Recipes

The recipes are copied from https://www.allrecipes.com/recipes/.
