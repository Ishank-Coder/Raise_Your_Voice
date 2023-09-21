const steps = Array.from(document.querySelectorAll("form .step"));
const nextBtn = document.querySelectorAll("form .next-btn");
const prevBtn = document.querySelectorAll("form .previous-btn");
const form = document.querySelector("form");

nextBtn.forEach((button) => {
  button.addEventListener("click", () => {
    x = document.getElementById("nickName").value;
    // console.log("inputs",x);
    changeStep("next",x);
  });
});
prevBtn.forEach((button) => {
  button.addEventListener("click", () => {
    changeStep("prev","negative");
  });
});

// form.addEventListener("submit", (e) => {
//   e.preventDefault();
//   const inputs = [];
//   form.querySelectorAll("input").forEach((input) => {
//     const { name, value } = input;
//     inputs.push({ name, value });
//   });
//   // console.log(inputs);
//   form.reset();
// });

function changeStep(btn,x) {
  let index = 0;
  const active = document.querySelector(".active");
  index = steps.indexOf(active);
  steps[index].classList.remove("active");

  if (btn === "next") {
    if(index===1){
      index++;

    }
    else if (x === "student"){
      if(index===0){
        index++;
      }
    }
    
    
    
    index++;
  } else if (btn === "prev") {
    if(index===3){
      if(x!=="student"){
        index--;
      }
      
      
    }
    else if(index===2){
      
      index--;
    }
    
    
    index--;
  }
  steps[index].classList.add("active");
}


// function validateForm() {
//     // This function deals with validation of the form fields
//     var x, y, i, valid = true;
//     x = document.getElementsByClassName("step");
//     y = x[currentTab].getElementsByTagName("input");
//     // A loop that checks every input field in the current tab:
//     for (i = 0; i < y.length; i++) {
//       // If a field is empty...
//       if (y[i].value == "") {
//         // add an "invalid" class to the field:
//         y[i].className += " invalid";
//         // and set the current valid status to false
//         valid = false;
//       }
//     }
//     // If the valid status is true, mark the step as finished and valid:
//     if (valid) {
//       document.getElementsByClassName("step")[currentTab].className += " finish";
//     }
//     return valid; // return the valid status
//   }
  
// document.addEventListener('DOMContentLoaded', function() {
//   const form = document.querySelector('form');
//   const steps = form.querySelectorAll('.step');
//   let currentStep = 0;

//   function showStep(stepNumber) {
//     steps.forEach((step, index) => {
//       if (index === stepNumber) {
//         step.classList.add('active');
//       } else {
//         step.classList.remove('active');
//       }
//     });
//   }

//   form.querySelectorAll('.next-btn').forEach((button) => {
//     button.addEventListener('click', function(event) {
//       event.preventDefault();
//       currentStep++;
//       showStep(currentStep);
//     });
//   });

//   form.querySelectorAll('.previous-btn').forEach((button) => {
//     button.addEventListener('click', function(event) {
//       event.preventDefault();
//       currentStep--;
//       showStep(currentStep);
//     });
//   });
// });
