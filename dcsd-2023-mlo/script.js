window.onload = function() {
  const slides = document.getElementsByClassName('slide');
  const navDots = document.querySelectorAll('#nav-dots li');
  let currentSlide = 0;

  function showSlide(n) {
    slides[currentSlide].style.display = 'none';
    slides[n].style.display = 'block';
    navDots[currentSlide].classList.remove('active');
    navDots[n].classList.add('active');
    currentSlide = n;
    window.scrollTo(0, 0);
  }

  showSlide(0);

  const homeValueInput = document.getElementById('home-value-input');
  const taxOutput = document.getElementById('tax-output');

  homeValueInput.oninput = function() {
    const value = parseInt(homeValueInput.value);
    const result = 66000000 * value * 0.06765 / 8144600544;
    taxOutput.textContent = result.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  };

  document.addEventListener('keydown', function(event) {
    if (document.activeElement === homeValueInput) {
      return;
    }

    if (event.key === 'ArrowLeft' && currentSlide > 0) {
      showSlide(currentSlide - 1);
    } else if (event.key === 'ArrowRight' && currentSlide < slides.length - 1) {
      showSlide(currentSlide + 1);
    }
  });

  navDots.forEach((dot, index) => {
    dot.addEventListener('click', function() {
      showSlide(index);
    });
  });
};