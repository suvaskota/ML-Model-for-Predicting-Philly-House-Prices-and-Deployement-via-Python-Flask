
var answer = document.getElementById("answer");
var submit = document.getElementById('submit');
var price = 0; 



function onClickedEstimatePrice() {
    console.log("Clicked");
    var years = document.getElementById("year");
    var sqFts = document.getElementById("sqFt");
    var bathroomss = document.getElementById("bathrooms");
    var bedroomss = document.getElementById("bedrooms");
    console.log("got info from fields");
    var url = "http://127.0.0.1:5000/predict_home_price"; 

    $.post(url, {
      year : parseFloat(years.value),
      sqFt: parseFloat(sqFts.value),
      bathrooms: parseFloat(bathroomss.value),
      bedrooms: parseFloat(bedroomss.value)
    },function(data, status) {
      console.log(data.estimated_price);
      price = data.estimated_price;
      answer.innerHTML = "$" + data.estimated_price.toString();
      console.log(status);
  });

}


// submit.addEventListener("click", function() {
//     onClickedEstimatePrice();
// });

// window.onload = onPageLoad;



