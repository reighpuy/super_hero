var settings = {
  "url": "https://www.superheroapi.com/api.php/(api_key_mu)/(nomor_hero)/powerstats",
  "method": "GET",
  "timeout": 0,
  "headers": {
    "Cookie": "cookie"
  },
};

$.ajax(settings).done(function (response) {
  console.log(response);
});