function filterSelection(){
  if(document.getElementById('username').checked) {
    document.getElementById('username_div').style.visibility = 'visible';
    document.getElementById('keyword_div').style.visibility = 'hidden';
  }
  else if(document.getElementById('keyword').checked) {
    document.getElementById('username_div').style.visibility = 'hidden';
    document.getElementById('keyword_div').style.visibility = 'visible';
  }
}

