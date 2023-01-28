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
}

function filter(){
  document.getElementById('table_neg').style.display = 'inline';
  document.getElementById('neg_button').style.display = 'none';
}

function filterPersonal(){
  document.getElementById('table_neg_personal').style.display = 'inline';
  document.getElementById('neg_button_personal').style.display = 'none';
}
