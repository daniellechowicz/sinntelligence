window.addEventListener('DOMContentLoaded', event => {
  // Toggle the side navigation.
  const sidebarToggle = document.body.querySelector('#sidebarToggle');
  if (sidebarToggle) {
    sidebarToggle.addEventListener('click', event => {
      event.preventDefault();
      document.body.classList.toggle('sb-sidenav-toggled');
      localStorage.setItem(
          'sb|sidebar-toggle',
          document.body.classList.contains('sb-sidenav-toggled'));
    });
  }
});


$('#overview').click(function(e) {
  $('.content').load('static/banner.html');
  e.preventDefault();
});




$('#edit').click(function(e) {
  $('.content').html('<h1>Edit here</h1>');
  e.preventDefault();
});