$( document ).ready(function() {
    getData('board');
    getData('hand');    
});

function getData (option) {
    fetch('http://127.0.0.1:5000/poker/getlast/'+option)
      .then((response) => response.json())
      .then((data) => {
        obj = data;
      })
      .then(() => {
        changeElement(option);
      });
};

function changeElement(elementID) {
    Board = JSON.parse(obj);
    document.getElementById(elementID).innerHTML = null ;
    for (const x in Board) {
        document.getElementById(elementID).innerHTML += Board[x].unicode;
      }
};

function dealCards() {
    fetch('http://127.0.0.1:5000/poker/dealcards')
    .then(() => {
        getData('board');
        getData('hand');
    });
}