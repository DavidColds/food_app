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

The application was coded on Atom Code Editor and with GItBash Terminal. I then committed the code GITHUB at https://github.com/DavidColds/food_app
The application was deployed from GITHUB to Heroku at http://supreme-food.herokuapp.com/recipes
My database is stored on MongoDB and is setup within Heroku.

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
