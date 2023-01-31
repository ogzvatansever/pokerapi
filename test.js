$( document ).ready(function() {
    getData();
});

var Board = 'test';

function getData (e) {
    fetch('http://127.0.0.1:5000/poker/')
      .then((response) => response.json())
      .then((data) => {
        obj = data;
      })
      .then(() => {
        console.log(JSON.parse(obj));
        test();
        //document.getElementById('test').innerHTML = obj;
      });
};

function test() {
    Board = JSON.parse(obj);
    for (const x in Board) {
        document.getElementById('test').innerHTML += Board[x].unicode;
      }
};