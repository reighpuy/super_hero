package main

import (
  "fmt"
  "net/http"
  "io/ioutil"
)

func main() {

  url := "https://www.superheroapi.com/api.php/(api_key_mu)/(nomor_hero)/powerstats"
  method := "GET"

  client := &http.Client {
  }
  req, err := http.NewRequest(method, url, nil)

  if err != nil {
    fmt.Println(err)
  }
  req.Header.Add("Cookie", "cookie")

  res, err := client.Do(req)
  defer res.Body.Close()
  body, err := ioutil.ReadAll(res.Body)

  fmt.Println(string(body))
}