# Carblog 

## Description 

This is the fourth project for the Code Institute Diploma in Software Development.

CarBlog is a webiste built in Django using Python, JavaScript, CSS/Bootstrap and HTML. 
It enables users to create and share blog posts with people around the world. It is targeted towards people who like cars and want to have a read about them, and share their thoughts. Users have the ability to create posts, categorys and their own profile. They can link their personal accounts in their profile. The profile is also editable.  They also can like posts and leave a comment. If wanted the user can contact Carblog via email.
The site provides user authentication and a Full CRUD functionality.

# Project Goals

## User Goals 
* To be able to create blog posts. 
* To be able to Comment and like on posts. 
* To be able to have a profile page. 
* To be able to have CRUD functionality whilst being logged in. 

## Site Owner Goals
* To provide a platform where users can add posts and share their thoughts.
* To provide a enjoyable user experince where users want to come back and read, update and create posts. 
* To have a contact form where users can give feedback. 

# User Experience

* Carblog is inteded to be a friendly community site where users can create and share their own thoughts on cars with others. Users will also be able to see other peoples posts and interact with them via comments or likes. 

# Agile development 
An Agile approach to creating this app has been applied. GitHub's projects was used to track user stories and implement ideas based on their level of importance for allowing use of the app with no loss of functionality or user experience. 

By using AGILE methodology in this project I was able to deliver a site which had all required functionality and some more. Due to time limit on this project I was not able to incorporate all initial listed features, but this is where an AGILE approach is great. The project displays this by having User stories in the Done section and the ones which decided to be left for future put in the future implementation.

## User stories

1. As a site user, i can add blog posts so that i can interact with others. 
2. As a site user, i can create posts so that i can interact with other people. 
3. As a site user, i can edit my blog post so that i can update the post in the future.
4. As a site user, i can delete my posts so that i don't have my posts displaying forever.
5. As a site user, i can register an account so that i can like posts.
6. As a site user/admin, i can add categories so that the blog posts are separated in their own category.
7. As a site user, i can contact the site admin so that i can communicate via email.
8. As a site user, i can like or unlike a post so that i can interact with the content.
9. As a site user, i can leave comments on posts so that i can be involved in the conversation.
10. As a site user, i can Create, read, update and delete posts so that i can manage my content.
11. As a site user, i can have my own profile page so that i can provide my information.
12. As a site user, i can edit my settings so that i can update my information in the future.
13. As a site admin, i can create draft posts so that i can finish writing them later.
14. As a Site user, i can approve or disapprove comments so that i can filter out comments.
15. As a Site user, i can add a image to my post so that i have a image with my text.

# Design

## CRUD Functionality
* Create - Users can create, account, profile, post, comment, like. 
* Read - Users can view post that other people have written and also their profile. 
* Update - Users can update their profile, posted posts and likes. 
* Delete - Users can delete posts, comments and likes. 

## Colors
The colour scheme used in this project was chosen with simplicity in mind. The colour scheme is used throughout all pages to ensure contrast readability and an overall good user experience.

## Fonts 
Google Fonts was used on deciding on the fonts for the website. "Zen dots with a fallback of sans-serif" was the ideal for the website.

## Site structure

### Pages
User experience was one of the main driving factors in this project. A simple, clear and easy to navigate app was the desired outcome. To achieve this there is  a sticky nav bar with links at the top. In the form of a hamburger toggle button if using a small screen device in which all links will be listed vertically.

The website consists of the following sections: 
#### If not logged in 
When the user is not logged in they are able to read post on the home page and visit the authors profile page. Posts will be displayed in order by date of most recent.
* Register, the user can register via a form. 
* Login, the user can log in.
* Categories, here the user can select a specific category to read. 
* Contact page, here the user can contact carblog via a email.  
* Post page, when a user select a post to read they are not able to like the post nor can they leave a comment.
#### If logged in 
When the user is logged in their name will appear in the navbar with a hello message. They are able to read post on the home page, posts will be displayed in order by date of most recent.
* Add post, the user can create a post. 
* Add Category, the user can add a category.
* Logout, the user is able to logout.
* Drop down Profile, the dropdown menu consist of...
    * Edit settings where the user can edit their settings, email, password, username and so on. 
    * Show profile, this page shows the user their profile page. 
    * Edit Profile page, here the user can edit their bio and social links via a form which will be update upon save.
* Post page, when a user select a post to read they are able to like or unlike the post and leave a comment.

