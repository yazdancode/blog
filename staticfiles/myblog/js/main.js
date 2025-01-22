var btn1 = document.querySelector('#green');
var btn2 = document.querySelector('#red');

btn1.addEventListener('click', function() {

    if (btn2.classList.contains('red')) {
      btn2.classList.remove('red');
    }
  this.classList.toggle('green');

});

btn2.addEventListener('click', function() {

    if (btn1.classList.contains('green')) {
      btn1.classList.remove('green');
    }
  this.classList.toggle('red');

});

/* myblog/static/myblog/js/main.js */
document.addEventListener('DOMContentLoaded', function() {
    // Handle form submissions with AJAX
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();

            const button = form.querySelector('button');
            const countSpan = form.querySelector('span');

            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
                },
                body: new FormData(form)
            })
            .then(response => response.json())
            .then(data => {
                // Update counts
                if (countSpan) {
                    countSpan.textContent = data.count;
                }

                // Toggle button states
                if (data.action === 'like' || data.action === 'dislike') {
                    button.disabled = data.active;
                }

                // Update share button text
                if (data.action === 'share') {
                    button.textContent = data.shared ? 'لغو اشتراک‌گذاری' : 'اشتراک‌گذاری';
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    });

    // Add smooth scrolling for all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});