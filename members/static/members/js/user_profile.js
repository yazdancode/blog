// استخراج داده‌ها و تبدیل به JSON
document.addEventListener('DOMContentLoaded', () => {
    const userName = document.getElementById('userName').textContent.trim();
    const userEmail = document.getElementById('userEmail').textContent.trim();
    const userBio = document.getElementById('userBio').textContent.trim();

    // داده‌های شبکه‌های اجتماعی
    const socialLinks = {};
    document.querySelectorAll('.bi').forEach(icon => {
        const link = icon.parentElement;
        const network = link.title.replace('مشاهده ', '').trim();
        socialLinks[network] = link.href || 'ثبت نشده است';
    });

    // تبدیل اطلاعات به JSON
    const userData = {
        name: userName,
        email: userEmail,
        bio: userBio,
        socialLinks: socialLinks,
    };

    // نمایش JSON در خروجی
    const jsonOutput = document.getElementById('jsonOutput');
    jsonOutput.textContent = JSON.stringify(userData, null, 4);
});
