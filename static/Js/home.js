let slideIndex = 0;

function showSlides() {
  const slides = document.querySelectorAll(".slide");
  if (slideIndex >= slides.length - 3) {
    slideIndex = 0;
  }
  if (slideIndex < 0) {
    slideIndex = slides.length - 3;
  }
  const offset = -slideIndex * (100 / 3);
  document.querySelector(
    ".slides-container"
  ).style.transform = `translateX(${offset}%)`;
}

function prevSlide() {
  slideIndex--;
  showSlides();
}

function nextSlide() {
  slideIndex++;
  showSlides();
}
setInterval(nextSlide, 3000);

// Load Button
let loadMoreBtn = document.querySelector("#load-more-btn");
let currentItem = 3;

loadMoreBtn.onclick = () => {
  let cards = [...document.querySelectorAll(".card-product")];
  for (let i = currentItem; i < currentItem + 3; i++) {
    if (i < cards.length) {
      cards[i].style.display = "inline-block";
    }
  }
  currentItem += 3;

  if (currentItem >= cards.length) {
    loadMoreBtn.style.display = "none";
  }
};
