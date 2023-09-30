window.onload = function() {
  const homeValueInput = document.getElementById('home-value-input');
  const taxOutput = document.getElementById('tax-output');

  homeValueInput.oninput = function() {
    const value = parseInt(homeValueInput.value);
    const result = 66000000 * value * 0.06765 / 8144600544;
    taxOutput.textContent = result.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  };
};