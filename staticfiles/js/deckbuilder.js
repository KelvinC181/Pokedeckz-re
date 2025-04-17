// Add event listeners
document.addEventListener('DOMContentLoaded', function() {
    for (let cardImg of cardImgs) {
        cardImg.addEventListener('click', () => addCard(cardImg));
    }
    
    for (let deckAreaImg of deckAreaImgs) {
        deckAreaImg.addEventListener('click', () => deleteCard(deckAreaImg));
    }

    //show delete deck modal on delete button click
    if (deleteDeckButton){
    deleteDeckButton.addEventListener('click', function() {
        deleteDeckModal.classList.remove('hidden');
    });
    }

    //hide delete deck modal on close button click
    for (let closeButton of closeButtons) {
        closeButton.addEventListener('click', function() {
            deleteDeckModal.classList.add('hidden');
        });
    }
});


const cardImgs = document.querySelectorAll('.library-img');
const textarea = document.querySelector('textarea[name="deck_content"]');
const deckarea = document.querySelector('.deck-area');
const deleteDeckButton = document.querySelector('.delete-deck');
const closeButtons = document.querySelectorAll('.close-button');
const deckAreaImgs = document.querySelectorAll('.deck-img');
const deleteDeckModal = document.getElementById('delete-modal');

/**
 * ADD card to deck
 * 1. append card to deck content field
 *  1.1 onlick: get card-id
 *  1.2 get content of deck_content
 *  1.3 check if deck array already contains 2 of the card id
 *      1.3.1 
 *  1.4 check if deck array is longer then 20
 *      1.4.1 if not append id
 *      1.4.2 if yes return error message
 * 
 * 2. add img to deck area dynamically
 *  2.1 onclick: get card img src
 *  2.2 create html element ( card img div + img )
 *      2.2.1 create card div
 *      2.2.2 create img 
 *      2.2.3 append img to div
 *      2.2.4 append div to deck area
 */

//2. add img to deck area dynamically
const addCardImg = (cardId, cardImgSrc, cardImgAlt) => {
    //create card div
    let cardDiv = document.createElement('div');
    cardDiv.classList.add('col-12', 'col-md-3', 'col-lg-2', 'my-2');


    //create img 
    let deckImg = document.createElement('img');
    deckImg.classList.add('deck-img');
    deckImg.setAttribute('src', cardImgSrc);
    deckImg.setAttribute('card-id', cardId);
    deckImg.setAttribute('alt', cardImgAlt);

    //append img to div
    cardDiv.appendChild(deckImg);

    //append div to deck area
    deckarea.appendChild(cardDiv);

    //add event listener for deletecard fuction
    deckImg.addEventListener('click', () => deleteCard(deckImg));
};


//1. append card to deck content field
const addCard = (cardImg) => {
    // Get the card ID/src/alt
    let cardId = cardImg.getAttribute('data-card-id');
    let cardImgSrc = cardImg.getAttribute('src');
    let cardImgAlt = cardImg.getAttribute('alt');

    // Get content of deck_content
    let deckContent = textarea.value;
    let deckArray;
    if (deckContent) { 
        deckArray = deckContent.split(',');
    } else {
        deckArray = []; //removes empty value from deck content
    }
    

    // Check if the deck array already contains 2 of the card ID
    const cardCount = deckArray.filter(id => id === cardId).length;
    if (cardCount >= 2) {
        alert('Cannot add more than 2 of the same card.');
        return;
    } else {
        // check if deck array is longer than 20
        if (deckArray.length<20) {
            // append card ID to text area
            deckArray.push(cardId);
            textarea.value = deckArray.join(',');
            addCardImg (cardId, cardImgSrc, cardImgAlt);
        } else {
            alert('deck can only contain 20 cards');
            return;
        }
    }
    
};


/**
 * DELETE card from deck
 * 1. delete card-id from text-area
 *  1.1 onlick: get card-id
 *  1.2 get content of deck_content
 *  1.3 delete card id from array
 *      1.3.1 get index of id in array
 *      1.3.2 splice id from array
 * 
 * 2. delete img from deck area dynamically
 *  2.1 delete parent
 */

//1. delete card-id from text-area
const deleteCard = (deckImg) => {
    //get card-id
    let cardId = deckImg.getAttribute('data-card-id');

    //get content of deck_content
    let deckContent = textarea.value;
    let deckArray = deckContent.split(',');

    //get index of id in array
    let idPosition = deckArray.indexOf(cardId);

    //splice id from array
    if (idPosition >-1) {
        deckArray.splice(idPosition,1);
    }
    textarea.value = deckArray.join(',');

    //2. delete img from deck area dynamically
    deckImg.parentElement.remove();
};
