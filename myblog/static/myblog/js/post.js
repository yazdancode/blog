document.addEventListener('DOMContentLoaded', function() {
    // Form submission handling
    const commentForm = document.querySelector('form');
    if (commentForm) {
        commentForm.addEventListener('submit', function(e) {
            const textarea = this.querySelector('textarea');
            if (!textarea.value.trim()) {
                e.preventDefault();
                showMessage('لطفاً نظر خود را وارد کنید', 'error');
            } else {
                showMessage('در حال ارسال نظر...', 'success');
            }
        });
    }

    // Add hover effects to comments
    const comments = document.querySelectorAll('.comments-list li');
    comments.forEach(comment => {
        comment.classList.add('comment-item');
    });

    // Function to show messages
    function showMessage(text, type) {
        const messageClass = type === 'error' ? 'error-message' : 'success-message';
        const existingMessage = document.querySelector(`.${messageClass}`);

        if (existingMessage) {
            existingMessage.textContent = text;
            existingMessage.style.display = 'block';
        } else {
            const messageDiv = document.createElement('div');
            messageDiv.className = messageClass;
            messageDiv.textContent = text;
            commentForm.insertBefore(messageDiv, commentForm.firstChild);
        }

        setTimeout(() => {
            const message = document.querySelector(`.${messageClass}`);
            if (message) {
                message.style.display = 'none';
            }
        }, 3000);
    }

    // Enhance textareas with auto-resize
    const textareas = document.querySelectorAll('textarea');
    textareas.forEach(textarea => {
        textarea.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
});