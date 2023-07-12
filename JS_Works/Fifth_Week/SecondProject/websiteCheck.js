var url = prompt("Enter URL");
var xhr = new XMLHttpRequest();

xhr.open("GET", url);
xhr.send();

xhr.onreadystatechange = function(){

        console.log(this.status);

};

