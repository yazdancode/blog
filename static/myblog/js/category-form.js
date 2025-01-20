document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-group');

    if (form) {
        // Add required attribute to inputs
        form.querySelectorAll('input[type="text"]').forEach(input => {
            input.required = true;
        });

        // Form validation
        form.addEventListener('submit', function(e) {
            const inputs = form.querySelectorAll('input[type="text"]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.classList.add('error');

                    // Create or update error message
                    let errorMsg = input.nextElementSibling;
                    if (!errorMsg || !errorMsg.classList.contains('errorlist')) {
                        errorMsg = document.createElement('ul');
                        errorMsg.classList.add('errorlist');
                        const li = document.createElement('li');
                        li.textContent = 'This field is required.';
                        errorMsg.appendChild(li);
                        input.parentNode.insertBefore(errorMsg, input.nextSibling);
                    }
                } else {
                    input.classList.remove('error');
                    const errorMsg = input.nextElementSibling;
                    if (errorMsg && errorMsg.classList.contains('errorlist')) {
                        errorMsg.remove();
                    }
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });

        // Real-time validation
        form.querySelectorAll('input[type="text"]').forEach(input => {
            input.addEventListener('input', function() {
                if (this.value.trim()) {
                    this.classList.remove('error');
                    const errorMsg = this.nextElementSibling;
                    if (errorMsg && errorMsg.classList.contains('errorlist')) {
                        errorMsg.remove();
                    }
                }
            });
        });
    }
});
Last edited 1 minute ago


