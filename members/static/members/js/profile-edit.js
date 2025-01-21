// profile-edit.js
document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const form = document.querySelector('form');
    const inputs = form.querySelectorAll('input, textarea, select');

    // Add custom validation styles
    inputs.forEach(input => {
        input.addEventListener('blur', function() {
            validateField(input);
        });
    });

    form.addEventListener('submit', function(e) {
        let isValid = true;
        
        inputs.forEach(input => {
            if (!validateField(input)) {
                isValid = false;
            }
        });

        if (!isValid) {
            e.preventDefault();
            scrollToFirstError();
        }
    });

    // Field validation function
    function validateField(input) {
        const value = input.value.trim();
        let isValid = true;

        // Remove existing error messages
        const existingError = input.parentElement.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }

        // Required field validation
        if (input.hasAttribute('required') && !value) {
            showError(input, 'This field is required');
            isValid = false;
        }

        // Email validation
        if (input.type === 'email' && value) {
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(value)) {
                showError(input, 'Please enter a valid email address');
                isValid = false;
            }
        }

        // Update input styles based on validation
        if (isValid) {
            input.classList.remove('invalid');
            input.classList.add('valid');
        } else {
            input.classList.remove('valid');
            input.classList.add('invalid');
        }

        return isValid;
    }

    // Show error message
    function showError(input, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.textContent = message;
        input.parentElement.appendChild(errorDiv);
    }

    // Scroll to first error
    function scrollToFirstError() {
        const firstError = document.querySelector('.invalid');
        if (firstError) {
            firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }

    // Handle file input preview if present
    const fileInput = form.querySelector('input[type="file"]');
    if (fileInput) {
        const previewContainer = document.createElement('div');
        previewContainer.className = 'image-preview';
        fileInput.parentElement.appendChild(previewContainer);

        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file && file.type.startsWith('image/')) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    previewContainer.innerHTML = `
                        <img src="${e.target.result}" alt="Preview" style="max-width: 200px; max-height: 200px;">
                    `;
                };
                reader.readAsDataURL(file);
            } else {
                previewContainer.innerHTML = '';
            }
        });
    }

    // Unsaved changes warning
    let formChanged = false;
    
    inputs.forEach(input => {
        input.addEventListener('change', () => {
            formChanged = true;
        });
    });

    window.addEventListener('beforeunload', (e) => {
        if (formChanged) {
            e.preventDefault();
            e.returnValue = '';
        }
    });

    // Clear warning when form is submitted
    form.addEventListener('submit', () => {
        formChanged = false;
    });
});