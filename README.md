# Carblog 

Developer: Dominik Wigh
## Description 

This is the fourth project for the Code Institute Diploma in Software Development.

CarBlog is a webiste built in Django using Python, JavaScript, CSS/Bootstrap and HTML. 
It enables users to create and share blog posts with people around the world. It is targeted towards people who like cars and want to have a read about them, and share their thoughts. Users have the ability to create posts, categorys and their own profile. They can link their personal accounts in their profile. The profile is also editable. They can also like posts and leave a comment. If wanted the user can contact Carblog via email.
The site provides user authentication and a full CRUD functionality.

## Project Goals
---
### User Goals 
* To be able to create blog posts. 
* To be able to Comment and like on posts. 
* To be able to have a profile page. 
* To be able to have CRUD functionality whilst being logged in. 

### Site Owner Goals
* To provide a platform where users can add posts and share their thoughts.
* To provide a enjoyable user experience where users want to come back and read, update and create posts. 
* To have a contact form where users can give feedback. 

## User Experience
---
* Carblog is inteded to be a friendly community site where users can create and share their own thoughts on cars with others. Users will also be able to see other peoples posts and interact with them via comments or likes. 

## Agile development 
---
An Agile approach to creating this app has been applied. GitHub's projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience. 

By using AGILE methodology in this project i was able to deliver a site which had all required functionality and some more. Due to time limit on this project I was not able to incorporate all initial listed features, but this is where an AGILE approach is great. The project displays this by having User stories in the Done section and the ones which decided to be left for future put in the future implementation.

## User stories

1. As a site user, i can add blog posts so that i can interact with others.  
2. As a site user, i can edit my blog post so that i can update the post in the future.
3. As a site user, i can delete my posts so that i can remove it from the site.
4. As a site user i can register an account so that i can interact with blog posts.
5. As a site user, i can add categories so that the blog posts are separated in their own category.
6. As a site user, i can contact the site admin so that i can communicate via email.
7. As a site user, i can like or unlike a post so that i can interact with the content.
8. As a site user, i can leave comments on posts so that i can be involved in the conversation.
9. As a site user, i can Create, read, update and delete posts so that i can manage my content.
10. As a site user, i can have my own profile page so that i can provide my information.
11. As a site user, i can edit my settings so that i can update my information in the future.
12. As a site user i can log in or out of my account so that i can kepp my account secure.
13. As a Site user, i can approve or disapprove comments so that i can filter out comments.
14. As a Site user, i can add a image to my post so that i have a image with my text.
15. As a site user i can delete my account so that users wishing to close can do that.
16. As a site user i can reply to a comment so that i can respond.
17. As a site user i can search for a post so that i can quickly find a post that i am looking.
18. As a site admin, i can create draft posts so that i can finish writing them later.
## Design
---
### CRUD Functionality
* Create - Users can create posts, an account, a profile, add a comment, and like. 
* Read - Users can view post that other people have written and also their profile. 
* Update - Users can update their profile, posted posts and likes. 
* Delete - Users can delete posts, comments and likes. 

## Colors
The colour scheme used in this project was chosen with simplicity in mind. The colour scheme is used throughout all pages to ensure contrast readability and an overall good user experience.

## Fonts 
Google Fonts was used on deciding on the fonts for the website. "Zen dots with a fallback of sans-serif" was the ideal font for the website.

## Site structure

## Pages
User experience was one of the main driving factors in this project. A simple, clear and easy to navigate app was the desired outcome. To achieve this there is  a sticky nav bar with links at the top. In the form of a hamburger toggle button if using a small screen device in which all links will be listed vertically.

The website consists of the following sections: 
### If not logged in 
When the user is not logged in they are able to read post on the home page and visit the authors profile page. Posts will be displayed in order by date of most recent.
* Register, the user can register via a form. 
* Login, the user can log in.
* Categories, here the user can select a specific category to read. 
* Contact page, here the user can contact carblog via a email.  
* Post page, when a user select a post to read they are not able to like the post nor can they leave a comment.
### If logged in 
When the user is logged in their name will appear in the navbar with a hello message. They are able to read post on the home page, posts will be displayed in order by date of most recent.
* Add post, the user can create a post. 
* Add Category, the user can add a category.
* Logout, the user is able to logout.
* Drop down Profile, the dropdown menu consist of...
    * Edit settings where the user can edit their settings, email, password, username and so on. 
    * Show profile, this page shows the user their profile page. 
    * Edit Profile page, here the user can edit their bio and social links via a form which will be update upon save.
* Post page, when a user select a post to read they are able to like or unlike the post and leave a comment.If the Post was created by the right user they are able to edit or delete the post. 

## Features 
---
The website consists of many features across the many pages. 

### Authentication

Authentication is a feature of the website, users will have to be authenticated to create delete and edit posts. Also if they want to add a category.

### Contact 

The Contact feature can be found in the navbar and allow both signed in users and not signed in to contact the site admin. 

### Add post
The add post feature can be found in the navbar when a user is registerd and logged in. And allows the user to make posts to the website. When a post is added the user is then redirected to the home page and gets a message displyed. 

### Edit post / delete post 
The edit and delete post feature can be found when the user is logged in and visits their post. When a post is edited or deleted the user gets a message displayed. 

### Blog posts
This feature is the main page with posts with the latest created at the top. This page can be found when clicking the carblog title in the navbar. 

### Like / unlike button
The Like feature can be found under the post, but is only visible when a user is logged in. Otherwise there is a link to login. 

### Comment section 
The comment section is only visible when a user is logged in, If there is no comment there will be a link to a page where the user can leave a comment. Otherwise there will be a link to login. 

### Register 
The register feature is located in the navbar and is a form that the user has to fill out to be registered. When a user creates a account and loggs in a message is displayed. 

### Login 
The login is located beside register and is avilable for the user to fill out if they have registered. 

### Categories 
The catgories dropdown menu is located in the navbar and displays different categories. 

### Add Category 
The add category is located in the navbar and lets the user add a category if wanted. When a category is added the user is redirected home and a message is displayed. 

## Future implementation
---
### Future features 
While using the AGILE design methodology against the time allocated to the project there are a number of features which would be great to implement in the future. These features are: number 13,14,15 in the user stories. 

### Improvments 
Although alot of effort was put into this project, due to time constraints there is still room for improvments. 

## Valdiation Testing
---
### HTML Validation 
[W3C Validation](https://validator.w3.org/) was used to validate the html code used in the project. The method to validate i chose to be by Direct Input. To achieve this a page that needed testing was navigated to. On the page right click and then choose the option of view source code. This code was then copied and pasted into the validator and tested.
<details>
<summary>Want to ruin the surprise?</summary>
<br>
Well, you asked for it!
</details>

## Css Validation
[W3C Validation](https://validator.w3.org/) was used to validate the css code used in the project. The method to validate i chose to be by Direct Input. To achieve this i copied all code from the style.css file. This code was then copied and pasted into the validator and tested.
<details open>
<summary>Want to ruin the surprise?</summary>
<br>
Well, you asked for it!
</details>

## JavaScript Validation 
[JShint](https://jshint.com/) Was used to validate the JavaScript code used. Thers i a small script used in the templates that has been intentionally placed there due to the small size of the script and being specific to those pages.
<details>
<summary>Want to ruin the surprise?</summary>
<br>
Well, you asked for it!
</details>

## Python Validation
[PEP8](https://pep8ci.herokuapp.com/#) 
<details>
<summary>Want to ruin the surprise?</summary>
<br>
Well, you asked for it!
</details>

## LightHouse Validation
[PEP8](https://pep8ci.herokuapp.com/#) was used to validate the performance of the app. 
<details>
<summary>Want to ruin the surprise?</summary>
<br>
Well, you asked for it!
</details>
<br>

## Manual Testing 

### Testing User Stories

User Story:
>1. As a site user, i can add blog posts so that i can interact with others.

Acceptance criteria:
* Given that i am a logged in user when i navigate to 'Add Post' in the navbar i have the option to create a blog post. 
* Given that i have created a blog post as a logged in user, then its available to other users to view. 

Implementation of tests: 
* Give authenticated users a clear option to create a blog post. 
* Make made posts available to other visitors to view. 

## All Tests Passed &check;
----
User Story:
> 2. As a site user, i can edit my blog post so that i can update the post in the future.

Acceptance criteria:
* Given that i have logged in as a correct user of a post, i can navigate to the full post when clicking on the post title. Then i have the option to Edit the post. 
* Given that i have logged in as a different user and i navigate to someone else's post then i don't get the edit option. 

Implementation of tests:
* Provide a easy way of editing posts. 
* Prevent other users from editing other peoples posts.
* Give blog posts owners a method to edit posts.

## All Tests Passed &check;
----
User Story: 
> 3. As a site user, i can delete my posts so that i can remove it from the site.

Acceptance criteria:
* Given that i have logged in as a correct user of a post, i can navigate to the full post when clicking on the post title. Then i have the option to delete the post.
* Given that i have logged in as a different user and i navigate to someone else's post then i don't get the delete option.
* Given that i have logged in as a correct user of a post and clicks on delete i recive a confirmation window to confirm that i want to delete the post. 

Implementation of tests:
* Provide post owners with the option to delete their blog posts. 
* Provide post owners with a confirmation window to prevent mistakes.
* Prevent unauthorised access to post deletion functionallity.
* Give blog posts owners a method to delete posts.

## All Tests Passed &check;
--- 
User Story:
> 4. As a site user i can register an account so that i can interact with blog posts.

Acceptance criteria:
* Given that i am a new user i can register for a account, through clicking on register in the navbar. 
* When i fill out the form i have registered and i am redirected to the log in page. 
* Given that a user is not registered they can not comment and like on posts. 

Implementation of tests:
* Provide a simple and clear registration form linked in the navbar.
* Redirection to log in page when registration form is completed. 
* Provide a authentication to comment on posts and like a post. 
* Restrict the ability to interact with content.
* Redirect users who make a request for a fnctionality that requires them to be authenticated. 

## All Tests Passed &check;
--- 
User story:
> 5. As a site user, i can add categories so that the blog posts are separated in their own category.

Acceptance criteria:
* Given that i am a registered and logged in user i can add blog categories and it only shows up for me when i am logged in. 
* Given that i dont have a account i dont have se the option to create a new category. 

Implementation of tests:
* Check for easy access in navbar to add a new category.
* Easy to create category and when created shown in categorys dropdown menu. 

## All Tests Passed &check;
--- 
User Story:
> 6. As a site user, i can contact the site admin so that i can communicate via email.

Acceptance criteria: 
* When visiting the blog i can see a contact section in the navbar where when clicked gives a form to fill out. 
* When Form is filled out The owner of the site gets an email with my message. 

Implementation of tests:
* When form is submitted, email is then checked for a message.

## All Tests Passed &check;
---
User Story:
> 7. As a site user, i can like or unlike a post so that i can interact with the content.

Acceptance criteria: 
* Given that i am logged in i can leave a like a post. 
* Given that i dont have a account i cant like a post. 
* I can Unlike post after i have liked it. 

Implementation of tests:
* When opening a post to view the whole post i can then read the post and like button is shown beneath the text. Originillay blue after clicked it turns blue.
* After a like has been given the counter increases. Or decreses if unliked. 
* Given that i dont have a account i cannot see Like button or count. 
* A link is displayd instead with a link to registration page. 

## All Tests Passed &check;
--- 
User Story: 
> 8. As a site user, i can leave comments on posts so that i can be involved in the conversation.

Acceptance criteria:
* Given that i am a registered user of the website when i navigate to comments section i am able to leave a comment. 
* Given that i am a registered user i can click on 'leave a comment' and it send me to a comment form to submit. 

Implementation of tests:
* Provide easy access to comment section. 
* Provide users the ability to comment on a post.
* Provide users with a comment section to start a dialogue. 

## All Tests Passed &check;
--- 
User Story: 
> 9. As a site user, i can Create, read, update and delete posts so that i can manage my content.

Acceptance criteria:
* Given that i am a unregistered user, when i am at the homepage i see the option to register. 
* Given that i am a registerd user i can add a post, update a post, open a post and delete a post. 
* When i add a post its then seen on the main page. 
* When i click on the post i can read the whole text. 
* When post is open i can both edit and delete the post thorugh buttons at the top. 


Implementation of tests:
* Check for clear accessible call to action, and that it works as expected.
* Easy display of functions. 

## All Tests Passed &check;
---
User Story:
> 10. As a site user, i can have my own profile page so that i can provide my information.

Acceptance criteria:
* Given that i am a unregistered user, when i am on the home page. Then i see a Register link in the navbar. When link is clicked it takes me to the register page where i have to fill out form to register. 
* Given that i am a unregistered user, When i fill out the form the system creates me a account and i am redirected to the login page where i have to log in. 
* Given that iam user i am able see a profile dropdown menu in the navbar, when clicked i can edit my settings and create a profile page. 
* When profile the page is created a link is added to the dropdown menu for me to view my profile.  

Implementation of tests:
* Check for clear accessible call to action, and that it works as expected.
* Clear accessible link to create profile and view it. 
* Easy process creating a profile. 

## All Tests Passed &check;
--- 
User Story:
> 11. As a site user, i can edit my settings so that i can update my information in the future.

Acceptance criteria:
* Given that i am logged in and click on the profile dropdown menu and then click on edit settings, i should be able to view my settings and edit them. 
* Given that i am not a logged in user i am not able to see the profile dropdown menu. 
* Given that i am not logged in to my account and type in the address to edit my settings i am not able to edit anything. 

Implementation of tests:
* Provide a clear accessebility to view settings and change them if wanted. 
* Provide a clear and easy to fill out form for the user to update their information. 

## All Tests Passed &check;
--- 
User Story: 
> 12. As a site user i can log in or out of my account so that i can kepp my account secure. 

Acceptance criteria:
* Given that i am a registered user, when i navigate to the log in link in the navbar and fill out my credentials correctly and press log in, then i am logged in to my account. 
* Given that i am a registered user, when i navigate to the log out link in the navbar and and press log out, then i am logged out from my account.
* Given that i am registered user but signed out and navigate to a blog post i cannot access functions that requires to be logged in. 

Implementation of tests:
* Provide login and logout functionality. 
* Secure restricted pages from access when a user is not logged in.

## All Tests Passed &check;
--- 
# Technologies 
-- 
* Python / Django 
    * Django was used as the main python framework. 
* Heroku 
    * Heroku was used as the cloud based platform to deploy the site on.
* Heroku PostgreSQL
    * Heroku PostgresSQL was used at the databse.
* JavaScript
    * JavaScript was 
* Bootstrap 4.6
    * Bootstrap was used for layout. 
* Font Awesome
    * Font Awesome was used for icons on the site. 
* CSS
    * Custom CSS was written for some ares and used to escpae some bootstrap look.
* HTML
    * HTML was used as the base programminglanguage for the templates. 
* GitHub 
    * GitHub was used to store the files for this project
* Gitpod
    * Gitpod was used to develop the website. 

## Resources Used 
---
* The Code Institute refernce material was used as a general reference for things i had previously done during the course. 
* All Other resources used are acknowleged where appropriate.

## Deployment
---
The steps to deploy are as follows..

* Go to Heroku and at the top click on the "new" button to create a new app.
* Enter a unique name and choose Europe as region and click create app.
* Go to settings and select "Config vars".
* Add a new "Config vars":
    * DATABSE_URL: ELEPHANTSQL postgres databse url, obtained below!
    * PORT: 8000
    * SECRET_KEY: Your secret key
* Exit the settings and click Deploy and click Github from the deploy options.
* Select your repository and connect it to Heroku.
* Click enable automatic deploy.
* Wait for the app to build and then click on the "View" link which will redirect you to the deployed link.
* The live version of the app can be found here..

### ElephantSQL 
* The app also uses ElephantSQL to host the database. 

The steps to use ElephantSQl are as follows..
* Log in to ElephantSQL or create an account for free. 
* Click on cretae a new instance
* Set up your plan, give the 'plan' the desired name, select Tiny Turtle(free) plan and leave tags blank. 
* Select the region, and select the nearest tou your location. 
* Click review, and if everything is ok, click on create instance down at the bottom. 
* From the instances section lcik on instance with the name that was just created. 
* Get the databse URL from the instance deatils page and copy, this will be inserted in the Heroku Config vars. 

## Credits
Code from external sources were used as a basis and built on top of in this project, They are credited below:
* The website has been built following [Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi).
* The code for the contact form with email backend was taken from [Email backend](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend).
* Code Institute "I think before i blog" have been used as insperation. 
* To deploy the site i have been using the videos in the "I think before i blog" part of the course.  
* Social media icons were sourced from [Font awesome](https://www.google.com).
* [W3Schools](https://www.google.com) used to research differnet syntaxes.
* Favicons used in this project came from [Icons8](https://icons8.com/icons/set/favicon-car) 
* The background image comes from [Pexels](https://www.pexels.com/sv-se/sok/car/).
[Am i Responsive](https://www.google.com) was used to check for responsivness.
* Github template used in this project come from [Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template).
* Fonts were taken from [Google fonts](https://fonts.google.com/).
