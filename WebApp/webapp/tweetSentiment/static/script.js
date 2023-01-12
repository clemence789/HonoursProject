function filterSelection(){
  //function that shows or hides the keyword/username fields based on which radio button is checked
  if(document.getElementById('username').checked) {
    document.getElementById('username_div').style.display = 'inline';
    document.getElementById('keyword_div').style.display = 'none';
  }
  else if(document.getElementById('keyword').checked) {
    document.getElementById('username_div').style.display = 'none';
    document.getElementById('keyword_div').style.display = 'inline';
  }

  //get tweets that have a sentiment score of 5
  var sentiment = document.getElementById("table");
  for(var i = 0, row; row = table.rows[i]; i++) {
    
  }
  if(sentiment === "5"){

  }
}
