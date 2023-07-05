    var chickenNum = prompt("How many chickens do you have?: ");
    //var chickenWeightMin = ("What is the minimum weight of a chicken?: " )
    var chickenWeightMax = prompt("What is the maximum weight of a chicken?: ");
    var day = prompt("How many days will you measure?: ");
      
function calculate() {
    var total = 0;
    var totalChicken = 0;
   
    for (var i = 1; i <= day; i++) {
      var chickenRand = Math.floor(Math.random() * chickenNum + 1);
      console.log(i + ". day " + chickenRand + " chicken(s) measured.");
      totalChicken += chickenRand;

      for (var j = 1; j <= chickenRand; j++) {
        let weightRand = Math.floor(Math.random() * (chickenWeightMax));
        console.log(j + ". chicken weight: " + weightRand);
        total += weightRand;
      }
      
      console.log("Uploaded total weight: " + total);
      console.log("Average weight: " + total / totalChicken);
      
    }
  }

  calculate();
  console.log("ok");
