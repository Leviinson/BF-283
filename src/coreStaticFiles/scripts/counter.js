'use strict'

// COUNTER

document.addEventListener('DOMContentLoaded', function () {
  document.addEventListener('click', async (event) => {
    const decrementBtn = event.target.closest('.decrement');
    const incrementBtn = event.target.closest('.increment');

    if (!decrementBtn && !incrementBtn) {
      return;
    }

    const card = event.target.closest('.product-card');
    const countSpan = card.querySelector('.count');
    let count = +countSpan.textContent || 1;

    if (decrementBtn && count <= 1) {
      return;
    }

    const totalPriceElement = document.querySelector('.cart-total-price');
    const csrfmiddlewaretoken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const id = card.dataset.productId;
    // const region = document.querySelector('.cart-cards-container').dataset?.region || '';
    const region = document.querySelector('.header-container').dataset.region;

    count = decrementBtn ? count - 1 : count +1;
    const action = decrementBtn ? 'decreace' : 'increace';
    const isBouquet = card.dataset.isBouquet.toLowerCase() === "true";

    try {
      const config = {
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfmiddlewaretoken,
        }
      };
      let requestBody
      if (isBouquet) {
        const bouquetSize = parseInt(card.dataset.selectedSize);
        if (!isNaN(bouquetSize) && bouquetSize % 1 === 0) {
          requestBody = { id, amount: count, csrfmiddlewaretoken, bouquet_size: bouquetSize };
        } else {
          requestBody = { id, amount: count, csrfmiddlewaretoken };
        }
         
      } else {
          requestBody = { id, amount: count, csrfmiddlewaretoken };
      }

      const response = await axios.put(
        `http://0.0.0.0:80/${region}/cart/`,
        requestBody,
        config
      );

      if (response.status === 204) {
        countSpan.textContent = count;
        setTotalCount(card, action);
      }

      if (response.status === 204 && decrementBtn && totalPriceElement) {
        decreaseTotalPrice(card);
      }

      if (response.status === 204 && incrementBtn && totalPriceElement) {
        increaseTotalPrice(card);
      }
    } catch (error) {
      console.error('Помилка PUT-запиту:', error);
    }
  })
});
