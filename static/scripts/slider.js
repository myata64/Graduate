let slides = document.querySelectorAll('.slide');
let currentSlide = 0;
let prevBtn = document.querySelector('.prevBtn');
let nextBtn = document.querySelector('.nextBtn');

function nextSlide () {
    slides[currentSlide].className = 'slide';
    currentSlide = (currentSlide + 1) % slides.length;
    slides[currentSlide].className = ' showSlide';
}

function prevSlide () {
  slides[currentSlide].className = 'slide';
  currentSlide = (currentSlide - 1) % slides.length;

  if (currentSlide === -1) {
    currentSlide = slides.length -1;
  }
  slides[currentSlide].className = ' showSlide';
}

nextBtn.addEventListener('click', () => {
    nextSlide();
})

prevBtn.addEventListener('click', () => {
    prevSlide();
})

let autoSLide = setInterval(nextSlide, 4000);