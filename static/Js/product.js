// let loadMoreBtn = document.querySelector('.load-more-btn');
//   let currentItem = 3;

//   loadMoreBtn.onclick = () => {
//     let cards = [...document.querySelectorAll('.card-product')];
//     for (let i = currentItem; i < currentItem + 3; i++) {
//       if (i < cards.length) {
//         cards[i].style.display = 'inline-block';
//       }
//     }
//     currentItem += 3;

//     if (currentItem >= cards.length) {
//       loadMoreBtn.style.display = 'none';
//     }
//   }
let loadMoreBtns = document.querySelectorAll('.load-more-btn');

loadMoreBtns.forEach(button => {
  button.onclick = () => {
    let category = button.getAttribute('data-category'); // Get the category of products associated with the button
    let cards = [...document.querySelectorAll(`.card-product[data-category="${category}"]`)]; // Select cards with the corresponding category

    let currentItem = 3;
    for (let i = currentItem; i < currentItem + 3; i++) {
      if (i < cards.length) {
        cards[i].style.display = 'inline-block';
      }
    }
    currentItem += 3;

    if (currentItem >= cards.length) {
      button.style.display = 'none';
    }
  };
});
