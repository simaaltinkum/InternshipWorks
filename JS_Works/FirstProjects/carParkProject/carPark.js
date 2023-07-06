class Car {
    constructor(plate, driver, entering_right) {
        this.plate = plate;
        this.driver = driver;
        this.entering_right = entering_right; 
    }
}

var cList = []; 

while (true) {
    var select = prompt("What is your selection? Write 1 to add a car, 2 to park, 3 to show info, 4 to quit: ");

    if (select == 1) {
        var plate = prompt("Please write the plate:");
        var driver = prompt("Please write your name:");
        var entering_right = prompt("Entering right (1 or 0):");
        cList.push(new Car(plate, driver, entering_right)); 
    } else if (select == 2) {
        var plate2 = prompt("Please write your plate:");
        var end = false;
        for (var i = 0; i < cList.length; i++) { 
            if (plate2 == cList[i].plate && cList[i].entering_right == 1) {
                end = true;
                if (end) {
                    console.log("Welcome");
                } else {
                    console.log("You can't enter");
                }
            }
        }
        
    } else if (select == 3) {
        for (var i = 0; i < cList.length; i++) { 
            console.log(cList[i].plate, cList[i].driver, cList[i].entering_right);
        }
    } else if (select == 4){
        console.log("Quiting...")
        break;
    }
    else {
        console.log("Invalid");
    }
}