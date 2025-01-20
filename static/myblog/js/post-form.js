document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.form-group');

    if (form) {
        // Set author ID
        const authorInput = document.getElementById("elder");
        if (authorInput) {
            authorInput.value = name; // name is defined in the template
        }

        // Add character counters for title and excerpt
        const titleInput = form.querySelector('input[name="title"]');
        const excerptInput = form.querySelector('textarea[name="excerpt"]');

        if (titleInput) {
            addCharacterCounter(titleInput, 200); // Adjust max length as needed
        }

        if (excerptInput) {
            addCharacterCounter(excerptInput, 500); // Adjust max length as needed
        }

        // Form validation
        form.addEventListener('submit', function(e) {
            const requiredFields = form.querySelectorAll('input[required], textarea[required], select[required]');
            let isValid = true;

            requiredFields.forEach(field => {
                if (!field.value.trim()) {
                    isValid = false;
                    showError(field, 'This field is required.');
                } else {
                    clearError(field);
                }
            });

            if (!isValid) {
                e.preventDefault();
                // Scroll to first error
                const firstError = form.querySelector('.errorlist');
                if (firstError) {
                    firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
                }
            }
        });

        // Real-time validation
        form.querySelectorAll('input, textarea, select').forEach(field => {
            field.addEventListener('input', function() {
                if (this.value.trim()) {
                    clearError(this);
                }
            });
        });
    }
});

function addCharacterCounter(element, maxLength) {
    const counter = document.createElement('span');
    counter.classList.add('char-counter');
    element.parentNode.appendChild(counter);

    function updateCounter() {
        const remaining = maxLength - element.value.length;
        counter.textContent = `${remaining} characters remaining`;
        counter.style.color = remaining < 20 ? '#e53e3e' : '#718096';
    }

    element.addEventListener('input', updateCounter);
    updateCounter(); // Initial count
}

function showError(element, message) {
    clearError(element);
    const errorList = document.createElement('ul');
    errorList.classList.add('errorlist');
    const errorItem = document.createElement('li');
    errorItem.textContent = message;
    errorList.appendChild(errorItem);
    element.parentNode.insertBefore(errorList, element.nextSibling);
    element.classList.add('error');
}

function clearError(element) {
    const errorList = element.parentNode.querySelector('.errorlist');
    if (errorList) {
        errorList.remove();
    }
    element.classList.remove('error');
}