var myHeaders = new Headers();
myHeaders.append("Cookie", "cookie");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("https://www.superheroapi.com/api.php/(api_key_mu)/(nomor_hero)/powerstats", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));