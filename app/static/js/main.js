// Core JavaScript logic for PQCrypto Web Interface

// Utility: Display temporary alert messages
function showNotification(message, type = 'info') {
    const alertBox = document.createElement('div');
    alertBox.className = `alert alert-${type} alert-dismissible fade show notification-toast`;
    alertBox.role = 'alert';
    alertBox.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
    `;

    alertBox.style.position = 'fixed';
    alertBox.style.top = '20px';
    alertBox.style.right = '20px';
    alertBox.style.zIndex = '1050';
    alertBox.style.minWidth = '300px';

    document.body.appendChild(alertBox);

    setTimeout(() => {
        alertBox.classList.remove('show');
        setTimeout(() => {
            alertBox.remove();
        }, 150);
    }, 5000);
}

// Utility: Copy string content to user's clipboard
function copyToClipboard(text) {
    if (!navigator.clipboard) {
        const tempInput = document.createElement('textarea');
        tempInput.value = text;
        tempInput.style.position = 'fixed';
        tempInput.style.left = '-999999px';
        tempInput.style.top = '-999999px';
        document.body.appendChild(tempInput);
        tempInput.focus();
        tempInput.select();

        try {
            const result = document.execCommand('copy');
            document.body.removeChild(tempInput);
            return result;
        } catch (e) {
            document.body.removeChild(tempInput);
            return false;
        }
    }

    return navigator.clipboard.writeText(text)
        .then(() => true)
        .catch(() => false);
}

// DOM Setup: Add clipboard buttons to readonly text areas
document.addEventListener('DOMContentLoaded', () => {
    const readonlyAreas = document.querySelectorAll('textarea[readonly]');

    readonlyAreas.forEach(area => {
        const wrapper = document.createElement('div');
        wrapper.className = 'position-relative';

        const originalParent = area.parentNode;
        originalParent.replaceChild(wrapper, area);
        wrapper.appendChild(area);

        const clipboardBtn = document.createElement('button');
        clipboardBtn.className = 'btn btn-sm btn-outline-secondary position-absolute';
        clipboardBtn.style.right = '5px';
        clipboardBtn.style.top = '5px';
        clipboardBtn.innerHTML = '<i class="bi bi-clipboard"></i> Copy';

        clipboardBtn.addEventListener('click', () => {
            const copied = copyToClipboard(area.value);
            if (copied) {
                showNotification('Copied to clipboard', 'success');
            } else {
                showNotification('Failed to copy to clipboard', 'danger');
            }
        });

        wrapper.appendChild(clipboardBtn);
    });
});

// Enhance card UI interaction with hover effects
document.addEventListener('DOMContentLoaded', () => {
    const algoCards = document.querySelectorAll('.card');

    algoCards.forEach(card => {
        card.addEventListener('mouseenter', function () {
            this.style.transform = 'translateY(-10px)';
            this.style.boxShadow = '0 10px 20px rgba(0, 0, 0, 0.2)';
        });

        card.addEventListener('mouseleave', function () {
            this.style.transform = 'translateY(-5px)';
            this.style.boxShadow = '0 4px 6px rgba(0, 0, 0, 0.1)';
        });
    });
});
