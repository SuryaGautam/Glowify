let loadMoreBtn = document.querySelector('#load-more-btn');
  let currentItem = 3;

  loadMoreBtn.onclick = () => {
    let cards = [...document.querySelectorAll('.card-product')];
    for (let i = currentItem; i < currentItem + 3; i++) {
      if (i < cards.length) {
        cards[i].style.display = 'inline-block';
      }
    }
    currentItem += 3;

    if (currentItem >= cards.length) {
      loadMoreBtn.style.display = 'none';
    }
  }