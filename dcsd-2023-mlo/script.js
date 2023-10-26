window.onload = function() {
  const homeValueInput = document.getElementById('home-value-input');
  const taxOutput = document.getElementById('tax-output');

  homeValueInput.oninput = function() {
    const value = parseInt(homeValueInput.value);
    const result = value * 0.06765 * 5.912 / 1000;
    taxOutput.textContent = result.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
  };
};