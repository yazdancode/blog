// داده‌های کاربر از قالب HTML استخراج می‌شود
document.addEventListener('DOMContentLoaded', () => {
    const userName = document.getElementById('userName').textContent.trim();
    const userEmail = document.getElementById('userEmail').textContent.trim();
    const userBio = document.getElementById('userBio').textContent.trim();

    // داده‌ها به صورت JSON تبدیل می‌شوند
    const userData = {
        name: userName,
        email: userEmail,
        bio: userBio,
    };

    // داده‌های JSON در خروجی نشان داده می‌شود
    const jsonOutput = document.getElementById('jsonOutput');
    jsonOutput.textContent = JSON.stringify(userData, null, 4);
});
