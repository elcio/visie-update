
const nome_input = document.querySelector('#nome')
const watcher_input = document.querySelector('#watcher')
const location_span = document.querySelector('#location')
let location_watcher = 0

if(localStorage.nome){
  nome_input.value = localStorage.nome
}

function salvaNome(){
  localStorage.nome = nome_input.value
}

function esquecer(){
  localStorage.clear()
  nome_input.value = ''
  nome_input.focus()
}

function changeLocation(){
  if(watcher_input.checked){
    location_watcher = navigator.geolocation.watchPosition(position => {
      location_span.innerHTML = `
        <strong>Latitude:</string> ${position.coords.latitude} /
        <strong>Longitude:</string> ${position.coords.longitude}
      `
    })
  }else{
    navigator.geolocation.clearWatch(location_watcher)
    location_span.innerHTML = ""
  }
}
