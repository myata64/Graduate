//дожидаемся полной загрузки страницы
window.onload = function () {
    //ищем элемент по селектору
    var a = document.getElementById('hover');
    //вешаем на него события
    a.onmouseout = function(e) {
      document.getElementsByClassName('shoes_item1_before').style.display='block';
    //   document.getElementsByClassName('shoes_item1_hover').style.display='none';
    }
  
    a.onmouseover = function(e) {
      document.getElementsByClassName('shoes_item1_before').style.display='none';
    //   document.getElementsByClassName('shoes_item1_hover').style.display='block';
    };
  }