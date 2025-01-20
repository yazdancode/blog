document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');

    // Add required class to form groups with required fields
    document.querySelectorAll('form [required]').forEach(field => {
        field.closest('p').classList.add('required');
    });

    // Add form group class to all form paragraphs
    document.querySelectorAll('form p').forEach(p => {
        p.classList.add('form-group');
    });

    // Form submission handling
    if (form) {
        form.addEventListener('submit', function(e) {
            const button = this.querySelector('button[type="submit"]');
            button.textContent = 'Updating...';
            button.disabled = true;

            // Re-enable button after short delay
            setTimeout(() => {
                button.disabled = false;
                button.textContent = 'Update Profile';
            }, 2000);
        });
    }

    // Add floating labels effect
    document.querySelectorAll('.form-group input, .form-group textarea').forEach(field => {
        field.addEventListener('focus', function() {
            this.classList.add('field-focus');
        });

        field.addEventListener('blur', function() {
            if (!this.value) {
                this.classList.remove('field-focus');
            }
        });

        if (field.value) {
            field.classList.add('field-focus');
        }
    });
});