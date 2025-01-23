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
 */


const cardImgs = document.querySelectorAll('.library-img');
let textarea = document.querySelector('textarea[name="deck_content"]');

const addCard = (cardImg) => {
    // Get the card ID
    let cardId = cardImg.getAttribute('card-id');
    
    // Get the current value of the textarea
    let deckContent = textarea.value;
    if (deckContent) {
        deckArray = deckContent.split(',');
    } else {
        deckArray = [];
    }
    
    // append card ID to text area
    console.log(cardId);
    deckArray.push(cardId);
    textarea.value = deckArray.join(',');

    let sendContent = textarea.value

    console.log(sendContent);
}

// Add an onclick event listener
document.addEventListener("DOMContentLoaded", function() {
    for (let cardImg of cardImgs) {
        cardImg.addEventListener("click", () => addCard(cardImg));
    }
})
