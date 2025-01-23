// Add onclick event listeners
document.addEventListener("DOMContentLoaded", function() {
    for (let cardImg of cardImgs) {
        cardImg.addEventListener("click", () => addCard(cardImg));
    }
})

const cardImgs = document.querySelectorAll('.library-img');
const textarea = document.querySelector('textarea[name="deck_content"]');
const deckarea = document.querySelector('.deck-area')

/**
 * ADD card to deck
 * 1. append card to deck content field
 *  1.1 onlick: get card-id
 *  1.2 get content of deck_content
 *  1.2 check if deck array is longer then 20
 *      1.2.1 if not append id
 *      1.2.2 if yes return error message
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
const addCardImg = (cardId, cardImgSrc) => {
    //create card div
    let cardDiv = document.createElement('div')
    cardDiv.classList.add('col-12', 'col-md-3', 'col-lg-1', 'my-2')


    //create img 
    let deckImg = document.createElement('img')
    deckImg.setAttribute('src', cardImgSrc)
    deckImg.setAttribute('card-id', cardId)

    //append img to div
    cardDiv.appendChild(deckImg);

    //append div to deck area
    deckarea.appendChild(cardDiv);
}


//1. append card to deck content field
const addCard = (cardImg) => {
    // Get the card ID
    let cardId = cardImg.getAttribute('card-id');
    let cardImgSrc = cardImg.getAttribute('src')

    // Get content of deck_content
    let deckContent = textarea.value;
    let deckArray;
    if (deckContent) { 
        deckArray = deckContent.split(',');
    } else {
        deckArray = []; //removes empty value from deck content
    }
    
    // append card ID to text area
    deckArray.push(cardId);
    textarea.value = deckArray.join(',');

    console.log(cardImgSrc);
    addCardImg (cardId, cardImgSrc)

}



