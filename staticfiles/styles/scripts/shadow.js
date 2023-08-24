window.onload = function () {
  var hover = document.getElementById('hover');
  var logo = document.getElementById('logo');
  var menu = document.getElementById('menu');

  hover.onmouseout = function(e) {
    document.getElementById('header_shadow').style.opacity='0';
    logo.style.color='black';
    menu.querySelectorAll('li').forEach(item => item.style.color='black');
  };

  hover.onmouseover = function(e) {
    document.getElementById('header_shadow').style.opacity='1';
    logo.style.color='white';
    menu.querySelectorAll('li').forEach(item => item.style.color='white');
  };
}