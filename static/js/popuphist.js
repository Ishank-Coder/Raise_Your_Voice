document.addEventListener('DOMContentLoaded', function() {
    const historyButtons = document.querySelectorAll('.history-button');
    const historyPopup = document.getElementById('history-popup');
    const closeHistoryPopup = document.getElementById('closeHistoryPopup');
  
    historyButtons.forEach(function(button) {
      button.addEventListener('click', function(event) {
        event.preventDefault();
        historyPopup.style.display = 'block';
      });
    });
  
    closeHistoryPopup.addEventListener('click', function() {
      historyPopup.style.display = 'none';
    });
  });

  document.addEventListener('DOMContentLoaded', function() {
    const dropdownButtons = document.querySelectorAll('.dropdown-btn');
  
    dropdownButtons.forEach(function(button) {
      button.addEventListener('click', function() {
        this.classList.toggle('active');
        const content = this.nextElementSibling;
        if (content.style.display === 'block') {
          content.style.display = 'none';
        } else {
          content.style.display = 'block';
        }
      });
    });
  });
   