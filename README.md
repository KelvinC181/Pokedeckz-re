# Pokedeckz (Capstone Project)

Pokedeckz is my first full stack Django website, it is a project based on my personal passion of the recently release Pokemon TCG Pocket.  The project utilizes html, css, javascript, python and bootstrap, alongside the Django framework to create a feature complete responsive font-end and back-end application.  The site mainly features a card library, and a dynamic deckbuilder.  While the project is mainly created manually, in this project, AI was used in user story generation, debugging, and testing.


![Responsice Mockup](documentation/readme/mockup.jpg)

## Design

The website is designed to create a place to create and share decks for the Pokemon TCG Pocket game.  I aimed in creating an intuative and interactive application that would be a fun and easy way for people to build decks.  As this project uses the Django framework, the design of the application was built around the concepts of models and views, so in the planning, I started with brainstorming features to build my models around, then expended on those freatures.

### User Stories

For users, I had 4 main users in mind: the developer, beginner players, verteran players, and the general user.  I took an approach where I had key features in mind before creating the user stories, then I used copilot to generate user stories for these features.

<img src="documentation/readme/story-prompting.jpg" alt="copilot user story prompting" width=100%>

<p style="margin-bottom: 20px;"></p>

Next I created issues after identifying the acceptance criteria and tasks associate with the user stories.  With this I identified details for the features I would like in the website.  Finally, I then decided their importance in the website and set their priority in the project (please see the linked project Pokedeckz User Stories).

### Layout and Color Scheme/Fonts

With the key features in mind I created a wireframe for each page I planned for, to ensure responsiveness I created 3 differnt layouts for each page targeting mobile, tablet and desktop devices.  In these layouts, I considered what I would believe to look best and is most natural to view on each screen size and designed my responsive grid/features accordingly.

<p style="margin-bottom: 20px;"></p>

As I had a clear theme, I took inspiration from the pokemon franchise's iconic color scheme of red, white and black.  I also wanted the website to be playful and intersting, so I went for a more imaginative and casual approach when deciding for fonts.

In the end, I settled on a color scheme of white as base color, red as the primary color, and black as a bonding agent between features.  I had yellow and blue as extra colors for other secondary features as a reference to the pokemon franchise.  

I picked Atma for the nav bar as the face of the website as it was playful but not too exaggerated, roboto for inner text for a clean, clear representation of the inner elements.

## Features 

In this project, all features revolves around the main feature of the deck builder.
There are 4 major features:
 - Deck Builder: 
    - allows the building and saving of a deck
    - dynamically displayed deck as it is built
    - click library cards to add to deck
    - click cards in deck to remove from deck
    - <img src="documentation/readme/deckbuilder.jpg" alt="deck builder" width=100%>

 - Card Library:
    - displays all cards in the card database
    - <img src="documentation/readme/home.jpg" alt="card library" width=100%>

 - Deck Forum:
    - displays all public decks
    - allows users to interact using comments (in development)
    - <img src="documentation/readme/decklist.jpg" alt="deck list" width=100%>
    - <img src="documentation/readme/deckdetail.jpg" alt="deck detail" width=100%>

 - Card Detail(in development):
    - displays all details of a card

In the following section, the features will be explained according to the Django framework, which is Model, Views, and Templates.

### Django Deepdive

- __Models__

  - The two main models for the current version of the application is the Card model and the Deck model.

  
<img src="documentation/readme/model.png" alt="model relations" width=100%>

<p style="margin-bottom: 20px;"></p>

- __Views__

  - card-library: a display of all cards in the card database 

  - deckbuilder: a combination of deck-form and card database.  Allows a submission of an instance of deck model and displays the card database for an interacttive deck building experience

  - deck-list/my-decks: a display of all public decks and all decks of the user respectively

  - deck-detail: a display of a selected deck instance

  - edit-deck: allows the modification of the selected deck instance

  - delete-deck: deletes the selected deck instance

  - card-detail(in developement): displays the full details of a card instance


<p style="margin-bottom: 20px;"></p>

- __Templates__

  - base.html: base for all templates

  - card_library.html: template for card libray, displays all cards in card database

  - deck_list/my_decks.html: templates for deck list/mt decks, displays filtered results of decks

  - deck_detail.html: template for deck detail, displays the cards in the choosen deck

  - deckbuilder.html: template for deckbuilder and edit deck, displays the dynamically interactive form and the card library

  - card_detail.html: template for card details, displays all details of cards (in development)

  - login/logout/signup.html: templates for authentication

<p style="margin-bottom: 20px;"></p>

### Features Left to Implement

- Comments: allow users to comment on the public decks.
- Upgrade card model: to include more information in the card model e.g poekmon type, hp.
- Display main card in deck-list: to include the main card of the deck in the deck list/ my decks views
- Filter and seach: improve user experience by allowing for filter and search functionality for the card library and deck list/my decks views.

## Testing 

The project went through manual testing on the live website.  Then I implemented automatic tests and validators to throughly test for errors.

### Unit Testing

unit tests were suggested by copilot, then was futher prompted to add additional tests to further test functionalities that were not included in the initial prompt.
 
<img src="documentation/readme/test-prompt.jpg" alt="W3C validating card library page" width=100%>

__DeckDetailViewTest__
- test_deck_detail_view: Verifies that the deck_detail view:

  - Returns a 200 status code.

  - Uses the deckbuilder/deck_detail.html template.

  - Contains the names of the cards in the deck_content.

__MyDecksViewTest__
- test_my_decks_view: Verifies that the my_decks view:

  - Returns a 200 status code.

  - Uses the deckbuilder/my_decks.html template.

  - Returns only the decks belonging to the logged-in user.

__DeckbuilderViewTest__
- test_deckbuilder_view_get: Verifies that the deckbuilder view:

  - Returns a 200 status code.

  - Uses the deckbuilder/deckbuilder.html template.

- test_deckbuilder_view_post_valid_data: Verifies that submitting valid data to the deckbuilder view:

  - Returns a 302 status code (indicating a successful redirect after saving the deck).

- test_deckbuilder_view_post_invalid_data: Verifies that submitting invalid data to the deckbuilder view:

  - Returns a 200 status code (indicating form errors and re-rendering the same page).

  - Displays the appropriate form error messages.

__EditDeckViewTest__
- test_edit_deck_view_get: Verifies that the edit_deck view:

  - Returns a 200 status code.

  - Uses the deckbuilder/deckbuilder.html template.

  - Gets the correct data from the existing deck (deck name, deck content, additional info).

- test_edit_deck_view_post: Verifies that submitting valid data to the edit_deck view:

  - Returns a 302 status code (indicating a successful redirect after saving the deck).

__DeleteDeckViewTest__
- test_delete_deck_view: Verifies that submitting a POST request to the delete_deck view:

  - Returns a 302 status code (indicating a successful redirect after deleting the deck).

  - The deck no longer exists in the database.

__DeckFormTest__
- test_deck_form_valid_data: Verifies that the DeckForm:

  - Is valid when provided with correct data.

- test_deck_form_no_data: Verifies that the DeckForm:

  - Is invalid when no data is provided.

  - Generates the correct number of error messages for missing required fields.

### Validator Testing 

- HTML
  - each page was passed through the official W3C validator
    - <img src="documentation/readme/hval1.jpg" alt="W3C validating card library page" width=100%>
    - <img src="documentation/readme/hval2.jpg" alt="W3C validating deck list page" width=100%>
    - <img src="documentation/readme/hval3.jpg" alt="W3C validating deck detail page" width=100%>
    - <img src="documentation/readme/hval4.jpg" alt="W3C validating deck-builder page" width=100%>

- CSS
  - No errors were found when passing through the official W3C(Jigsaw) validator
  - <img src="documentation/readme/cval.jpg" alt="W3C validating card library page" width=100%>

-JS
  -No error, only warning found when passing through the JS hint validator
  - <img src="documentation/readme/jval.jpg" alt="W3C validating card library page" width=100%>

- Lighthouse
  - Good scores were achieved in lighthouse
  - Best practice score lower due to http
  
  <p style="margin-bottom: 20px;"></p>
  <img src="documentation/readme/lh1.jpg" alt="lighthouse for home page" width=28%>
  <img src="documentation/readme/lh2.jpg" alt="lighthouse for deck builder" width=28%>
  <img src="documentation/readme/lh3.jpg" alt="lighthouse for deck detail" width=28%>
 
  <p style="margin-bottom: 20px;"></p>

### Unfixed Bugs
- When passing through the JS hint validator, it mentions that functions declared within loops referencing an outer scoped variable may lead to confusing semantics for the function:
    - for (let cardImg of cardImgs) {
        cardImg.addEventListener('click', () => addCard(cardImg));
      }
    
    - for (let deckAreaImg of deckAreaImgs) {
        deckAreaImg.addEventListener('click', () => deleteCard(deckAreaImg));
    }
    
    - for (let closeButton of closeButtons) {
        closeButton.addEventListener('click', function() {
            deleteDeckModal.classList.add('hidden');
        });
    }

 I currently could not figure out a way to change this without breaking the script, currently it poses no probelm functionally to the site, so this will be investigated in future iterations


## Deployment

- The site was deployed to Heroku. The steps to deploy are as follows: 
  - In the GitHub repository, ensure the version in branch is the version desired
  - Ensure debug is set to false
  - manually deploy the branch

The live link can be found here - https://pokedeckz-66be6c7e2c2c.herokuapp.com/


## Credits 

This project was done during CI full stack developer bootcamp.  The design process, some page structures and features are inspired by and further developed on from the walk-projects of the course.

### AI Assistance Declaration

This project was developed with the assistance of AI tools, including GitHub Copilot.  Co-pilot was used to assist the completetion of my project in terms of efficiency.

Co-pilot was used in the following context:
  - generation of user story
  - generation of unit tests
  - code debugging

### Content 

- All text content are prompted and created by GitHub Copilot and futher modifed to fit the website.
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)
- Fonts can be found on google fonts

### Media

- All Pokémon images, names, characters, and related marks are trademarks and copyright of The Pokémon Company, Nintendo, Game Freak, or Creatures Inc. (“Pokémon Rights Holders”).
- The logos for the find help page were taken from google search:
- [Pokemon Logo](https://www.cleanpng.com/png-super-smash-bros-melee-computer-icons-pok-ball-3519133/)