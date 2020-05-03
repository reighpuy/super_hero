
var xhr = new XMLHttpRequest();
xhr.withCredentials = true;

xhr.addEventListener("readystatechange", function() {
  if(this.readyState === 4) {
    console.log(this.responseText);
  }
});

xhr.open("GET", "https://www.superheroapi.com/api.php/(api_key_mu)/(nomor_hero)/powerstats");
xhr.setRequestHeader("Cookie", "cookie");

xhr.send();