document.getElementById("new_action").addEventListener("click", function(event) {
    event.preventDefault();
    document.getElementById("popup").style.display = "block";
  });
  
  document.getElementById("closePopup").addEventListener("click", function() {
    document.getElementById("popup").style.display = "none";
  });
  