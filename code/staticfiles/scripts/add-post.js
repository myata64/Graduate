const adminBtn = document.getElementById('admin_gears');
const adminMenu = document.getElementById('admin_menu');

adminBtn.addEventListener('click', function() {
  if (adminMenu.style.display === 'block') {
    adminMenu.style.display = 'none';
  } else {
    adminMenu.style.display = 'block';
    adminMenu.style.opacity = 0;
    let opacity = 0;
    const interval = setInterval(function() {
      opacity += 0.05;
      adminMenu.style.opacity = opacity;
      if (opacity >= 1) {
        clearInterval(interval);
      }
    }, 10);
  }
});