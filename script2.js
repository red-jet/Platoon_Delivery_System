document.getElementById('GetValue').addEventListener('click', GetValue);

function GetValue(){
  fetch('value.txt')
  .then(response => response.text())
  .then((data) => {
    document.getElementById('display').innerHTML = data;
  })
}
