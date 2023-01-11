function filterSelection(){
  if(document.getElementById('username').checked) {
    document.getElementById('username_div').style.display = 'inline';
    document.getElementById('keyword_div').style.display = 'none';
  }
  else if(document.getElementById('keyword').checked) {
    document.getElementById('username_div').style.display = 'none';
    document.getElementById('keyword_div').style.display = 'inline';
  }

  var sentiment = document.getElementById("table");
  for(var i = 0, row; row = table.rows[i]; i++) {
    
  }
  if(sentiment === "5"){

  }
}
