document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('.list-group-item');

    // Add entrance animation with delay
    listItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.1}s`;
        item.classList.add('new-category');
    });

    // Add hover sound effect (subtle)
    const hoverSound = new Audio('/static/myblog/sounds/hover.mp3');
    listItems.forEach(item => {
        item.addEventListener('mouseenter', () => {
            hoverSound.volume = 0.1;
            hoverSound.currentTime = 0;
            hoverSound.play().catch(() => {}); // Ignore errors if sound can't play
        });
    });

    // Add touch support for mobile
    listItems.forEach(item => {
        let touchStartX = 0;
        item.addEventListener('touchstart', (e) => {
            touchStartX = e.touches[0].clientX;
        });

        item.addEventListener('touchmove', (e) => {
            const diff = touchStartX - e.touches[0].clientX;
            if (Math.abs(diff) > 50) {
                e.preventDefault();
                const direction = diff > 0 ? -1 : 1;
                item.style.transform = `translateX(${direction * 20}px)`;
            }
        });

        item.addEventListener('touchend', () => {
            item.style.transform = '';
        });
    });

    // Optional: Add category post counts (if available in your context)
    listItems.forEach(item => {
        const count = document.createElement('span');
        count.classList.add('category-count');
        // You would need to add data attributes to your template to make this work
        // count.textContent = item.dataset.postCount || '0';
        item.appendChild(count);
    });
});